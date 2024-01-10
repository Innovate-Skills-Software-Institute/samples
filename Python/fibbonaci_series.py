# step 1 : Take input from user
num = int(input("Enter the number : "))
# step 2 : Validation
while(num < 0):
    print("Invalid input. Please enter a valid number.")
    num = int(input("Enter the number : "))

# step 3 : define vars
f0 = 0
f1 = 1
n = 0

if num == 0:
    print(f0)
elif num == 1:
    print(f1)
else:
    # Loop
    r = range(2, num + 1)
    for i in r:
        n = f0 + f1
        f0 = f1
        f1 = n
    print(n)