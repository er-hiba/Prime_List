n = int(input("Enter an integer: "))

print("Prime integers less than",n,":")

list =[]

for i in range(2, n) :
    divisor_count = 0
    for j in range(1, i+1):
        if i % j == 0 :
            divisor_count += 1
    if divisor_count == 2 :
        list.append(i)

print(list)
