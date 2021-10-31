# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).
# Errors fixed were line 10 integer was put in front of input
# Line 15 fixed with the proper expression
# Added colons to line 14, 16
# Created expression for from the far future

year = int(input("Greetings What is your year of origin?"))
'''
Range:   _________________|1900_____________________|2020_________________
           past                  present                     future

            year <= 1900         1900 < year < 2020      year >= 2020
                                                         
'''
if year <= 1900:
    print("Woah, that's the past!")
'''
elif year > 1900 and year < 2020:           
    print("That's totally the present!")
else:
    print(Far out, that;s the future!!")
'''
elif year > 1900 or year < 2020:           
    print("That's totally the present!")
if year > 2020:                            
    print("Far out, that's the future!!")

