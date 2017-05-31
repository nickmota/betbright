from datetime import datetime

def validate_date(date_text):
    if not isinstance(date_text, str):
        raise ValueError('Incorrect data format, should be a string')
    try:
        return datetime.strptime(date_text, '%d-%m-%Y %H:%M')
    except ValueError:
        raise ValueError('Incorrect data format, should be DD-MM-YYYY H:M')
