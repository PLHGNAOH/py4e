import locale
locale.setlocale(locale.LC_ALL,"vi_VN")

money=30000 # constant

hour_s, minute_s = input("enter start hours: ").split(":")
hour_e, minute_e = input("enter end hours: ").split(":")

hour_s=int(hour_s)
hour_e=int(hour_e)
minute_s=int(minute_s)
minute_e=int(minute_e)

total_hour_s = hour_s + minute_s / 60
total_hour_e = hour_e + minute_e / 60

total_hours= (hour_e - hour_s) + ((minute_e -minute_s) / 60)
    
if total_hour_s  >= 8 and  total_hour_s <= 17 or total_hour_e >=8 and total_hour_e <= 17:
    if total_hours >= 1 and total_hours <= 3:
        x = total_hours * money 
        x= locale.format_string("%d",x,grouping=True)
        print(x,"VND")
    elif total_hours > 3:
        x = 3*money + (total_hours-3)*money*0.6
        x = locale.format_string("%d",x,grouping=True)
        print(x,"VND")
    elif total_hour_s < 1:
        print("you can not book the room :(((")
else:
    if total_hours >= 1 and total_hours <= 3:
        x = total_hours * money
        x = locale.format_string("%d",x,grouping=True)
        print(x,"VND")
    elif total_hours > 3:
        x = 3*money + (total_hours-3)*money*0.7
        x = locale.format_string("%d",x,grouping=True)
        print(x,"VND")
    elif total_hour_s < 1:
        print("you can not book the room :(((")

    
    