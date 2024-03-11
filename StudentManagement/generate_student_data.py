import random
from datetime import datetime, timedelta

last_name = ['Zhang', 'Li', 'Wang', 'Zheng', 'Ma', 'Sun', 'Song', 'Shi', 'Ren', 'Zhou', 'Qian', 'Feng', 'Chen']
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'ea', 'ay', 'ai', 'ei', 'ou', 'au', 'ao', 'eo', 'eu', 'ey', 'oy']
cons = ['r', 'w', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'sh', 'ch', 'ng',
        'ts', 'st', 'ph']


def generate_name():
    name = random.choice(last_name)
    for _ in range(1, random.choice([2, 3])):
        name += ' '
        first = random.choice(cons)
        name += first[0].upper() + first[1:]
        name += random.choice(vowels) + random.choice(cons)
    return name


def generate_all_students(n=50000):
    return set(generate_name() for _ in range(n))


def random_date(year=2024):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    days_between = (end_date - start_date).days + 1
    random_days = random.randrange(days_between)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime('%Y-%m-%d')
