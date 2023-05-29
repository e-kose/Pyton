def ft_flatten_list(sample_list):
    flatten_l = []
    for item in sample_list:
        if type(item) == list:
            flatten_l.extend(ft_flatten_list(item))
        else:
            flatten_l.append(item)
    return flatten_l


liste1 = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(ft_flatten_list(liste1))


##########################################################################################
#################################################################################

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