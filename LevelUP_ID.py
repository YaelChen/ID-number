
def id_num(id):
    id_list = []
    for x in range(8):
        if x % 2 == 0:
            id_list.append(int(id[x]))
        else:
            n = int(id[x]) * 2
            y = str(n)
            if len(y) > 1:
                n = int(y[0]) + int(y[1])
            id_list.append(n)

    new_num = id_list[0] + id_list[1] + id_list[2] + id_list[3] + id_list[4] + id_list[5] + id_list[6] + id_list[7]
    if new_num % 10 != 0:
        c = ((new_num//10) + 1) * 10
    else:
        c = new_num
    ending_no = c - new_num
    print(f"ending number is {ending_no}.\nID no. is {id_8}{ending_no}.")


id_8 = "03365372"
id_num(id_8)
