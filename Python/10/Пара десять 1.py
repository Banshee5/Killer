def task_1():
    t = monotonic()
    start = round(time(), 0)
    while monotonic() - t != 0:
        user_input = input('Enter: ')
        if user_input != 'off':
            check_time = round(time(), 0)
            left = (1800 - (check_time - start)) / 60
            print('Осталось:', round(left, 2), 'мин')
        else:
            break