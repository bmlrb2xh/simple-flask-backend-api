import datetime

def date_tostring(date: datetime) -> str:
    if not all([date, isinstance(date, datetime)]): return "XXXX-XX-XX XX:XX:XX"
    return date.strftime("%Y-%m-%d %H:%M:%S")
