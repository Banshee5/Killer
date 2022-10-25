def timetable(reg):
    if 'расп' in reg.lower():
        print('пн 14:30-16:00,'
              'ср 18:30-20:00,'
              'пт 10:30-13:00')


def teatcher(reg):
    if 'трен' in reg.lower():
        print('Иванов Иван Иванович')


def sum(reg):
    if 'плат' in reg.lower():
        print('с вас 5000 рублей')


def juice(reg):
    if 'сок' in reg.lower():
        name_juice()
        price()


def name_juice():
    print('томатный, банановый или вишневый? ')


def price():
    a = input('вид сока: ')
    if a == 'томатный':
        print('с вас 70 рублей!')
    elif a == 'банановый':
        print('с вас 90 рублей!')
    elif a == 'вишневый':
        print('вас 99 рублей!')
    else:
        print('спасибо за покупку, хорошего дня!')