def delenie_chisla(num_1, num_2):
    if num_1 % num_2 == 0:
        print("{} kratno {}".format(num_1, num_2))
    else:
        print ("{} nekratno {}".format(num_1, num_2))

def main():
    temp_1 = int(input("Vvedite pervoye chislo:\n"))
    temp_2 = int(input("Vvedite vtoroye chislo:\n"))
    delenie_chisla(temp_1, temp_2)



if __name__ == "__main__":
    main()
