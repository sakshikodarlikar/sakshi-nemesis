from django.urls import path
from . import views

urlpatterns = [
    path('user_details/', views.user_details, name='user_details'),
    path('user_update/<str:email>/', views.user_update, name='user_update'),
    path('user_delete/<str:email>/', views.user_delete, name='user_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
]