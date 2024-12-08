import math
year = int(input("Enter year (4 digits):"))
C = year // 100
Y = year % 100
a = Y % 4
b = Y % 7
c = Y % 19
m = (15 + C - math.floor(C / 4) - math.floor((8 * C + 13) / 25)) % 30
n = (4 + C - math.floor(C / 4)) % 7
d = (19 * c + m) % 30
e = (2 * a + 4 * b + 6 * d + n) % 7
if d == 29 and e == 6:
    month = 4
    day = 19
elif d == 28 and e == 6 and m in [2, 5, 9, 12, 15, 18, 21, 24, 27, 30]:
    month = 4
    day = 18
else:
    easter_date = 22 + d + e
    if easter_date > 31:
        month = 4
        day = easter_date -31
    else:
        month = 3
        day = easter_date

# Output the date of Easter Sunday
print("Easter in the year",year, "is" ,month,day,year)





