result = {}
musik = input("Введите данные в виде (место в чарте, исполнитель, название)").lower().split(",")
while musik !="off":
    n_m = musik.split(",")
    result[(n_m[0], n_m[1])] = n_m[2]
    musik = input("Введите данные в виде (место в чарте, исполнитель, название)").lower()
print(result)