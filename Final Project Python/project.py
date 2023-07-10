import sys
import requests
import datetime
from pprint import pprint
import cowsay


def main():
        if len(sys.argv) < 4:
            cowsay.ghostbusters("Usage as follows; type in: project.py (latitude format: decimal) (longitude format: decimal) (date format: YYYY-MM-DD, or 'today'/'tomorrow') --> without parantheses")
            sys.exit
        elif len(sys.argv) > 4:
            cowsay.ghostbusters("Usage as follows; type in: project.py (latitude format: decimal) (longitude format: decimal) (date format: YYYY-MM-DD 'today'/'tomorrow') --> without parantheses")
            sys.exit
        else:
            if validate(sys.argv[3]) == True:
                selection = input(
                    "What are you interested in? The time of sunrise, sunset, first light, last light, dawn, dusk, solar noon, golden hour, the day length, the time zone or everything? "
                )
                selection = selection.lower()
                choice = user(selection)
                if isinstance(choice, list) == True:
                    pprint(choice)
                else:
                    cowsay.tux(choice)
            elif sys.argv[3] in ["today", "tomorrow"]:
                selection = input(
                    "What are you interested in? The time of sunrise, sunset, first light, last light, dawn, dusk, solar noon, golden hour, the day length, the time zone or everything? "
                )
                selection = selection.lower()
                choice = user(selection)
                if isinstance(choice, list) == True:
                    pprint(choice)
                else:
                    cowsay.tux(choice)
            else:
                cowsay.ghostbusters("Incorrect date format --> YYYY-MM-DD / today / tomorrow")
                sys.exit



def request(arg1, arg2, arg3):
    response = requests.get(
        f"https://api.sunrisesunset.io/json?lat={arg1}&lng={arg2}&date={arg3}"
    )
    return response


def validate(date_text):
    try:
        datetime.date.fromisoformat(date_text)
        return True
    except ValueError:
        return False

def user(input):
    response = request(sys.argv[1], sys.argv[2], sys.argv[3])
    o = response.json()
    sunrise = "Sunrise is at " + o["results"]["sunrise"]
    sunset = "Sunset is at " + o["results"]["sunset"]
    first_light = "The first light shines at " +  o["results"]["first_light"]
    last_light = "The last light is seen at " +  o["results"]["last_light"]
    dawn = "Dawn is at " + o["results"]["dawn"]
    dusk = "Dusk is at " + o["results"]["dusk"]
    solar_noon = "Solar Noon is at " +  o["results"]["solar_noon"]
    golden_hour = "The golden hour is expexted at " + o["results"]["golden_hour"]
    day_length = "The day length is approximately " + o["results"]["day_length"]
    timezone = "The timezone is " + o["results"]["timezone"]
    everything = [sunrise,
        sunset,
        first_light,
        last_light,
        dawn,
        dusk,
        solar_noon,
        golden_hour,
        day_length,
        timezone]
    if input == "everything":
        return everything
    elif input == "sunrise":
        return sunrise
    elif input == "sunset":
        return sunset
    elif input == "first light":
        return first_light
    elif input == "last light":
        return last_light
    elif input == "dawn":
        return dawn
    elif input == "dusk":
        return dusk
    elif input == "solar noon":
        return solar_noon
    elif input == "golden hour":
        return golden_hour
    elif input == "day length":
        return day_length
    elif input == "timezone":
        return timezone
    else:
        cowsay.ghostbusters("please choose correct category to display")
        raise ValueError


if __name__ == "__main__":
    main()
