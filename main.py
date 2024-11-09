import datetime

date1=input("Enter a first date in DD.MM.YYYY HH:MM:SS format: ")
date2=input("Enter a second date in DD.MM.YYYY HH:MM:SS format: ")

data1st=datetime.datetime.strptime(date1,"%d.%m.%Y %H:%M:%S")
data2nd=datetime.datetime.strptime(date2,"%d.%m.%Y %H:%M:%S")

difference=data1st-data2nd
print("Difference between two dates is: {0}".format(difference))