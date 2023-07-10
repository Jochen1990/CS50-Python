# Daytime Data Checker
#### Video Demo:  <URL https://youtu.be/t9yhZWbAOCo>
#### Description:

**Introduction**

Hi,

my name is Jochen from Munich, Germany.

My CS 50 final project is called 'Daytime Data Checker'. It is a basically a terminal base program without a GUI that lets the user check for data on the time of sunrise, sunset, first light, last light, dawn, dusk, solar noon, golden hour, day length and the timezone.

**Main Part**

The user is able to specify for what region or city and day he wants to check this data by inputting latitudinal and longitudinal data (in decimal format e.g.: 38.907192) and a specific date (YYYY-MM-DD format or 'today', 'tomorrow').

If the user does not input in the correct format or omits the necessary command-line arguments, the user gets instructions on how to use the program correctly. This is also the case if the user types in too many command line arguments.

Once the user inputs correct information, an API (https://sunrisesunset.io/api/) is called which returns a JSON object which contains all the categories and information described above.

The user is than prompted with the question of what he wants to get displayed. The user is able to choose one of the categories or he/she can get displayed everything as a list (type) (printed with pprint).

To add a bit of humoristic flair, I imported the cowsay library, so the output is 'told' by the cowsay character 'Tux'.

If the user makes a mistake, the error messages are also displayed with cowsay, but this time with the character 'ghostbusters'.

Of course the inputs by the user (not only the command line arguments) are error checked.

All in all, I included the libraries 'requests', 'sys', 'cowsay' and 'datetime'.

This way, the user can display any information on sunset etc for any given geo-data.




