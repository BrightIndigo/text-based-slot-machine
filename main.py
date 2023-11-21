import random

class User:
    def __init__(self):
        self.money = 0

    def deposit(self):
        print("Enter the amount of money you want to deposit:")
        amount = int(input(">"))
        self.money = amount

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

User = User()
User.board()
