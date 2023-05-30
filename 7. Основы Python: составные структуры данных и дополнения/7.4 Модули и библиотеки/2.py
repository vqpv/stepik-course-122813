from datetime import datetime
from calendar import monthrange

start_date = datetime.strptime(input(), '%Y-%m-%d').date()
end_date = datetime.strptime(input(), '%Y-%m-%d').date()

if start_date.month != end_date.month or start_date.year != end_date.year:
    print(monthrange(start_date.year, start_date.month)[1] - start_date.day + 1)
else:
    print((end_date - start_date).days + 1)
