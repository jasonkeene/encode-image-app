Introduction
============

A simple app to encode image files as `data URIs`_.

.. _data URIs: http://en.wikipedia.org/wiki/Data_URI_scheme

Supported File Types
====================

* png
* jpeg
* gif

Instructions
============

OSX
---

1. Double click on EncodeImage.app
2. Select one or more images to encode and click Open.
3. The generated HTML file will be placed in the same directory as the
   image with the same name as the image.

Other Platforms
---------------

1. Run encode_image.py with your favorite python interpreter!
2. Select one or more images to encode and click Open.
3. The generated HTML file will be placed in the same directory as the
   image with the same name as the image.

Troubleshooting
===============

If nothing happens when you run EncodeImage.app ensure you have the execute
permission bit set.

::

    chmod 755 EncodeImage.app/Contents/MacOS/EncodeImage # OSX
    chmod 755 encode_image.py # Other Platforms
