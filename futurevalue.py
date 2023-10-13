import math

present_value = float(input("Enter current bank balance:"))
interest=float(input("Enter interested rate (in decimal):"))
time=float(input("Enter the amount of time (in year):"))

def power(i,t,p):
    value= math.pow(i + 1, t)*p
    return value

print(power(interest, time,present_value))
