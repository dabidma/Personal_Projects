# this is a script to figure out the least amount of bills you will need for a $ amount

dollar = int(input('What is the amount you need to break: '))
bills = {"Hundreds": 0, "Fifties": 0, "Twenties": 0, "Tens": 0, "Fives": 0, "Ones": 0}

def billbreak(dollar):
    while dollar > 0:
        if dollar%100 == 0:
            bills["Hundreds"] += 1
            dollar -= 100
        elif dollar%50 == 0:
            bills["Fifties"] += 1
            dollar -= 50
        elif dollar%20 == 0:
            bills["Twenties"] += 1
            dollar -= 20
        elif dollar%10 == 0:
            bills["Tens"] += 1
            dollar -= 10
        elif dollar%5 == 0:
            bills["Fives"] += 1
            dollar -= 5
        else:
            bills["Ones"] += 1
            dollar -= 1
    print(bills)

billbreak(dollar)

