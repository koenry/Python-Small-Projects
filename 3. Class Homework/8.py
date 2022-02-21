from datetime import datetime, timedelta
print(datetime.today())
print(datetime.today() - timedelta(days=5))
print (datetime.today() + timedelta(hours=8))
print(datetime.today().strftime('%Y-%m-%d'))
