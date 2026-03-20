count_odd = 0
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 != 0:
        count_odd += 1
print("Number of odd inputs:", count_odd)