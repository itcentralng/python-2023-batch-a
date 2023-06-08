# write a program that simulates a website
# Users should be allowed to register
# They should then be allowed to login with their email and password
# If their email and password are correct, the website should welcome them by their names
# If their email is correct and their password is not, notify them that their password is 
# wrong. if their email is wrong and their password is correct, notify them  their email 
# is wrong. If neither are correct, tell them their credentials are invalid.

print('Web')
name = input('enter your name ')
email = input('enter your email ')
password = input('enter your password ')

print('site')
email2 = input('enter your email ')
password2 = input('enter your password ')

if email == email2:
    if password == password2:
        if len(password) < 6 :
            print('Welcome to our website ', name)
        else:
            print('password is too long')
    else:
        print('wrong password')
else:
    print('wrong email')         