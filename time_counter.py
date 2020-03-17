from datetime import time, timedelta

def read_times_from_file(some_file):

    my_file = open(some_file, 'r')
    lines = my_file.readlines()

    t = []
    for line in lines:
        m, s = line.strip().split(':')
        t.append(time(minute=int(m), second=int(s)))

    return t


def get_total_time(times):

    cummulative_duration = timedelta(0,0)
    for t in times:
        duration = timedelta(minutes=t.minute, seconds=t.second)
        cummulative_duration += duration

    return cummulative_duration


times = read_times_from_file('times.txt')
duration = get_total_time(times)

print(duration)