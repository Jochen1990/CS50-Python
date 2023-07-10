from datetime import date, datetime
import inflect
import sys
from dateutil.parser import parse


def main():
    birthday = input("Date of Birth: ")
    word = convert(birthday)
    print(word)

def convert(birthday):
    try:
        parse(birthday, fuzzy=False)
        birthday = datetime.strptime(birthday, '%Y-%m-%d')
        birthday = datetime.date(birthday)
        today = date.today()
        difference = today - birthday
        days = difference.days
        hours = days * 24
        minutes = hours * 60
        inflector = inflect.engine()
        word = inflector.number_to_words(minutes, andword = "")
        word= word.capitalize() + " minutes"
        return word
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()