date_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
name = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

mon, day = map(int, input().split())

print(name[(sum(date_month[:mon])+day)%7])