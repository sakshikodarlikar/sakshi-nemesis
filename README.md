# nemesis-task

Code Deployed on Heroku - https://sakshi-nemesis.herokuapp.com/


=======================================================================================

 Screen 1: Login Form
1.Email (Input)
2.Password (Input)
3.Login Button
4.SignUp Link


Screen 2: Sign Up Form
1.Username
2.Email
3.Password
4.Confirm Password
5.Address


Screen 3: User Detail Page
1.All User Detail except password will be shown in table
2.There will be edit and delete option in every row.
3.On Edit option a modal will be option where user details will be edited
4.On delete user details will be deleted
5.Logout option


Note:- User authentication will be through JWT token and Session Should expire in 5 min.

=======================================================================================


All the above objectives completed.



## How to Use and Test this Application on your computer
- run ```pip install -r requirements.txt```  in your shell to install the specified packages with the specified version.
- run the app ```python manage.py runserver```


## How to run this application

- ```https://sakshi-nemesis.herokuapp.com/signup/``` enter Username, Email, Password, Confirm Password, Address and click on the submit button to singup.


- ```https://sakshi-nemesis.herokuapp.com/login/``` login with email and password and click on login button 


- ```https://sakshi-nemesis.herokuapp.com/user_details/``` shows your username and the table contains user details from the User Model

The User Details page consists of 'update' and 'delete' link helps to update and delete the user. The update link redirects to ``` https://sakshi-nemesis.herokuapp.com/user_update/<str:email>/ ``` where updation of the user details take place.


- ```https://sakshi-nemesis.herokuapp.com/logout/``` helps to logout from the account.



### JWT Authentication

When you login a JWT session token is created for 5 minutes.

All the other login required pages check for this token validity and availability.

When you click on logout your current session JWT authentication token is deleted.
