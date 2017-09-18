def main():
    """Основная функция, выполняется при запуске скрипта"""
    #bar()
    #baz(int(input("Введите шаг  ")),
    #    int(input("Введите колво итераций   ")))
    # получим докстроку для функции main
    print(main.__doc__, )


def foo(iters):
    print("entered function")
    # for <название> in <итератор> 
    for i in range(1, iters+1):
        if i % 2:
            print("итерация {}".format(i))
        else:
            print("идерация {}".format(i))
    print("exited for loop")


def bar():
    for _ in range(1, 11):
        foo(int(input("Введите кол-во итераций  ")))


def baz(step, iters):
    sum = 1
    for n in range(1, iters+1):
        print("iteration {}".format(n))
        sum += step
        print("current sum {}".format(sum))


if __name__ == "__main__":
    main()