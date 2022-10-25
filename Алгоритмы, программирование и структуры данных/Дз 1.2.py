
def numberOfMatches(n):
    matches = 0                         # количество матчей равно нулю
    while n > 1:                        # пока команд больше 1
        if n % 2 != 0:                  # если команд нечетное кол-во
            matches += int(n // 2)      # то нужно сыграть половине команд с другой половиной (за вычетом одной, которая автоматом в след. этап), делим нацело на 2, явно приводим к инту (округление в меньшую сторону)
            n = int(n // 2) + 1         # теперь команд стало 'остаток от деления нацело всех изначальных на 2' + 1 команда
        else:                           # если четное количество команд
            matches += int(n / 2)       # то матчей нужно ровно половина от всех команд (играют n/2 против n/2)
            n = int(n / 2)              # теперь n = половина от изначального кол-ва команд
    return matches                      # возвращаем кол-во матчей
print(numberOfMatches(76345))
