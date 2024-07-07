import datetime


def get_date():
    return datetime.datetime.today().replace(microsecond=0)