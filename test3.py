old_list = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]

new_list = []

def my_fun(temp_list):
    for i in temp_list:
        if type(i) == list:
            my_fun(i)
        else:
            new_list.append(i)


my_fun(old_list)
print(old_list)
print(new_list)