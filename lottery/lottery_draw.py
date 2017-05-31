from datetime import datetime, timedelta

from .validates import validate_date


def calculate_next_draw_date(date_time=None):
    '''
        Calculates which is the next date of
        the draw based on a specific day or the current date
        params:
        date_time: Specific date to calculate the next draw
    '''
    date_time = validate_date(date_time) if date_time else datetime.now()
    
    wednesday = get_next_wednesday(date_time)
    saturday = get_next_saturday(date_time)

    if date_time <= wednesday <= saturday:
        return wednesday.strftime('%d-%m-%Y %A %H:%M')

    return saturday.strftime('%d-%m-%Y %A %H:%M')



def get_next_wednesday(date_time):
    '''
        Calculates Wednesdays and if it has already occurred, take the next
    '''
    wednesday = date_time.replace(
        hour=8,
        minute=0,
        second=0,
        microsecond=0
    ) + timedelta(days=3-date_time.isoweekday())

    if date_time > wednesday:
        wednesday += timedelta(days=7)

    return wednesday


def get_next_saturday(date_time):
    '''
        Calculates saturdays and if it has already occurred, take the next
    '''
    saturday = date_time.replace(
        hour=8,
        minute=0,
        second=0,
        microsecond=0
    ) + timedelta(days=6-date_time.isoweekday())

    if date_time > saturday:
        saturday += timedelta(days=7)

    return saturday