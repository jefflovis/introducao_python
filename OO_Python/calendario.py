import calendar as c

# print(c.TextCalendar().formatmonth(2023,2))

# print(c.LocaleTextCalendar(locale='pt-BR').formatmonth(2023,1), c.LocaleTextCalendar(locale='pt-BR').formatmonth(2023,2))

# print(c.day_name[c.weekday(2023,8,14)])

mes = c.monthcalendar(2020,11)
if mes[0][c.THURSDAY] != 0:
    dia = mes[3][c.THURSDAY]
else:
    dia = mes[4][c.THURSDAY]

print(dia)