def fib(n):
    fib1 = fib2 = 1
    i = 2 
    while i < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib_sum

yes_or_no = "y"

while (yes_or_no == "y" or yes_or_no == "Y"):
    in_max_fibonat = int (input ("Какой элемент ряда Фибоначчи ищем? ")) 
    # for i in range (in_max_fibonat):   
    #     print (fib (i))
    print (fib (in_max_fibonat))
    yes_or_no = input ("Для продолжения нажмите y или Y: ")