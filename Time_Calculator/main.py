def add_time(start, duration, start_day=None):
    # Extract start time and period (AM/PM)
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    # Convert start time to 24-hour format
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    # Extract duration time
    duration_hour, duration_minute = map(int, duration.split(':'))
    # Calculate end time in 24-hour format
    end_hour = start_hour + duration_hour
    end_minute = start_minute + duration_minute
    if end_minute >= 60:
        end_hour += end_minute // 60
        end_minute %= 60
    end_hour %= 24
    # Convert end time back to 12-hour format
    if end_hour == 0:
        end_hour = 12
        period = 'AM'
    elif end_hour == 12:
        period = 'PM'
    elif end_hour > 12:
        end_hour -= 12
        period = 'PM'
    else:
        period = 'AM'
    end_time = f"{end_hour:02}:{end_minute:02} {period}"
    # Calculate number of days later
    num_days_later = end_hour // 24
    # Determine day of the week if start_day is provided
    if start_day is not None:
        start_day = start_day.capitalize()
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days_of_week.index(start_day)
        end_day_index = (start_day_index + num_days_later) % 7
        end_day = days_of_week[end_day_index]
        end_time += f", {end_day}"
    # Add 'next day' or 'n days later' if applicable
    if num_days_later == 1:
        end_time += " (next day)"
    elif num_days_later > 1:
        end_time += f" ({num_days_later} days later)"
    return end_time
