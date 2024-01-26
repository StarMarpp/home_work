"""
Напишите программу которая будет спрашивать пользователя ввод имени пока пользователь не введет off.
Программа должна используя lambda-функцию добавлять к каждому имени надпись "гений".
"""
name_user = input('Your name')
lambda_name = [lambda name: name+'гений']
while name_user:
    print(lambda_name [0] (name_user))
    name_user = input('Your name')
print(lambda_name)