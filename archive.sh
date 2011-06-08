#!/bin/sh

SOURCE_NAME=EncodeImage.app
ARCHIVE_NAME=$SOURCE_NAME.zip

if [ -f $ARCHIVE_NAME ]; then rm $ARCHIVE_NAME ; fi
zip -r $ARCHIVE_NAME $SOURCE_NAME
