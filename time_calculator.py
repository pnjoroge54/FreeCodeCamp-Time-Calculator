def add_time(start, duration, day_of_week=None):
    # Time variables
    hh = int(start.split(':')[0])
    rem = start.split(':')[1]
    mm = int(rem.split(' ')[0])
    AM_PM = rem.split(' ')[1]
    d_hh = int(duration.split(':')[0])
    d_mm = int(duration.split(':')[1])
    
    # Convert to 24h clock
    if AM_PM == 'PM':
        hh += 12

    # Minutes calculations
    n_mm = mm + d_mm  

    if n_mm < 60:
        n_hh = hh + d_hh   
    else:
        n_hh = hh + d_hh + 1
        n_mm %= 60
    
    # Add zero infront of minutes < 10
    if n_mm < 10:
        n_mm = '0' + str(n_mm)

    # Convert AM to PM. 
    if (n_hh % 24) <= 11:
        nAM_PM = 'AM'
    else:
        nAM_PM = 'PM'
        
    n_days = n_hh // 24
        
    # Convert to 12h clock
    if n_hh % 12 == 0:
        n_hh = 12
    else:
        n_hh %= 12
        
    n_time = str(n_hh) + ':' + str(n_mm) + ' ' + nAM_PM    
    
    if day_of_week is None:
        if n_days == 0:
            return n_time
        elif n_days == 1:
            days = ' (next day)'
            return n_time + days
        elif n_days > 1:
            days = str(n_days)
            return n_time + ' (' + days + ' days later)'
    else:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']
        day_of_week = day_of_week.title()
        weekday = (days.index(day_of_week) + n_days) % 7
        weekday = days[weekday]
        if n_days == 0:
            return n_time + ', ' + weekday
        elif n_days == 1:
            days = ' (next day)'
            return n_time + ', ' + weekday + days
        else:
            return n_time + ', ' + weekday + ' (' + str(n_days) + \
        ' days later)'