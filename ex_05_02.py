largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        num = int(num)
    except:
        print('invalid input')
        continue
    if largest == None or num > largest:
        largest = num
    elif smallest == None or smallest > num:
        smallest = num

print('maximum is', largest)
print('minimum is', smallest)
