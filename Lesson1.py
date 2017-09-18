def even_or_odd(num):

    if num % 4 == 0:
        print("Dyelyatso na 4")
    elif num % 2 == 0:
        print("Chetnoe")
    else:
        print("Nechotnoye")


def main():
    even_or_odd(int(input("Vvedite chislo   ")))


if __name__ == "__main__":
    main()
