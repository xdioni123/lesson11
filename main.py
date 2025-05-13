# file_path = "C:/Users/Student/lesson11/leximi.txt"
# file = open(file_path, "r")

# content = file.read()
# print(content)

# with open(file_path, "r") as file:
#     content = file.read()
#     print(content)

# with open(file_path, "r") as file:
#     line1 = file.readline()
#     print(line1)

# with open(file_path, "w") as file:
#     file.write("Hello World")

# with open(file_path, "r") as file:
#     file.seek(20)
#     data = file.read()
#     print(data)

import datetime

koha_aktuale = datetime.datetime.now()

print(koha_aktuale)

print("Year:",koha_aktuale.year)
print("Month:",koha_aktuale.month)
print("Day:",koha_aktuale.day)
print("Hour:",koha_aktuale.hour)
print("Second:",koha_aktuale.second)
print("microsecond:",koha_aktuale.microsecond)

koha_aktuale = datetime.datetime.now().time()

print(koha_aktuale)

time_object = datetime.date(2015, 2, 17)
print(time_object)

duration = datetime.timedelta(days=5, hours=3)
print(duration)

new_Day = koha_aktuale = datetime
print(new_Day)

bday=datetime.timedelta(days=7298)

bday1=koha_aktuale = bday

print(bday1)