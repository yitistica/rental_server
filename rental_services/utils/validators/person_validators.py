from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class SoftNIDValidator(RegexValidator):
    """
    soft: not checking the NID belongs to a legit province;
    """
    regex = "^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$"
    message = 'nid is not valid'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def nid_validator(value):
    import re
    regex = "^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$"
    if not re.search(regex, value):
        raise ValidationError('not valid')


