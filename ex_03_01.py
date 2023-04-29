hours = input("Enter Hours:")
rph = input("Enter rate:")
h = float(hours)
r = float(rph)
if h <=40:
    grosspay = h * r
if h > 40:
    grosspay = ((h-40) * r * 1.5) + 40 * r
print('pay:', grosspay)
