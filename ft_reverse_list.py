def ft_reverse_list(listt):
    revers_list = []
    for item in listt[::-1]:
        if type(listt) == list:
            revers_list.append(ft_flatten_list(item))
        else:
            revers_list.append(item)
    return revers_list

liste2=[[1, 2], [3, 4], [5, 6, 7]]
print(ft_reverse_list(liste2))