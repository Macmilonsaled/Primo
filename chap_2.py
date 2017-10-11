def stats_dict(hp, mp, st):
    new_dict = {
        'hp': hp,
        'mp': mp,
        'st': st
    }
    return new_dict


def is_it_true(something):
    if something:
        print('true')
    else:
        print('false')


lists = ['list_1,', 23, 'september', "octoberfest",
         [23, 5435, 3546],
          23]

print(lists[-2])
print(lists[2:4])

lists.append('unity')
lists.insert(0, "2-car")
lists.extend([2, 3, 1, 4, 5, 6, 7])
lists.pop()
lists.pop()

print(lists[:])
print(lists.count(23))
print(lists.index('september'))


PERS_STATS = {
    'pers_1': stats_dict(101010, 1010101, 1232),
    'pers_2': stats_dict(10, 10, 10),
    'pers_3': stats_dict(10, 14, 12),
}

print(PERS_STATS)
