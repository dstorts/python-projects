

# sentence = "What is the Airespeed Velocity of an Unladen Swallow?"
#
# result = {word:len(word) for word in sentence.split()}
#
# print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

#now use dictionary comprehension to convert that weather_c dict to farenheit
#weather_f = {day:((weather_c[day]*(9/5))+32) for day in weather_c}
weather_f = {day:int(((temp_c*(9/5))+32)) for (day, temp_c) in weather_c.items()}

print(weather_f)