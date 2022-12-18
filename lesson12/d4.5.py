buses = [
    {
        "delays": ['1h 20m', '25m', '3h', '2h 1m'],
        "status": 'bad',
        "name": "Jacob",
        "route_num": 560
    },
    {
        "delays": ['20m', '5m', '3h'],
        "status": 'great',
        "name": "Moshe",
        "route_num": 769
    },
    {
        "delays": ['2h 3m'],
        "status": 'good',
        "name": "Jack",
        "route_num": 766
    },
    {
        "delays": ['6h'],
        "status": 'great',
        "name": "Mark",
        "route_num": 876
    },
    {
        "delays": ['2h 3m'],
        "status": 'good',
        "name": "Anna",
        "route_num": 456
    },
]


# Implement a function that gets a dictionary of the format above and
# returns its elements sorted first by status (great - good - bad), then by total minutes late, then by name.

def get_total_delay_mins(bus: dict):
    delay_sum = 0
    for delay in bus['delays']:
        d = delay.split()
        for ts in d:
            if 'h' in ts:
                delay_sum += int(ts[:ts.index('h')]) * 60
            if 'm' in ts:
                delay_sum += int(ts[:ts.index('m')])

    return -delay_sum


print(sorted(buses, key=lambda bus: (len(bus['status']), get_total_delay_mins, bus['name']), reverse=True))
