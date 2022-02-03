def old_enough(age):
    """"Which rated movie can someone watch based on their age?"""
    if age >= 17:
        print("Can see a rated R movie!")
    elif age < 17 and age > 12:
        print("Can see a rated PG-13 movie")
    else:
        print("Can only see rated PG movies")


#Test the funtion to check if the math checks out!
old_enough(45) # R
old_enough(17) # R
old_enough(13) # PG-13
old_enough(12) # PG only
old_enough(4) # PG only 