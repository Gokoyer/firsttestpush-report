
#4.6 Write a program to prompt the user for hours and rate per hour using input
#to compute gross pay. Pay should be the normal rate for hours up to 40 and
#time-and-a-half for the hourly rate for all hours worked above 40 hours.
#Put the logic to do the computation of pay in a function called computepay()
#and use the function to do the computation. The function should return
#a value. Use 45 hours and a rate of 10.50 per hour to test the program
#(the pay should be 498.75). You should use input to read a string and
#float() to convert the string to a number. Do not worry about error
#checking the user input unless you want to - you can assume the user types
#numbers properly. Do not name your variable sum or use the sum() function.

def computepay(h, r):
    if h <= 40:
        return h * r
    elif h > 40:
        return (((h-40) * r * 1.5) + 40 * r)
h = input("Enter Hours:")
r = input("Enter rates:")
hrs = float(h)
rate = float(r)
p = computepay(hrs, rate)
print("Pay", p)

..............................................
def computepay(h,r):
if h > 40:
pay = 40*r + (h — 40)*(r*1.5)
else:
pay = r*h
p = float(pay)
return p
hrs = raw_input(“Enter Hours:”)
h = float(hrs)
rate = raw_input(“Enter Rate:”)
r = float (rate)
m = computepay(h,r)
print(‘Pay’,m)
..................................
def computepay(h,r):
if h > 40:
p = 1.5 * r * (h - 40) + (40 *r)
else:
p = h * r
return p

h = float(input("Enter Hours:"))
r = float(input("Enter rate per hour:"))

p=computepay(h,r)
print("Pay",p)
