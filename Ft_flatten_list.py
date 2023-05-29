def ft_flatten_list(sample_list):
    flatten_l = []
    for item in sample_list:
        if type(item) == list:
            flatten_l.extend(ft_flatten_list(item))
        else:
            flatten_l.append(item)
    return flatten_l
sample_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(ft_flatten_list(sample_list))