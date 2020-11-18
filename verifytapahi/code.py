import random
n = []
for i in range(5):
    m = random.randint(1000, 9999)
    n.append(m)
print(n)
a = int(input("Enter the number:"))
for i in range(1, 6):
    b = int(input("Enter the code:"))
    if n[a] == b:
        print("Right Person!!!\n")
        break
    else:
        print("Wrong code")
        print(str(5-i) + " attemts remaining\n")
