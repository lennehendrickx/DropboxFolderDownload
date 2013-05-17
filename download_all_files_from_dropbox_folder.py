# -- coding: utf-8 -- 
# Include the Dropbox SDK libraries
from dropbox import client, rest, session
import os
import re

# Get your app key and secret from the Dropbox developer website
APP_KEY = '8ua45ds2iq0ofsp'
APP_SECRET = 'za3jfxxsw3y37rr'

# Your app access token (see retrieve_dropbox_access_token.py)
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''

# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = 'dropbox'

# Folder to download
DROPBOX_DIR = "/Camera Uploads"
DEST_DIR = "/test"

# functions
def assure_path_exists(path):
    if not os.path.exists(path):
    	print "Creating directory:", path 
        os.makedirs(path)
        
def lreplace(pattern, sub, string):
    return re.sub('^%s' % pattern, sub, string)

# make connection to dropbox
print "Connecting to dropbox..."
sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
sess.set_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
client = client.DropboxClient(sess)

# get list of files for DROPBOX_DIR
print "Fetching list of files in:", DROPBOX_DIR
metadata = client.metadata(DROPBOX_DIR)
def files_only(metadata): return metadata['is_dir'] == False
files = map(lambda metadata: metadata['path'], filter(files_only, metadata['contents']))

# download files to DEST_DIR
assure_path_exists(DEST_DIR)
for file in files:
    dest_file = DEST_DIR + lreplace(DROPBOX_DIR, '', file)
    print "Downloading file: %s to: %s" % (file, dest_file)
    out = open(dest_file, 'wb')
    out.write(client.get_file(file).read())
    
# remove files in DROPBOX_DIR
