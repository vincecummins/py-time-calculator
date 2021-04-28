import re
import math

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def add_time(start, duration, day = None):
    hours = int(re.match('^\d+(?=:)', start).group()) 
    minutes = int(re.search('(?<=:)\d+', start).group())
    am_pm = re.search('[a-zA-Z]+$', start).group()
    if am_pm == 'PM':
        two_four = hours + 12
    else:
        two_four = hours
    durat = duration.split(':')
    new_hours = two_four + int(durat[0])
    new_minutes = minutes + int(durat[1])
    if new_minutes >= 60:
        new_hours += 1
        new_minutes -= 60
    days = math.floor(new_hours/24)
    if days > 0:
        if days == 1:
            new_day = '(next day)'
        if days > 1:
            new_day = f'({days} days later)'
    else:
        new_day = ''
    new_hours = new_hours - days * 24
    new_time = time_formatter(new_hours, new_minutes)
    return_string = ''
    if day == None:
        return_string = new_time + ' ' + new_day
    else:
        new_day_of_the_week = days_of_week[(days_of_week.index(day.lower().capitalize()) + days) % 7]
        return_string =  new_time + ', ' + new_day_of_the_week + ' ' + new_day
    return return_string.strip()

def time_formatter (hours, minutes):
    if minutes < 10:
        new_minutes = '0' + str(minutes)
    else:
        new_minutes = str(minutes)
    if hours > 12:
        new_hours = hours - 12
        tod = ' PM'
    elif hours == 0:
        new_hours = 12
        tod = ' AM'
    elif hours == 12:
        new_hours = 12
        tod = ' PM'
    else:
        new_hours = hours
        tod = ' AM'
    return str(new_hours) + ':' + new_minutes + tod




