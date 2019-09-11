#program that takes in the hours, minutes and seconds then outputs the total number of seconds
hours = int(input("Please input the number of hours"))
minutes = int(input("Please input the number of minutes"))
seconds = int(input("Please input the number of seconds"))

HoursToSeconds = hours * 3600
MinutesToSeconds = minutes * 60

TotalSeconds = HoursToSeconds + MinutesToSeconds + seconds
print(TotalSeconds)
