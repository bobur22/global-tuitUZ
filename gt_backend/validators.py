from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validateFullNname(value):
    """Validate Full Name"""
    num = 0
    for char in value.split(' '):
        num+=1

    if num >= 2:
        for i in value.split(' '):
            if i.isdigit():
                raise ValidationError(_("Enter a valid full name.(without numbers)"))
    else:
        raise ValidationError(_("Enter a valid full name that contains first name and last name"))