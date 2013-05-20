#!/usr/bin/env python

# -- coding: utf-8 -- 
# Include the Dropbox SDK libraries
from dropbox import client, rest, session
import os, re, argparse

# parse commandline arguments
parser = argparse.ArgumentParser(description='Download all files from a dropbox folder.')
parser.add_argument('--app_key', help='App Key (get your app key from the Dropbox developer website)',required=True)
parser.add_argument('--app_secret', help='App Secret (get your app secret from the Dropbox developer website)',required=True)
parser.add_argument('--access_token_key', help='Access Token Key (get your access token key from retrieve_dropbox_access_token.py)',required=True)
parser.add_argument('--access_token_secret', help='Access Token Secret (get your access token secret from retrieve_dropbox_access_token.py)',required=True)
parser.add_argument('--access_type', help='should be "dropbox" or "app_folder" as configured for your app',required=True)
parser.add_argument('-s', '--dropbox_dir', help='Folder you want to download from Dropbox', default='/',  required=False)
parser.add_argument('-d','--dest_dir',help='Folder where you want to download to (default: script_dir/download)', default=os.path.dirname(os.path.abspath(__file__)) + '/download' , required=False)
parser.add_argument('-r', '--remove_downloaded_files', help='Remove files downloaded from dropbox remotely' action='store_true')
args = parser.parse_args()

# functions
def assure_path_exists(path):
    if not os.path.exists(path):
    	print "Creating directory:", path 
        os.makedirs(path)
        
        
def lreplace(pattern, sub, string):
    return re.sub('^%s' % pattern, sub, string)

# make connection to dropbox
print "Connecting to dropbox..."
sess = session.DropboxSession(args.app_key, args.app_secret, args.access_type)
sess.set_token(args.access_token_key, args.access_token_secret)
client = client.DropboxClient(sess)

# get list of files for args.dropbox_dir
print "Fetching list of files in:", args.dropbox_dir
metadata = client.metadata(args.dropbox_dir)
def files_only(metadata): return metadata['is_dir'] == False
files = map(lambda metadata: metadata['path'], filter(files_only, metadata['contents']))

# download files to args.dest_dir
assure_path_exists(args.dest_dir)
for file in files:
    dest_file = args.dest_dir + lreplace(args.dropbox_dir, '', file)
    print "Downloading file: %s to: %s" % (file, dest_file)
    out = open(dest_file, 'wb')
    out.write(client.get_file(file).read())
    
# remove files in args.dropbox_dir
if args.remove_downloaded_files == True:
    for file in files:
        print "Removing file: %s from dropbox" % (file)
        client.file_delete(file)
