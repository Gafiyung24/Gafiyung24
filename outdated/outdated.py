def main():
    a, b, c = convert_date()
    print(f"{a}-{b:02}-{c:02}")

def convert_date():
    months_a = [
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
    "December"
    ]
    months_ab = [

    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "June",
    "July",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"
    ]
    month_n = range(12)
    days_m = range(31)
    while True:
        user_input = input("Date: ") #taking user's date input
        if user_input.find("/") != -1:#handling dates in the format 8/9/1996
            user_input = user_input.split("/")
            u1 = user_input[0].strip()
            u2 = user_input[1].strip()
            u3 = user_input[2].strip()
            if u1.isnumeric() and u2.isnumeric():
                month = u1
                day = u2
                year = u3
            else:
                day = u1
                month = u2
                year = u3
        elif user_input.find(",") != -1:#handling dates with month spellings and comma
            user_input = user_input.split(", ")
            u1 = user_input[0].split(" ")[0]
            u2 = user_input[0].split(" ")[1]
            year = user_input[1]
            if u1.isnumeric():
                day = u1
                month = u2
            else:
                month = u1
                day = u2

        elif user_input.find(" ") != -1:#handling dates with months spelling without comma
            user_input = user_input.split(" ")
            day = user_input[0]
            month = user_input[1]
            year = user_input[2]
        for i in months_a:
            if month in months_a:#checking if month was fully spelt
                day = int(day)
                try:
                    d = days_m.index(day)
                    m = months_a.index(month)
                except ValueError:
                    pass
                else:#printin out date
                    return year, m+1, d



        for i in months_ab:
            if month in months_ab:#checking if month wasn't fully spelt
                day = int(day)
                try:
                    d = days_m.index(day)
                    m = months_ab.index(month)
                except ValueError:
                    pass
                else:#printin out date
                    return year, m+1, d


        if month.isnumeric() and day.isnumeric():
            month = int(month)
            day = int(day)
            '''for i in month_n:
                if month == i:'''
            try:
                m = month_n.index(month)
                d = days_m.index(day)
            except ValueError:
                pass
            else:
                return year, m, d


main()












