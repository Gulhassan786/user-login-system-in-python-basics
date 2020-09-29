#                                         ******** USER LOGIN SYSTEM *******
# In this program we have 5 functions 1) forggot_user_password , 2) forggot_user_mail , 3) forggot_user_name , 4) user_login , 5) user_singup

# Two functions are really important , 1) user_signup function takes data from user and save it in dic_user_data dictionary .

# 2) user_login it takes data for login and store it into login dictionary than it camperes login data with signup data if both are same then users login will successgfull if user_name is incorrect than it askes from user to forggot user name through forggot_user_name() function , if user mail is incorrect than it askes user to forggot or change the user E-mail by forggot_user_mail() function  and if user forggot the password than it will askes user to forggot password by using forggot_user_password() function .

# when we are asking from user his/her name , email and password we have to write seprate line for that but due to this dictionary we can as user his/her
# data in single line by the loop and its values dropped their by there index .as on line number 20 .
datao = [" Name ", " E-mail ", " Password "]

# dic_user_data is dictionary for the storing of users signup data
dic_user_data = {"name": "", "mail": "", "password": ""}

# login is dictionary for  storing data which is givin by user for the login and we campere that data with the signup_data
login = {"name": "", "mail": "", "password": ""}


# If user forggot his / her password then through this function he / she will rest password and set new one and again login .
def forggot_user_password():
    user_new_password = input("\n\nEnter new pass word!")
    dic_user_data["password"] = user_new_password
    print("\n\nData for login with updated password \n\n")
    for i in range(0, 3):
        user_login = input(
            f"Enter  {datao [i]} :  ")
        if i == 0:
            login["name"] = user_login
        elif i == 1:
            login["mail"] = user_login
        else:
            login["password"] = user_login
    if login["name"] == dic_user_data["name"] and login["mail"] == dic_user_data["mail"] and login["password"] == dic_user_data["password"]:
        print("\n\n Hurry! login succeded :) and password is updated ")
    else:
        print("login failed :(")


# If user forggot his/her E-mail than throgh this function he/she can rest it easly and login back with new E-mail
def forggot_user_mail():
    user_new_email = input("Enter you new E-mail")
    dic_user_data["mail"] = user_new_email
    print("\n\n Data for login with updated E-mail\n\n")
    for i in range(0, 3):
        user_login = input(f"Enter  {datao[i]} : ")
        if i == 0:
            login["name"] = user_login
        elif i == 1:
            login["mail"] = user_login
        else:
            login["password"] = user_login
    if login["name"] == dic_user_data["name"] and login["mail"] == dic_user_data["mail"] and login["password"] == dic_user_data["password"]:
        print("\n\n Hurry! login succeded :) and E-mail is updated ")
    else:
        print("login failed :(")


# If user forggot user name than through this function he/she can rest user name and set new one and login again
def forggot_user_name():
    User_new_name = input("Enter your new user name")
    dic_user_data["name"] = User_new_name
    print("\n\nData for login with updated User-name \n\n")
    for i in range(0, 3):
        user_login = input(f"Enter  {datao[i]} : ")
        if i == 0:
            login["name"] = user_login
        elif i == 1:
            login["mail"] = user_login
        else:
            login["password"] = user_login
    if login["name"] == dic_user_data["name"] and login["mail"] == dic_user_data["mail"] and login["password"] == dic_user_data["password"]:
        print("\n\n Hurry! login succeded :) and user-name is updated ")
    else:
        print("login failed :(")
    print(login)


# signup_web is a varaible which asks from user to singup or not for a website if he says yes then user_signup funtion will run otherwise it will not/call.
signup_web = input("Do you want to signup for this web-site ? ")

# storing signup data for campering with login data it matches or not


def user_signup():
    print("Data for signup \n\n")
# This loop run 3 times ask from user 3 things name , mail and password but these name will come from the list datao by insertin there index in datao[]using i.
    for i in range(0, 3):

        # datao is list which contain 3 elements which will be dropped her by the index one by one
        user_signup_data = input(
            f"Enter  {datao[i]}: ")

        if i == 0:
            # here we are assigning data of name entering by user in to key of dic_user_data dict (name)
            dic_user_data["name"] = user_signup_data
        elif i == 1:
            # here we are assigning data of mail entering by user in to key of dic_user_data dict (mail)
            dic_user_data["mail"] = user_signup_data
        elif i == 2:
            # here we are assigning data of password entering by user in to key of dic_user_data dict (pas)
            dic_user_data["password"] = user_signup_data
    print("\n\nConratulation! you have singup for this web-site \n\n")


# IN login_user function we are  getting data from user for login and storing it for checking either data of login matches with data of signup
def user_login():
    print("\n\nData for login \n\n")
    for i in range(0, 3):
        # This loop run 3 times ask from user 3 things name , mail and password but these name will come from the list datao by insertin there index in datao[]using i.
        user_login_data = input(
            f"Enter  {datao [i]} :  ")
        if i == 0:
            # here we are assigning data of name entering by user in to key of login dict (name)
            login["name"] = user_login_data
        elif i == 1:
            # here we are assigning data of mail entering by user in to key of login dict (mail)
            login["mail"] = user_login_data
        else:
            # here we are assigning data of password entering by user in to key of login dict (password)
            login["password"] = user_login_data

# checking either information for login is correct or not as before given by user for  signup .
    if login["name"] == dic_user_data["name"] and login["mail"] == dic_user_data["mail"] and login["password"] == dic_user_data["password"]:
        print("\n\n Hurry! login succeded :)")

    elif login["name"] != dic_user_data["name"]:
        print(
            "\n\nlogin failed! User-name is incorrect :(")
        # asking from user for rest user name by ask variable
        ask = input("do you want to forggot your User-name ")
        if ask == "y" or ask == "yes" or ask == "YES":
            # forggot_user_name() is a function through which user can re-set new user name
            forggot_user_name()
        else:
            print("As your whish :) \n\n we do not rest your User-name")

    elif login["mail"] != dic_user_data["mail"]:
        print(
            "\n\nlogin failed! User-email is incorrect :(  ")
        # asking from user for rest E-mail by ask variable
        ask = input("do you want to forggot your E-mail ")
        if ask == "y" or ask == "yes" or ask == "YES":
            # forggot_user_mail() is a function through which user can re-set new E-mail
            forggot_user_mail()
        else:
            print("As your whish :) \n\n we do not rest your E-mail")

    elif login["password"] != dic_user_data["password"]:
        print(
            "\n\n Login failed! , User-password is incorrect :(\n\n")
        # asking from user for rest password by ask variable
        ask = input("do you want to forggot password ")
        if ask == "y" or ask == "yes" or ask == "YES":
            # forggot_user_password() is a function through which user can re-set new password
            forggot_user_password()
        else:
            print("As your whish :) \n\n we do not rest your password")


# This condition checking if user says yes he want to signup for this website than user_signup function will run otherwise it will not. And the answer of user
#  will be stored in a variable sugnup_web which is decleared above on the top for the sack of users will either he/she will or will not signup .
if signup_web == "yes" or signup_web == "Yes" or signup_web == "YES" or signup_web == "y":
    user_signup()


# this variable lo means login asks user to login if he says yes then login_user function will run otherwise it will not run / call.
lo = input("do you want to login ?")

# This condition checking if user says yes he want to login for this website than login_user function will run otherwise it will not.And the answer of user
#  will be stored in a variable ( lo ) which is decleared above . for the sack of users will either he/she will or not login .
if lo == "yes" or lo == "Yes" or lo == "YES" or lo == "y":
    user_login()
