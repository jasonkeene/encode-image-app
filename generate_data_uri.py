#!/usr/bin/env python
# encoding: utf-8

# For data URI standard see: http://www.ietf.org/rfc/rfc2397.txt

from __future__ import print_function
import sys
import os
import getopt
import mimetypes
import base64
import urllib

def generate_base64_data_uri(f):
    r'''Generate a base64 encoded data URI from the provided file.'''
    return 'data:{0};base64,{1}'.format(mimetypes.guess_type(f.name)[0],
                                        base64.b64encode(f.read()))

def generate_text_data_uri(f):
    r'''Generate a URL encoded data URI from the provided text file.'''
    return 'data:text/plain,{0}'.format(urllib.quote(f.read(), safe=''))

generate_data_uri = generate_base64_data_uri

USAGE_MESSAGE = r'''generate_data_uri.py [-t|--text] [files]

options:
    -t, --text
            Encode files as text using URL encoding insteed of base64.
'''

class Usage(Exception):
    def __init__(self, msg=None):
        self.msg = 'usage: {0}'.format(USAGE_MESSAGE)
        if msg is not None:
            self.msg = '{0}\n\n{1}'.format(msg, self.msg)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ht", ["help", "text"])
        except getopt.error, msg:
            raise Usage(msg)
        
        # option processing
        for option, value in opts:
            if option in ("-h", "--help"):
                raise Usage()
            if option in ("-t", "--text"):
                global generate_data_uri
                generate_data_uri = generate_text_data_uri
        
        # argument processing
        if not args:
            raise Usage("no files provided")
    
    except Usage, err:
        print(err.msg, file=sys.stderr)
        print("\tfor help use --help", file=sys.stderr)
        return 2
    
    for file_name in args:
        if os.path.exists(file_name):
            print(generate_data_uri(open(file_name)))
        else:
            print("{0}: Unable to locate file {1}".format(
                    sys.argv[0].split("/")[-1],
                    file_name
                ), file=sys.stderr)

if __name__ == "__main__":
    sys.exit(main())
