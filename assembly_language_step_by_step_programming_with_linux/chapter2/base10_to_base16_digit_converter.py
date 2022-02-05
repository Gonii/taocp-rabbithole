'''
Converts a base10 number to one or more base16 "digits"
A "digit" being a number in base10 that should be interpreted in base16
'''

#########################
base10Number = 264
convertToBaseNumber = 16
#########################

def get_highest_divisible_number(number, baseNumber):
    '''
    Returns int
    Gets the highest divisible number based on the base number being converted to 
    '''

    # i = 1
    # while True:
    #     divisibleNumber = baseNumber ** i
    #     if int(number / divisibleNumber) == 0:
    #         break
    #     i +=1
    # return baseNumber ** (i-1)
    
    i = 1
    divisibleNumber = baseNumber ** i
    while int(number / divisibleNumber) != 0:
        i +=1
        divisibleNumber = baseNumber ** i
    return baseNumber ** (i-1)

result = []

divisible_number = get_highest_divisible_number(base10Number, convertToBaseNumber)

convertedNumberInBase10 = int(base10Number / divisible_number)
result.append(convertedNumberInBase10)
base10Number = base10Number - (divisible_number * convertedNumberInBase10)


while divisible_number != 1:
    divisible_number = divisible_number / convertToBaseNumber
    convertedNumberInBase10 = int(base10Number / divisible_number)
    result.append(convertedNumberInBase10)
    base10Number = base10Number - (divisible_number * convertedNumberInBase10)

print(result)