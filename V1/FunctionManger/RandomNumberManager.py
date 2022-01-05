from FunctionManger.DateTimeManager import get_date_time_sec_as_random
import random

def get_random_number_with_datetime():
    return get_random_number(2)+get_date_time_sec_as_random()+get_random_number(2)


def get_random_number(length):
    min=10**(length-1)
    max=(10**length)-1
    return str(random.randint(min,max))