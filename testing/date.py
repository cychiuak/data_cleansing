from datetime import datetime, timezone

publish_date_str = "2019-12-31T23:59:59-04:00"
publish_date = datetime.fromisoformat(publish_date_str)
tzinfo = publish_date.tzinfo
print(tzinfo)

print(publish_date)
if publish_date < datetime(2020, 1, 1, tzinfo=tzinfo):
    print("The publish date is before January 1, 2020")