from datetime import date
from dateutil.relativedelta import relativedelta

    
    
def calculate_dates(SEGMENT_MONTH_COUNT, date_input:date):
    day_today = int(date_input.strftime("%d"))
    TRAFFIC_MONTH_LAST = -1 if day_today > 4 else -2
    end_date = date.today()-relativedelta(months=-TRAFFIC_MONTH_LAST)
    start_date = (end_date - relativedelta(months=SEGMENT_MONTH_COUNT)).strftime("%Y-%m") #to ingest last months of data
    end_date = end_date.strftime("%Y-%m")
    return {'start_date': start_date, 'end_date':end_date}


