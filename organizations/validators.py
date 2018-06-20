"""Custom validators for pope Organizations """
import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError


def DV_maker(v):
    if v >= 2:
        return 11 - v
    return 0


def validate_CNPJ(value):
    """Validates CNPJ.
    Reference: https://djangosnippets.org/snippets/10601/
    """

    value = str(value)
    if value in EMPTY_VALUES:
        return u''
    if not value.isdigit():
        value = re.sub("[-/\.]", "", value)
        orig_value = value[:]
    try:
        int(value)
    except ValueError:
        raise ValidationError('CNPJ deve conter apenas dígitos')
    if len(value) > 14:
        raise ValidationError('CNPJ Invalido')
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(list(
        range(5, 1, -1)) + list(range(9, 1, -1)))])
    new_1dv = DV_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(list(
        range(6, 1, -1)) + list(range(9, 1, -1)))])
    new_2dv = DV_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        raise ValidationError('CNPJ inválido')

    return orig_value
