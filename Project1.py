# File: Project1.py
# Student: Sanjitha Venkata
# UT EID: sv28325
# Course Name: CS303E
# 
# Date Created: 9/28/2023
# Description of Program: Takes input of month in integer form, outputs calendar month of 2024 

#input month
month = int(input("Enter the number of a month [1..12]: "))

#validate month
while month<1 or month>12:
    print("  Month must be between 1 and 12.  Try again!")
    month = int(input("Enter the number of a month [1..12]: "))

#set specific data for month inputted
if month == 1:
    month="January 2024"
    days=31
    start=1
elif month == 2:
    month="February 2024"
    days=29
    start=4
elif month == 3:
    month="March 2024"
    days=31
    start=5
elif month == 4:
    month="April 2024"
    days=30
    start=1
elif month == 5:
    month="May 2024"
    days=31
    start=3
elif month == 6:
    month="June 2024"
    days=30
    start=6
elif month == 7:
    month="July 2024"
    days=31
    start=1
elif month == 8:
    month="August 2024"
    days=31
    start=4
elif month == 9:
    month="September 2024"
    days=30
    start=0
elif month == 10:
    month="October 2024"
    days=31
    start=2
elif month == 11:
    month="November 2024"
    days=30
    start=5
elif month == 12:
    month="December 2024"
    days=31
    start=0

#print
print()
print(month.center(20))
print("Su Mo Tu We Th Fr Sa")

#loop for spacing for start date
for i in range(start):
    print("   ",end="")

#loop for printing days
col=start-1
for i in range(days):
    if(col<6):
        print(format(i+1,"2.0f"), end=" ")
        col+=1
    elif(col==6):
        col=0
        print("\n", format(i+1,"2.0f"), sep="", end=" ")
    i+=1

print()
