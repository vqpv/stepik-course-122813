from datetime import datetime, timedelta, time, timezone
from zoneinfo import ZoneInfo


d = datetime.fromisoformat(input())
custom_tz = timezone(offset=-timedelta(hours=3, minutes=46))
moskow_tz = ZoneInfo("Europe/Moscow")

print(d.astimezone(custom_tz).isoformat())
print(d.astimezone(moskow_tz).isoformat())
