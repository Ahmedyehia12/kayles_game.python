
#[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]

try:
    a = [] # The main list of the game

    x = int(input("enter arbitarary number:")) 
    for i in range(1, x + 1):
        a.append(i % 10) # Filling the list with numbers from 0 to 9
    print("Numbers are", a)

    check = True
    while check:
        for player in ["1", "2"]:
            two_adj_numbers = False
            for i in range(len(a) - 1): # Checking if there is still two consecutive numbers
                if a[i] != "-" and a[i + 1] != "-" :
                    two_adj_numbers = True
            n1 = int(input("player " + player + " how many numbers to remove 1 or 2? :"))
            while (n1 != 1 and n1 != 2) or (n1 == 2 and two_adj_numbers == False): # Checking if the user's input is valid or not
                print("invalid input")
                n1 = int(input("player " + player + " how many numbers to remove 1 or 2? :"))
            print(a)

            if n1 == 1:
                p1 = int(input("player " + player + " choose a number:"))
                while a[p1 - 1] == '-'  or p1 > x: # Checking if the number the player choosed is not already picked or out of index
                    print("invalid input")
                    print(a)
                    p1 = int(input("player " + player + " choose a number:"))
                a[p1 - 1] = "-"
                print(a)
                if a.count("-") == x: # The game ends when all numbers are picked
                    check = False
                    print(" player "+ player + " won !")
                    break
                else:
                    check = True
            elif n1 == 2:
                p1 = int(input("player" + player + " choose the first number:"))
                while a[p1 - 1] == "-" or p1 > x: # Checking if the number the player choosed is not already picked or out of index

                    print("invalid input")
                    print(a)
                    p1 = int(input("player " + player + " choose the first number:"))
                    print(a)
                p2 = int(input("player" + player + " choose the second number: "))
                while a[p2 - 1]  == "-" or p2 > x: # Checking if the second number is not already picked or out of index
                    print("invalid input")
                    print(a)
                    p2 = int(input("player" + player + " choose the second number:"))
                c = p1 - p2
                while c != -1 and c!= 1 :
                    print("numbers are not adjacent ")
                    p1 = int(input("player " + player + " choose the first number:"))
                    p2 = int(input("player" + player + " choose the second number: "))
                    c = p1 - p2
                a[p1 -1] = "-"
                a[p2 - 1] = "-"
                print(a)
                if a.count("-") == x: # The game ends when all numbers are picked

                    check = False
                    print(" player " + player + " won! ")
                    break
                else:
                    check = True

except:
    print("ERROR ")


