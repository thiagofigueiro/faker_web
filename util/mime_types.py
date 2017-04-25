# -*- coding: utf-8 -*-

import requests
import pprint

source_url = 'https://svn.apache.org/repos/asf/httpd/httpd/trunk/docs/conf/' \
             'mime.types'

response = requests.get(source_url, stream=True)
mimetypes = {}
for line in response.iter_lines():
    if line.startswith(b'#'):
        continue
    parts = line.split()
    mimetype = parts.pop(0).decode('utf-8')
    mimetypes[mimetype] = b','.join(parts).decode('utf-8').split(',')


with open('src/web/mimetypes.py', 'w', encoding='utf-8') as fh:
    fh.write('# -*- coding: utf-8 -*-\n')
    fh.write('# mime-types list sourced from {}\n\n\n'.format(source_url))
    fh.write('mime_types = {}\n'.format(pprint.pformat(mimetypes, indent=4)))
