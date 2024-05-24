import datetime

human_time = 'Jan 15, 2023 - 12:05:33'
python_time = datetime.datetime.strptime(human_time, '%b %d, %Y - %H:%M:%S')
full_month = python_time.strftime('%B')
format_date = python_time.strftime('%d.%m.%Y, %H:%M')

print(full_month)
print(format_date)
