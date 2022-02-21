import time, datetime, math
s = input("Input Year YYYY MM :")
list = list(map(int, s.split()))
a = time.mktime(datetime.datetime.now().timetuple()) - time.mktime(datetime.datetime(list[0], list[1], list[2]).timetuple())
print("In Years: " + str(math.floor(a / 31536000)) + "\nIn Months: " + str(math.floor(a / 2628288 )) + "\nIn Days: " + str(math.floor(a / 86400 ))+ "\nIn Hours: " + str(math.floor(a / 3600 ))+ "\nIn Minutes: " + str(math.floor(a / 60 ))+"\nIn Seconds: " + (str(math.floor(a))) )
