from datetime import datetime
from service.helper_dates import calculate_dates

def test_calculate_dates_1():
    date_str = '12-02-2023'
    today = datetime.strptime(date_str, '%m-%d-%Y').date()
    SEGMENT_MONTH_COUNT = 2
    dates = calculate_dates(SEGMENT_MONTH_COUNT, today)
    print(dates)

def test_calculate_dates_2():
    date_str = '12-10-2023'
    today = datetime.strptime(date_str, '%m-%d-%Y').date()
    SEGMENT_MONTH_COUNT = 2
    dates = calculate_dates(SEGMENT_MONTH_COUNT, today)
    print(dates)

def test_calculate_dates_3():
    date_str = '03-02-2023'
    today = datetime.strptime(date_str, '%m-%d-%Y').date()
    SEGMENT_MONTH_COUNT = 2
    dates = calculate_dates(SEGMENT_MONTH_COUNT, today)
    print(dates)

def test_calculate_dates_4():
    date_str = '03-10-2023'
    today = datetime.strptime(date_str, '%m-%d-%Y').date()
    SEGMENT_MONTH_COUNT = 2
    dates = calculate_dates(SEGMENT_MONTH_COUNT, today)
    print(dates)

def test_calculate_dates_5():
    date_str = '04-11-2023'
    today = datetime.strptime(date_str, '%m-%d-%Y').date()
    SEGMENT_MONTH_COUNT = 2
    dates = calculate_dates(SEGMENT_MONTH_COUNT, today)
    print(dates)

def test_calculate_dates_6():
    date_str = '04-11-203'
    today = datetime.strptime(date_str, '%m-%d-%Y').date()
    SEGMENT_MONTH_COUNT = 2
    dates = calculate_dates(SEGMENT_MONTH_COUNT, today)
    print(dates)


    #### Mal kein Datum, ungülti