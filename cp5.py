def system():
    a = int(input("Введите число для перевода в двоичную систему: "))
    x = ""
 
    while a > 0:
        b = str(a % 2)
        x = b + x
        a = int(a / 2)

    print(x)
 
system()
