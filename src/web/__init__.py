# -*- coding: utf-8 -*-
from random import choice

from faker.providers import BaseProvider

from .mimetypes import mime_types


class WebProvider(BaseProvider):
    """
    Web-related data provider.
    """
    def mime_type(self):
        """
        Returns a mime-type.

        >>> mime_type()

        :return:
        """
        return choice(list(mime_types.keys()))
