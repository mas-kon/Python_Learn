def up_low_string (str):
    up_char = 0
    low_char = 0
    other_char = 0
    num_of_chars = len (str)
    for i in range(num_of_chars):
        if str[i].isupper():
            up_char = up_char + 1
        elif str[i].islower():
            low_char = low_char + 1
        else:
            other_char = other_char + 1
    if low_char >= up_char:
        new_str = str.lower()
    else:
        new_str = str.upper()
    print ("Больших букв - {}".format(up_char))
    print ("Маленьких букв - {}".format(low_char))
    print ("Иных символов - {}".format(other_char))
    print (new_str)


yes_or_no = "y"


while (yes_or_no == "y" or yes_or_no == "Y"):
    up_low = str (input ("Введите строку: "))         
    up_low_string  (up_low)
    yes_or_no = input ("Для продолжения нажмите y или Y: ")