import random

class User:
    def __init__(self):
        self.money = 0

    def deposit(self):
        print("Enter the amount of money you want to deposit:")
        amount = int(input(">"))
        self.money += amount

    def board(self):
        floor1 = []
        floor2 = []
        floor3 = []

        for i in range(3):
            i = random.randint(0, 9)
            floor1.append(i)
        for i in range(3):
            i = random.randint(0, 9)
            floor2.append(i)
        for i in range(3):
            i = random.randint(0, 9)
            floor3.append(i)
        col1 = f"{floor1[0]}-{floor1[1]}-{floor1[2]}"
        col2 = f"{floor2[0]}-{floor2[1]}-{floor2[2]}"
        col3 = f"{floor3[0]}-{floor3[1]}-{floor3[2]}"
        print(col1)
        print(col2)
        print(col3)
        if floor1[0] == floor1[1] and floor1[2] == floor1[1]:
            self.money += self.money
            print("win in a row on the first column!")
        elif floor2[0] == floor2[1] and floor2[2] == floor2[1]:
            self.money += self.money
            print("win in a row on the first column!")
        elif floor3[0] == floor3[1] and floor3[2] == floor3[1]:
            self.money += self.money
            print("win in a row on the first column!")
        elif floor1[0] == floor2[1] and floor2[1] == floor3[2]:
            self.money += self.money + self.money
            print("sloping line wins!")
        elif floor1[2] == floor2[1] and floor2[1] == floor3[0]:
            self.money += self.money + self.money
            print("sloping line wins!")

User = User()
User.deposit()
User.board()
User.money -= 50
print(f"Your account balance is: {User.money}$")

while True:
    print("Do you want to play again for 50$? (y/n)")
    decision = input(">")
    if decision == "y":
        User.money -= 50
        User.board()
        print(f"Your account balance is: {User.money}$")
    else:
        break
    if User.money <= 0:
        print("Do you want to deposit money to continue playing? (y/n)")
        yn = input(">")
        if yn == "y":
            User.deposit()
        else:
            break