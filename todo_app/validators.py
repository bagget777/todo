import re
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    if not is_valid_phone_number(value):
        raise ValidationError('Номер телефона недействителен')

def is_valid_phone_number(value):
    pattern = r'^\+996\d{9,15}$'
    return bool(re.match(pattern, value))
