from datetime import datetime
from Views import Functions as viewFunc
def get_current_date():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def generate_id():
    return datetime.now().strftime("%d%m%Y%H%M%S")

def check_length(inputName,inputValue,minLength,maxLength):
    if len(inputValue) < minLength or len(inputValue) > maxLength:
        viewFunc.error_message(f"La valeur '{inputValue}' du champ '{inputName}' doit avoir une longueur entre {minLength} et {maxLength} caractères.")
        return False
    return True