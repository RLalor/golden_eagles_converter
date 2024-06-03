#App name: War Thunder currency converter
from pprint import pprint

baht = 1
_20000 = 6.557377049180328
_10000 = 5.878894767783657
_5000 = 5.9523809523809526
_2500 = 4.325259515570934
_1000 = 3.8910505836575875
_150 = 4.054054054054054

current_rates = {"20000": _20000, "10000": _10000, "5000": _5000, "2500": _2500, "1000": _1000, "150": _150}
print('''Welcome to War Thunder Currency Converter
An app for you to better visualise the real money value of Golden Eagles in War Thunder''')
print("\n")
print("The current rates are:")
pprint(current_rates)

base_ge = int(input("Enter amount of Golden Eagles to check: "))
type_ge = input("Enter the type of Golden Eagles you are checking: ")
if type_ge == "20000":
    type_ge = _20000
elif type_ge == "10000":
    type_ge = _10000
elif type_ge == "5000":
    type_ge = _5000
elif type_ge == "2500":
    type_ge = _2500
elif type_ge == "1000":
    type_ge = _1000
elif type_ge == "150":
    type_ge = _150
else:
    print("Please enter either 20000, 10000, 5000, 2500, 1000 or 150")
print(f"Your Golden Eagles have a value of: {base_ge / type_ge} Thai Baht")


#print("5000")
#print(5000 / 840)
#print(5.95 * 840)
#print("\n")
#print("2500")
#print(2500 / 578)
