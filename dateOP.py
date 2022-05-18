#hint : You should import the date class from the datetime module.
from datetime import date
#A function that when called prints the current date.
def current_date():

    today = date.today()
    day = today.strftime("%d/%m/%Y")
    print("Day =", day)

current_date()