def fib(n):
    if n < 3:
        return 1
    f_elem = fib(n-1) + fib(n-2)
    return f_elem

yes_or_no = "y"

while (yes_or_no == "y" or yes_or_no == "Y"):
    in_max_fibonat = int (input ("Какой элемент ряда Фибоначчи ищем? "))
    for i in range (1, in_max_fibonat + 1):
        print (fib (i))
    yes_or_no = input ("Для продолжения нажмите y или Y: ")