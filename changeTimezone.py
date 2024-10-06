from datetime import datetime, timezone, timedelta
publish_date = "2023-04-01 00:28:00-04:00"
dt = datetime.fromisoformat(publish_date)
tzInfo = dt.tzinfo
print("The timezone is", timezone(timedelta(hours=-5)))
print("month is",dt.month)
print("type of month is",type(dt.month))
if tzInfo == timezone(timedelta(hours=-5)):
    print("The timezone is GMT-5")
    dt_reduced = dt - timedelta(hours=8, minutes=30)
if tzInfo == timezone(timedelta(hours=-4)):
    print("The timezone is GMT-4")
    dt_reduced = dt - timedelta(hours=9, minutes=30)
print("dt is ",dt)
from datetime import datetime, timedelta

def adjust_publish_date(publish_date: str, gmt_offset: int) -> datetime:
    # Parse the ISO format date
    dt = datetime.fromisoformat(publish_date)
    
    # Adjust the time based on the GMT offset
    if gmt_offset == -4:
        adjusted_time = dt - timedelta(hours=9)  # GMT-4 adjusted 9 hours early
    elif gmt_offset == -5:
        adjusted_time = dt - timedelta(hours=8)  # GMT-5 adjusted 8 hours early
    else:
        raise ValueError("Unsupported GMT offset")

    return adjusted_time

# Example usage
publish_date_gmt4 = "2024-10-04T12:00:00"
publish_date_gmt5 = "2024-10-04T12:00:00"

adjusted_gmt4 = adjust_publish_date(publish_date_gmt4, -4)
adjusted_gmt5 = adjust_publish_date(publish_date_gmt5, -5)

print("Adjusted GMT-4:", adjusted_gmt4)
print("Adjusted GMT-5:", adjusted_gmt5)