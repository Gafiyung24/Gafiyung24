def main():
    #collecting user input and storing in variable T
    T = input("What time is it? ").strip()
    T1 = convert(T)
    #condtional statement to know meals
    if 


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    time_1 = hours + minutes
    return time_1




if __name__ == "__main__":
    main()
