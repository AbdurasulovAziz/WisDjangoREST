import datetime

from django.core.exceptions import ValidationError


def check_correct_datetime(value):
    if value < datetime.datetime.now():
        raise ValidationError(
            'Нельзя указывать прошлое время'
        )
