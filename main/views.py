from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm,UserUpdateForm
from .models import UserDetail
from rest_framework.response import Response
import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed


# user details
@login_required(login_url='login')
def user_details(request):
    token = request.session.get('jwt')
    if not token:
        raise AuthenticationFailed(detail='No token')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed(detail='Invalid token')
        
    users = User.objects.all()
    user_details = UserDetail.objects.all()
    print(user_details)
    return render(request, 'main/user_details.html', {'users': users, 'user_details': user_details})


# login with email and password
def login_view(request):
    if request.user is not None and request.user.is_authenticated:
        return redirect('user_details')
    if request.method == "POST":
        email = request.POST['email']
        username = User.objects.get(email=email).username
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            'iat': datetime.datetime.utcnow(),
                }

            token = jwt.encode(payload, 'secret', algorithm='HS256')
            request.session['jwt']=token
            return redirect('user_details')
        else:
            return render(request, 'main/login.html', {'error_message': 'Invalid login'})
    return render(request, 'main/login.html')
    

# logout view
@login_required(login_url='login')
def logout_view(request):
    del request.session['jwt']
    logout(request)
    return redirect('login')

# signup view
def signup(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'main/signup.html', {'form': form})

    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})



# delete user_details
@login_required(login_url='login')
def user_delete(request,email):
    token = request.session.get('jwt')
    if not token:
        raise AuthenticationFailed(detail='No token')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed(detail='Invalid token')
    user = User.objects.get(email=email)
    user_details = UserDetail.objects.get(user=user)
    user_details.delete()
    user.delete()
    return redirect('user_details')


# update user_details
@login_required(login_url='login')
def user_update(request,email):
    token = request.session.get('jwt')
    if not token:
        raise AuthenticationFailed(detail='No token')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed(detail='Invalid token')
    user = User.objects.get(email=email)
    user_detail = UserDetail.objects.get(user=user)    
    form = UserUpdateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(user.pk)
            return redirect('user_details')
        else:
            return redirect('user_update',email)

    else:
        form = UserUpdateForm()
    return render(request, 'main/user_update.html', {'form': form, 'user':user_detail})






