import calendar
from datetime import datetime

# Get user input
year = int(input("Enter a year (e.g., 2025): "))
month = int(input("Enter a month (1-12): "))

# Display the calendar
print("\n" + "=" * 40)
print(f"CALENDAR FOR {calendar.month_name[month].upper()} {year}")
print("=" * 40)
print(calendar.month(year, month))

# Get today's date
today = datetime.now()

# Check if today falls within the specified month and year
print("=" * 40)
if today.year == year and today.month == month:
    print(
        f"Today is {today.strftime('%B %d, %Y')} "
        f"and it falls within the selected month."
    )
else:
    print(
        f"Today's date ({today.strftime('%B %d, %Y')}) "
        f"does not fall within the selected month and year."
    )
print("=" * 40)