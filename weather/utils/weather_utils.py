degresses = [
    {
        'deg': 0,
        'value': 'East',
        'period': ''
    },
    {
        'deg': 45,
        'value': 'North-East',
        'period': 'East, North-East'
    },
    {
        'deg': 90,
        'value': 'North',
        'period': 'North, North-East'
    },
    {
        'deg': 135,
        'value': 'North-West',
        'period': 'North, North-West'
    },
    {
        'deg': 180,
        'value': 'West',
        'period': 'West, North-West'
    },
    {
        'deg': 225,
        'value': 'South-West',
        'period': 'West, South-West'
    },
    {
        'deg': 270,
        'value': 'South',
        'period': 'South-West, South'
    },
    {
        'deg': 315,
        'value': 'South-East',
        'period': 'South, South-East'
    }
]


def _get_interval(d):
    for deg in degresses:
        if d == deg['deg']:
            return deg['value']
        elif d < deg['deg']:
            return deg['period']
        elif d > 315:
            return 'East, South-East'


def wind_direction(data):
    speed = data['wind']['speed'] if 'speed' in data['wind'] else 'n/a'
    direction = _get_interval(data['wind']['deg']) if 'deg' in data['wind'] else 'n/a'
    wind = {
        'speed': speed,
        'direction': direction
    }
    # direction = _get_interval(data['wind']['deg'])
    # wind['direction'] = direction
    return wind
