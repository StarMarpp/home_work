# внутри декоратоора попадают функцию

#Декоратор в обещм виде:
def decorator(func):
    # print('код внутри декоратора')
    def wrapper(x,y):
        print('код до вызова функции')
        func(x,y)
        print('код после вызова функции')
    return wrapper

@decorator
def aplusb(a,b):
    print(f"{a}+{b}=a+b")
    return f"{a}+{b}=a+b"

aplusb(10,20)


