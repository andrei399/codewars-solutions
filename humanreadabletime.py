#https://www.codewars.com/kata/52742f58faf5485cae000b9a
def format_duration(seconds):
    if seconds == 0:
        return 'now'
    time_stamps = [[31536000, ' year'], [86400, ' day'], [3600, ' hour'], [60, ' minute'], [1, ' second']]
    return_list = []
    for time_in_seconds, time in time_stamps:
        if seconds >= time_in_seconds:
            string_to_append = time
            if seconds//time_in_seconds > 1:
                string_to_append = time + 's'
            return_list.append(str(seconds//time_in_seconds) + string_to_append)
            seconds = seconds % time_in_seconds
    return (', '.join(return_list)[::-1].replace(', '[::-1], ' and '[::-1], 1))[::-1]