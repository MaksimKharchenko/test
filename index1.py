import csv

records = []

with open('acme_worksheet.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        records.append(row)

del records[0]

employees = []
dates = []

for i in records:
    employees.append(i[0])
    dates.append(i[1])

uniqueEmployees = list(set(employees))
uniqueDates = list(set(dates))
uniqueDates.sort()

def user_dict():
    user = {}
    user['name'] = ''
    for i in uniqueDates:
        user[i] = '0'

    return user


def is_user_in_result(user, result):
    for i in result:
        if user == i['name']:
            return i
    return False

def setDate(user, record):
    user[record[1]] = record[2]
    return user


result = []

for i in records:
    is_exist = is_user_in_result(i[0], result)
    if is_exist != False:
        updated = setDate(is_exist, i)
    else:
        user = user_dict()
        user['name'] = i[0]
        result.append(user)

final = []
final.append(['Name-Date'] + uniqueDates)

for i in result:
    values = i.values()
    final.append(list(values))


myFile = open('result.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(final)

print("Writing complete")
