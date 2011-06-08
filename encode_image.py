#!/usr/bin/env python

import os
import Tkinter
import tkFileDialog
import mimetypes
import base64
from itertools import izip_longest

def generate_data_uri(f):
    r'''Generate a data URI from the provided file.'''
    return 'data:{0};base64,{1}'.format(mimetypes.guess_type(f.name)[0],
                                        base64.b64encode(f.read()))

def generate_image_tag(uri, alt='', wrap=False):
    r'''Generate a image tag from provided URI.'''
    uri = '\n          '.join(''.join(s) for s in grouper(wrap, uri, '')) if wrap else uri
    return '<img src="{0}" alt="{1}" />'.format(uri, alt)

def grouper(n, iterable, padvalue=None):
    "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return izip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

def main():
    root = Tkinter.Tk()
    root.withdraw()
    files = tkFileDialog.askopenfilenames(parent=root)
    
    for file_name in files:
        if os.path.exists(file_name):
            bits = os.path.basename(file_name).split('.')
            if bits[0] and len(bits) > 1:
                if bits[-1] in ('jpg', 'jpeg', 'png', 'gif'):
                    html_file = os.path.join(os.path.dirname(file_name),
                                             '.'.join(bits[:-1] + ['html']))
                    if not os.path.exists(html_file):
                        with open(html_file, 'w') as f:
                            f.write(generate_image_tag(
                                generate_data_uri(open(file_name))
                            ))

if __name__ == "__main__":
    main()
