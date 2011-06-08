#!/usr/bin/python

from __future__ import with_statement
import os
import Tkinter
import tkFileDialog
import tkMessageBox
import tkSimpleDialog
import mimetypes
import base64
import urllib2
from itertools import izip_longest

WRAP = 66 # hard wrap at a sensible length
IMAGE_FILE_EXT = ('jpg', 'jpeg', 'png', 'gif')

INSTRUCTION_MESSAGE = """Select one or more images to encode and click Open.

The generated HTML file will be placed in the same directory as the image \
with the same name as the image."""
SOURCE_QUESTION = """Do you want to encode an image that is on 
your local filesystem or via a remote URL?"""
URL_QUESTION = """Please provide a URL to the image you wish to encode."""

def generate_data_uri(f, mime_type=None):
    r'''Generate a data URI from the provided file.'''
    if not mime_type and f.name:
        mime_type = mimetypes.guess_type(f.name)[0]
    return 'data:{0};base64,{1}'.format(mime_type, base64.b64encode(f.read()))

def generate_image_tag(uri, alt='', wrap=None):
    r'''Generate a image tag from provided URI.'''
    if wrap:
        uri = '\n          '.join(''.join(s) for s in grouper(wrap, uri, ''))
    return '<img src="{0}" alt="{1}" />'.format(uri, alt)

def grouper(n, iterable, padvalue=None):
    "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return izip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

class ChoiceDialog(tkSimpleDialog.Dialog):
    def __init__(self, prompt, choices=('Yes', 'No'), title="Please choose:",
                 parent=None):
        
        if not parent:
            parent = Tkinter._default_root
        
        self.prompt = prompt
        self.choices = choices
        
        tkSimpleDialog.Dialog.__init__(self, parent, title)
    
    def body(self, master):
        Tkinter.Label(master, text=self.prompt).pack()
    
    def buttonbox(self):
        box = Tkinter.Frame(self)
        
        for choice in self.choices:
            def cmd(event=None, choice=choice):
                self.button_click(event, choice)
            b = Tkinter.Button(box, text=choice, command=cmd)
            b.pack(side=Tkinter.LEFT, padx=5, pady=5)
        
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        
        box.pack()
    
    def button_click(self, event=None, choice=None):
        self.result = choice
        
        self.withdraw()
        self.update_idletasks()
        self.cancel()

def askchoice(prompt, *args, **kwargs):
    c = ChoiceDialog(prompt, *args, **kwargs)
    return c.result

def main():
    root = Tkinter.Tk()
    root.withdraw()
    
    source = askchoice(SOURCE_QUESTION, choices=('Local', 'Remote'))
    
    if source is 'Local':
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
                            with open(html_file, 'w') as html_f:
                                with open(file_name, 'r') as f:
                                    html_f.write(generate_image_tag(
                                        generate_data_uri(f),
                                        wrap=WRAP
                                    ))
    elif source is 'Remote':
        urlstring = tkSimpleDialog.askstring('Open a URL', URL_QUESTION)
        
        try:
            f = urllib2.urlopen(urlstring)
            data_uri = generate_data_uri(f, mime_type=f.info().get('Content-Type', None))
            f.close()
        except (urllib2.URLError, urllib2.HTTPError):
            pass
        if data_uri:
            with tkFileDialog.asksaveasfile(mode='w', defaultextension='html') as html_f:
                html_f.write(generate_image_tag(
                    data_uri,
                    wrap=WRAP
                ))

if __name__ == "__main__":
    main()
