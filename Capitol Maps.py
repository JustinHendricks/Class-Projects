#The directions for this project were: given a list of places and their coordinates, find out if you are north south east or west of these points. The extra credit was to calculate how far you were from a set point.
#The code only works for specific cases and isn't the best. Uploaded for two reasons. 
#1. This was my first time using dictionaries to simplify how I solve a problem/ get a shorter solution. 
#2. The if statements at the bottom only get the correct answer for certain solutions. The formula given in the instructions wasn't correct, so I had to use math to create a formula for each one. It wasn't anything too complex but I'm proud of it.

coordinates = {
    "K St" : [38.902649],
    "the White House" : [38.897789, -77.036562], 
    "Downing Hall" : [38.921669, -77.021361],
    "Dupont Circle" : [38.909760, -77.043479],
    "Union Station" : [38.897698, -77.007200]
    }
miles_away = 0
user_latitude = float(input("Insert your latitude: "))
user_longitude = float(input("Insert your longitude: "))

for key, value in coordinates.items():
    if len(value) == 1:
        if (user_latitude > value[0]):
            print("You are north of", key)
        elif (user_latitude < value[0]):
            print("You are south of", key)
        else:
            pass
    else:
        if (user_latitude > value[0]):
            print("You are north of", key)
        elif (user_latitude < value[0]):
            print("You are south of", key)
        else:
            pass
        if (user_longitude > value[1]):
            print("You are east of", key)
        elif (user_longitude < value[1]):
            print("You are west of", key)
        else:
            pass
if (abs(1000 * (user_longitude - -77.021361)) > 12) and ((1000 * (user_longitude - -77.021361)) < 30):
    miles_away = abs((  user_longitude - -77.021361) * 92) #Trying to use 53 as the multiplier made all the mile calculations a lot less accurate than ones >70
    miles_away = round(miles_away, 1)
elif abs(1000 * (user_longitude - -77.021361)) < 12:
    miles_away = abs((  user_longitude - -77.021361) * 74) #Trying to use 53 as the multiplier made all the mile calculations a lot less accurate than ones >70
    miles_away = round(miles_away, 1)
elif ((1000 * (user_longitude - -77.021361)) > 30):
    miles_away = abs((  user_longitude - -77.021361) * 94) #Trying to use 53 as the multiplier made all the mile calculations a lot less accurate than ones >70
    miles_away = round(miles_away, 1)

print("You are" , miles_away , "miles from Downing Hall")
