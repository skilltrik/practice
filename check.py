from datetime import datetime, timezone, timedelta

timezone_offset = 32400
custom_timezone = timezone(timedelta(seconds=timezone_offset))
sunrise_utc = datetime.fromtimestamp(1751916731, tz=timezone.utc)
sunrise_local = sunrise_utc.astimezone(custom_timezone).strftime("%Y-%m-%d %H:%M:%S")
print(sunrise_local)
