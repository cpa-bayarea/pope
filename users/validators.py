"""Custom validators for Pope User."""
import re

from django.core.validators import EMPTY_VALUES
from django.core.exceptions import ValidationError


def DV_maker(v):
    if v >= 2:
        return 11 - v
    return 0


def validate_cpf(value):
    """Validates CPF.

    Reference: https://djangosnippets.org/snippets/10601/
    """

    if value in EMPTY_VALUES:
        return u''
    if not value.isdigit():
        value = re.sub("[-\.]", "", value)

    orig_value = value[:]
    try:
        int(value)
    except ValueError:
        raise ValidationError('CPF deve conter apensar dígitos')

    if len(value) is not 11:
        raise ValidationError('O CPF é composto por no máximo 11 dígitos')

    if value == len(value) * value[0]:
        raise ValidationError(
            'Os caracteres do CPF não podem ser todos iguais'
        )

    orig_dv = value[-2:]

    new_1dv = sum(
        [i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))]
    )
    new_1dv = DV_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum(
        [i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))]
    )
    new_2dv = DV_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)

    if value[-2:] != orig_dv:
        raise ValidationError('CPF inválido')

    return orig_value
