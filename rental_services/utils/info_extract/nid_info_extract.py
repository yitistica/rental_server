"""
after validation
"""
from typing import Union
import datetime


def _convert_nid_to_str(nid: Union[str, int]):
    return str(nid)


def get_gender_from_nid(nid: Union[str, int]) -> str:
    nid = _convert_nid_to_str(nid)
    gender_digit = nid[16]
    if int(gender_digit) % 2 == 0:
        return 'female'
    else:
        return 'male'


def get_gender_from_nid_cn(nid: Union[str, int]):
    gender_translate_map = {'female': '女', 'male': '男'}
    gender = get_gender_from_nid(nid=nid)
    return gender_translate_map[gender]


def get_dob(nid: Union[str, int]):
    nid = _convert_nid_to_str(nid)
    _date = datetime.date(year=int(nid[6:10]), month=int(nid[10:12]), day=int(nid[12:14]))
    return _date

