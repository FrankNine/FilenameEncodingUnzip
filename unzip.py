#!/usr/bin/env python

# original author: Dave dV (http://unknowngenius.com/blog/)

# Small script to decode zip archives made on different systems while preserving
# filenames in non-English languages (particularly Japanese)

# reusing code from: http://stackoverflow.com/questions/1807063/extract-files-with-invalid-characters-in-filename-with-python

# More info here: http://unknowngenius.com/blog/archives/2011/11/04/recovering-japanese-filenames-from-zip-archives-on-os-x

# Use at your own risk, feel free to improve and redistribute!

import shutil
import zipfile
import os

from sys import argv

def ensure_dir(path):
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

if len(argv) < 2:
    print "\n*** Need a file to unzip ***\n\nUsage: %s filename.zip [optional encoding]\n(if no source encoding is provided, Windows 'sjis' will be assumed by default)" % argv[0]
    quit()

if len(argv) > 2:
    encoding = argv[2]
else:
    encoding = 'sjis'

archive_path = argv[1]
print "Unpacking archive: '%s' using encoding %s" % (archive_path, encoding)
f = zipfile.ZipFile(archive_path, 'r')
archive_dir = os.path.dirname(archive_path)

for fileinfo in f.infolist():
    decoded_relative_path = unicode(fileinfo.filename, encoding)
    # ignore folder
    if decoded_relative_path.endswith(os.sep):
        continue
    
    decoded_path = os.path.join(archive_dir, decoded_relative_path)
    
    print "Extracting: %s" % decoded_relative_path
    ensure_dir(decoded_path)
    outputfile = open(decoded_path, "wb")
    shutil.copyfileobj(f.open(fileinfo.filename), outputfile)
