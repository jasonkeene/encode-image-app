#!/usr/bin/env python

import os
import Tkinter
import tkFileDialog
import tkMessageBox
import mimetypes
import base64
from itertools import izip_longest

IMAGE_FILE_EXT = ('jpg', 'jpeg', 'png', 'gif')
INSTRUCTION_MESSAGE = """Select one or more images to encode and click Open.

The generated HTML file will be placed in the same directory as the image \
with the same name as the image."""

def generate_data_uri(f):
    r'''Generate a data URI from the provided file.'''
    return 'data:{0};base64,{1}'.format(mimetypes.guess_type(f.name)[0],
                                        base64.b64encode(f.read()))

def generate_image_tag(uri, alt='', wrap=None):
    r'''Generate a image tag from provided URI.'''
    if wrap:
        uri = '\n          '.join(''.join(s) for s in grouper(wrap, uri, ''))
    return '<img src="{0}" alt="{1}" />'.format(uri, alt)

def grouper(n, iterable, padvalue=None):
    "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return izip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

def main():
    root = Tkinter.Tk()
    root.withdraw()
    tkMessageBox.showinfo(message=INSTRUCTION_MESSAGE)
    files = tkFileDialog.askopenfilenames(parent=root)
    
    for file_name in files:
        if os.path.exists(file_name):
            bits = os.path.basename(file_name).split('.')
            if bits[0] and len(bits) > 1:
                if bits[-1] in IMAGE_FILE_EXT:
                    html_file = os.path.join(os.path.dirname(file_name),
                                             '.'.join(bits[:-1] + ['html']))
                    if not os.path.exists(html_file):
                        with open(html_file, 'w') as f:
                            f.write(generate_image_tag(
                                generate_data_uri(open(file_name)),
                                wrap=66 # hard wrap at a sensible length
                            ))

if __name__ == "__main__":
    main()
