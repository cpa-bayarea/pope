"""Custom validators for pope Organizations """
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError


def get_digit(multiplier_arr, cnpj):
    count = 0

    for idx, num in enumerate(multiplier_arr):
        count += num * int(list(cnpj)[idx])

    digit = (11 - (count % 11))
    if (count % 11) < 2:
        return 0
    return digit


def validate_CNPJ(value):
    if len(value) != 14:
        raise ValidationError('O CNPJ deve conter 14 dígitos')

    first_digit = get_digit([5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2], value)
    second_digit = get_digit([6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2], value)

    if value[-2:] != '{}{}'.format(first_digit, second_digit):
        raise ValidationError('CNPJ inválido')
    
    return value 