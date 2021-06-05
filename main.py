
import datetime
def reverse(fname, lname):
    print(f"First Name:{fname}\nLast Name:{lname}")
    print("---------------reverse------------------ ")
    #print name in reverse
    print(f"{lname}" + "   " + f"{fname}")
def circle_radius(radius):
    #calculate area of radius
   area=(22/7)*radius**2
   print("----------------------------------------------------------------")
    #print area of radius
   print(f"Radius of circle is {radius} and area of circle is :{str(area)}")

def current_date():
       #print current date using build in method datetime.datetime.now() after convert it  into string
       print("Current date is:" + str(datetime.datetime.now()))
def main():
    #print program information
    print("This Python program accepts the radius of a circle from the user and compute the area")
    print("-------------------------------------------------------------------------------------")
    #enter radius from user
    radius = float(input("Enter radius of circle:"))
    #call  circle_radius function
    circle_radius(radius)

    print("\n This program accepts the user's name and  print it in reverse order")
    print("----------------------------------------------------------------------")
    #enter first and last name from user
    fname = input("Please enter your First Name:")
    lname = input("Please enter your Last Name:")

    #call reverse function to reverse print name
    reverse(fname, lname)

    print(" \nThis Python program to display the current date and time")
    print("-----------------------------------------------------------")
    #call function current_date
    current_date()


main()