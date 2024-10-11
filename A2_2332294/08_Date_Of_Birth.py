
def getAstrologicalSign(day, month):
    if month == "december":
        return "Sagittarius" if day < 22 else "Capricorn"
    elif month == "january":
        return "Capricorn" if day < 20 else "Aquarius"
    elif month == "february":
        return "Aquarius" if day < 19 else "Pisces"
    elif month == "march":
        return "Pisces" if day < 21 else "Aries"
    elif month == "april":
        return "Aries" if day < 20 else "Taurus"
    elif month == "may":
        return "Taurus" if day < 21 else "Gemini"
    elif month == "june":
        return "Gemini" if day < 21 else "Cancer"
    elif month == "july":
        return "Cancer" if day < 23 else "Leo"
    elif month == "august":
        return "Leo" if day < 23 else "Virgo"
    elif month == "september":
        return "Virgo" if day < 23 else "Libra"
    elif month == "october":
        return "Libra" if day < 23 else "Scorpio"
    elif month == "november":
        return "Scorpio" if day < 22 else "Sagittarius"


day = int(input("Input birthday: "))
month = input("Input month of birth (e.g. march, july etc): ").lower()
sign = getAstrologicalSign(day, month)
print("Your Astrological sign is:", sign)

