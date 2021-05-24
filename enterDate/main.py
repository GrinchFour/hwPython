monthes = {"Январь": 1, "Февраль": 2, "Март": 3, "Апрель": 4, "Май": 5, "Июнь": 6, "Июль": 7, "Август": 8,
           "Сентябрь": 9, "Октябрь": 10, "Ноябрь": 11, "Декабрь": 12, "Января": 1, "Февраля": 2, "Марта": 3,
           "Апреля": 4, "Мая": 5, "Июня": 6, "Июля": 7, "Августа": 8, "Сентября": 9, "Октября": 10, "Ноября": 11,
           "Декабря": 12, "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
           "August": 8, "September": 9, "October": 10, "November": 11, "December": 12, "1": 1, "2": 2, "3": 3, "4": 4,
           "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "11": 11, "12": 12}

dayMonthes = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def format():
    f = 'f'
    while f != 0 and f != 1:
        print("Введите 1, если формат вводимой даты - русский, 0 - если американский.")
        f = int(input())
    return f


def isDate(d, f):
    if f:
        buff = testDateRus(d)
    else:
        buff = testDateEng(d)
    return buff


def isMonth(isM):
    for i in monthes.keys():
        if isM.lower() == i.lower():
            return 1
    return 0


def testDateRus(d):
    if d[0].isdigit() and d[1].isdigit():
        if 0 < int(d[1]) <= 12 and 0 < int(d[0]) <= 31 and d[2].isdigit():
            return 1
    elif d[0].isdigit():
        if isMonth(d[1]) and 0 < int(d[0]) <= 31 and d[2].isdigit():
            return 1
    return 0


def testDateEng(d):
    if d[0].isdigit() and d[1].isdigit():
        if 0 < int(d[0]) <= 12 and 0 < int(d[1]) <= 31 and d[2].isdigit():
            return 1
    elif d[1].isdigit():
        if isMonth(d[0]) and 0 < int(d[1]) <= 31 and d[2].isdigit():
            return 1
    return 0


def numD(d1, d2):
    ves = 0
    for i in range(1, abs(int(d1[2]))):
        if ((i % 4 == 0) and (i % 100 != 0)) or (i % 400 == 0):
            ves += 1
    days1 = (abs(int(d1[2])) - ves) * 365 + ves * 366
    if testDateRus(d1):
        for i in range(1, monthes.get(d1[1])):
            days1 += dayMonthes.get(i)
        days1 += int(d1[0])
        if (((abs(int(d1[2])) % 4 == 0) and (abs(int(d1[2])) % 100 != 0)) or (
                abs(int(d1[2])) % 400 == 0)) and monthes.get(d1[1]) > 2:
            days1 += 1
    else:
        for i in range(1, monthes.get(d1[0])):
            days1 += dayMonthes.get(i)
        days1 += int(d1[1])
        if (((abs(int(d1[2])) % 4 == 0) and (abs(int(d1[2])) % 100 != 0)) or (
                abs(int(d1[2])) % 400 == 0)) and monthes.get(d1[0]) > 2:
            days1 += 1

    ves = 0
    for i in range(1, abs(int(d2[2]))):
        if ((i % 4 == 0) and (i % 100 != 0)) or (i % 400 == 0):
            ves += 1
    days2 = (abs(int(d2[2])) - ves) * 365 + ves * 366
    if testDateRus(d2):
        for i in range(1, monthes.get(d2[1])):
            days2 += dayMonthes.get(i)
        days2 += int(d2[0])
        if (((abs(int(d2[2])) % 4 == 0) and (abs(int(d2[2])) % 100 != 0)) or (
                abs(int(d2[2])) % 400 == 0)) and monthes.get(d2[1]) > 2:
            days2 += 1
    else:
        for i in range(1, monthes.get(d2[0])):
            days2 += dayMonthes.get(i)
        days2 += int(d2[1])
        if (((abs(int(d2[2])) % 4 == 0) and (abs(int(d2[2])) % 100 != 0)) or (
                abs(int(d2[2])) % 400 == 0)) and monthes.get(d2[0]) > 2:
            days2 += 1
    return abs(days1 - days2)


form1 = format()

buff = 0  # input Dates
while buff == 0:
    print("Введите первую дату корректно:")
    date1 = input()

    date1 = date1.split('/')
    date1 = ' '.join(date1)
    date1 = date1.split('.')
    date1 = ' '.join(date1)
    date1 = date1.split('-')
    date1 = ' '.join(date1)

    date1 = date1.split()  # Convert to list
    if len(date1) == 3:
        buff = isDate(date1, form1)

form2 = format()

buff = 0
while buff == 0:
    print("Введите вторую дату корректно:")
    date2 = input()

    date2 = date2.split('/')
    date2 = ' '.join(date2)
    date2 = date2.split('.')
    date2 = ' '.join(date2)
    date2 = date2.split('-')
    date2 = ' '.join(date2)
    date2 = date2.split()  # Convert to list
    if len(date2) == 3:
        buff = isDate(date2, form2)

print("Number of days -", numD(date1, date2))
