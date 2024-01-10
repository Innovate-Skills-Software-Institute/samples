# Step 1 : Take input from user
num = int(input("Enter the number : ")) # Typecast str to int

while num < 1:
    print("Please enter the number greater than 0")
    num = int(input("Enter the number : "))  # Typecast str to int

# Step 2 : Iterate and do product
ans = 1
r = range(1, num + 1)

for i in r:
    ans *= i

print(ans)