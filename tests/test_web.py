# -*- coding: utf-8 -*-
import re

from src.web import WebProvider  # noqa


def test_mime_type(fake):
    assert re.match(r'\w+/\w([.+-]\w+)*', fake.mime_type())
    assert re.match(r'\w+/\w([.+-]\w+)*', fake.mime_type_popular())


def test_server_token(fake):
    servers = ['Apache', 'Microsoft-IIS', 'nginx', 'Varnish']
    token = fake.server_token()
    assert any(server in token for server in servers)


def test_server_token_solo(fake):
    token = fake.apache()
    assert any(os in token for os in WebProvider.apache_distro)
    assert fake.apache().startswith('Apache/')
    assert fake.iis().startswith('Microsoft-IIS/')
    assert fake.nginx().startswith('nginx')
    assert fake.varnish().startswith('Varnish')
