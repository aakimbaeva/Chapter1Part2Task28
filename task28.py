list_ = [8, -2, 6, -3, 0, 1, -2, 3, 4]
print(list_)
for i in list_:
    x = list_.index(i)
    if i > 0:
        list_[x] = 1
    elif i < 0:
        list_[x] = -1
    else:
        list_[x] = 0

print(list_)
