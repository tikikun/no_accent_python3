#!/usr/bin/env python3
"""No longer has any accent
"""

import re


def no_accent_vietnamese(s):
    s = re.sub('[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub('[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub('[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub('[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub('[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub('[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub('[ìíịỉĩ]', 'i', s)
    s = re.sub('[ÌÍỊỈĨ]', 'I', s)
    s = re.sub('[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub('[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub('[ỳýỵỷỹ]', 'y', s)
    s = re.sub('[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub('Đ', 'D', s)
    s = re.sub('đ', 'd', s)
    return s


def create_name_for_link(s):
    raw_name = no_accent_vietnamese(s)
    lower_raw_name = raw_name.lower()
    naked_name = re.sub('[^\w\d\s]+', '', lower_raw_name)
    return '-'.join(naked_name.split())


if __name__ == '__main__':
    print('These lines are for testing purpose')
    print('VIỆT NAM ĐẤT NƯỚC CON NGƯỜI')
    print(no_accent_vietnamese('VIỆT NAM ĐẤT NƯỚC CON NGƯỜI'))
    print(create_name_for_link('VIỆT NAM ĐẤT NƯỚC CON NGƯỜI'))
