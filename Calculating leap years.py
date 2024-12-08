final_year=int(input("Enter a year:"))
initial_year=1600
total_leap_years=0
for year in range (initial_year,final_year + 1):
    if year%4 ==0:
        if year%100!=0 or year%400==0:
            total_leap_years=total_leap_years +1
print (" The total number of leap years between",initial_year, "and",final_year, "is",total_leap_years)


