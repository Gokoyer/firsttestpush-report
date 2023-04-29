# This is to write a program that prompt the user for hours(h) and rate per
#hour(r) using input to compute grosspay. Pay the hourly rate for the Hours
#upto 40 and 1.5 times the hourly rate for all the hours worked above 40 Hours
# Use 45 hours and a rate of 10.50 per hour to test the program

#This is the first option
#rph = input("Enter rate:")
#grosspay = float(hrs) * float(rph)
#if float(hrs) <= 40:
    #print('pay:', grosspay)
#elif float(hrs) > 40:
    #grosspay = (float(hrs)-40.0)*(float(rph)*1.5) + (40.0*float(rph))
    #print('pay:', grosspay)

####################################
# This is the second option
hours = input("Enter Hours:")
rph = input("Enter rate:")
h = float(hours)
r = float(rph)
if h <=40:
    grosspay = h * r
if h > 40:
    grosspay = ((h-40) * r * 1.5) + 40 * r
print('pay:', grosspay)
