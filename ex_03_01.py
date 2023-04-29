#rph = input("Enter rate:")
#grosspay = float(hrs) * float(rph)
#if float(hrs) <= 40:
    #print('pay:', grosspay)
#elif float(hrs) > 40:
    #grosspay = (float(hrs)-40.0)*(float(rph)*1.5) + (40.0*float(rph))
    #print('pay:', grosspay)

####################################
hrs = input("Enter Hours:")
rph = input("Enter rate:")
h = float(hrs)
r = float(rph)
if h <=40:
    grosspay = h * r
if h > 40:
    grosspay = ((h-40) * r * 1.5) + 40 * r
print('pay:', grosspay)
