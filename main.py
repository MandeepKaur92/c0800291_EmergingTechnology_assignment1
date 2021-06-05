import datetime
def reverse(fname, lname):
    print(f"First Name:{fname}\nLast Name:{lname}")
    print("---------------reverse------------------ ")
    print(f"{lname}" + "   " + f"{fname}")
def circle_radius(radius):
   area=(22/7)*radius**2
   print("----------------------------------------------------------------")
   print(f"Radius of circle is {radius} and area of circle is :{str(area)}")

def current_date():
       print("Current date is:" + str(datetime.datetime.now()))
def main():
    print("This Python program accepts the radius of a circle from the user and compute the area")
    print("-------------------------------------------------------------------------------------")
    radius = float(input("Enter radius of circle:"))
    circle_radius(radius)

    print("\n This program accepts the user's name and  print it in reverse order")
    print("----------------------------------------------------------------------")
    fname = input("Please enter your First Name:")
    lname = input("Please enter your Last Name:")
    reverse(fname, lname)

    print(" \nThis Python program to display the current date and time")
    print("-----------------------------------------------------------")
    current_date()


main()