def add_time(start, duration, starting_day=None):
    # Get start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Get duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Convert start time into 24h format
    if period == 'PM':
        start_hour += 12

    # Get total minutes
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    # Get final hour and minute
    final_hour = total_minutes // 60 % 24
    final_minute = total_minutes % 60

    # Get AM or PM
    final_period = 'AM' if final_hour < 12 else 'PM'

    # Convert final hour to 12h format
    if final_hour > 12:
        final_hour -= 12
    elif final_hour == 0:
        final_hour = 12

    # Days later 
    days_later = total_minutes // (24 * 60)

    # Get day of the week
    if starting_day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days_of_week.index(starting_day.lower().capitalize())
        new_day_index = (start_day_index + days_later) % 7
        new_day = ', ' + days_of_week[new_day_index]
    else:
        new_day = ''
    
    # Combine output
    if days_later == 0:
        days_later_string = ''
    elif days_later == 1:
        days_later_string = ' (next day)'
    else:
        days_later_string = f' ({days_later} days later)'

    return f"{final_hour}:{final_minute:02d} {final_period}{new_day}{days_later_string}"

print(add_time("6:30 PM", "205:12"))