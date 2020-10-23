def two_sum (in_list, in_sum):
    out_lst = []
    for i in range (len (in_list)):
        for j in range(1,(len (in_list))):
            temp_sum = int (in_list[i]) + int (in_list[j])
            if temp_sum == in_sum:
                out_lst = [i, j]
                print (out_lst)
                return 0
            
    print ("Нет такой пары в этом списке!")
    return 0


def str_to_list (in_list):
    out_list = list(in_list.split(","))
    return out_list

yes_or_no = "y"

while (yes_or_no == "y" or yes_or_no == "Y"):
    input_list = str (input ("Введите список через запятую: "))
    input_sum = int (input ("Введите искомую сумму: "))
    temp_list = str_to_list (input_list)
    two_sum (temp_list, input_sum)
    yes_or_no = input ("Для продолжения нажмите y или Y: ")