def find_multipex(x, y):
    z = 0
    lst = []
#    if not isinstance(x, int):
#        print("Число должно быть INT!")
#        return 0
#    elif not isinstance(y, int):
#        print("Лимит должен быть INT!")
#        return 0
    if y < x:
#        print("Лимит должен быть больше числа!")
        print(lst)
        return 0
    else:
        for i in range (1,y):
            i = i * x
            lst.insert(z, i)
            z = z + 1
            if i > y:
                lst.pop() # Костыль :(
                print(lst)
                return         
#            print(i)

yes_or_no = "y"

while (yes_or_no == "y" or yes_or_no == "Y"):
    num_int = int (input ("Введите число: "))
    lim_int = int (input ("Введите лимит: "))         
    find_multipex (num_int, lim_int)
    yes_or_no = input ("Для продолжения нажмите y или Y: ")