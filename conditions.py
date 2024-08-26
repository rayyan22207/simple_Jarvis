def condition(value):
    if value == "Hello":
        return "Hello"
    elif (value == "Weather" or value == "what is the weather"):
        return "weather_api"
    else:
        return "Sorry, I don't understand"
    