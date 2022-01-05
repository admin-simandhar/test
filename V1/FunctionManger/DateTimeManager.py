from datetime import datetime

def get_date():
    return datetime.now().strftime("%d-%m-%Y")

def get_date_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M")

def get_date_time_sec():    
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def get_date_time_sec_as_random():    
    return datetime.now().strftime("%d%m%Y%H%M%S")

def get_date_time_db():
    return datetime.now()