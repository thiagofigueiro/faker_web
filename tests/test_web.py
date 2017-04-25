# -*- coding: utf-8 -*-
import re


def test_mime_type(fake):
    assert re.match(r'\w+/\w([.+-]\w+)*', fake.mime_type())
