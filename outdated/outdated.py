months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


while True:
    try:
        date_user = input("Date: ")
        if date_user.index("/"):
            month = date_user.split("/")[0]
            day = date_user.split("/")[1]
            year = date_user.split("/")[2]
            month = int(month)
            day = int(day)
            year = int(year)
            if month > 12:
                pass
            elif day > 31:
                pass
            else:
                print(f"{year}-{month:02}-{day:02}", end="")
                print()
                break
    except ValueError:
        try:
            if date_user.index(","):
                month = date_user.split(" ")[0].capitalize()
                day = date_user.split(" ")[1]
                day = day.split(",")[0]
                year = date_user.split(" ")[2]
                index_month = months.index(month)
                index_month = int(index_month) + 1
                day = int(day)
                year = int(year)
                if day > 31:
                    pass
                else:
                    print(f"{year}-{index_month:02}-{day:02}", end="")
                    print()
                    break
        except ValueError:
            pass
