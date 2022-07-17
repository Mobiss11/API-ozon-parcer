from datetime import datetime, timedelta

dt = datetime.now()

today = dt.strftime('%Y-%m-%d')
yesterday = dt - timedelta(days=1)
yesterday_good_format = yesterday.strftime('%Y-%m-%d')
