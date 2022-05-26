decimalNumber = 134516736

count = 1
while True:
    value = 2 ** count
    if len(str(value)) >=len(str(decimalNumber)):
        break
    count +=1

print(count)