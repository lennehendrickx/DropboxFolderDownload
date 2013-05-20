DropboxFolderDownload
=====================

DropboxFolderDownload lets you do perform an automated download of all files in a given dropbox folder.

Use retrieve_dropbox_access_token.py to retrieve the access token.
This is needed to authenticate without user interaction to dropbox.

Usage: ./retrieve_dropbox_access_token.py

Retrieve dropbox access token

optional arguments:
  -h, --help            show this help message and exit
  --app_key APP_KEY     App Key (get your app key from the Dropbox developer
                        website)
  --app_secret APP_SECRET
                        App Secret (get your app secret from the Dropbox
                        developer website)
  --access_type ACCESS_TYPE
                        should be "dropbox" or "app_folder" as configured for
                        your app


Use download_all_files_from_dropbox_folder.py to download any dropbox folder.

Usage: ./download_all_files_from_dropbox_folder.py

Download all files from a dropbox folder.

optional arguments:
  -h, --help            show this help message and exit
  --app_key APP_KEY     App Key (get your app key from the Dropbox developer
                        website)
  --app_secret APP_SECRET
                        App Secret (get your app secret from the Dropbox
                        developer website)
  --access_token_key ACCESS_TOKEN_KEY
                        Access Token Key (get your access token key from
                        retrieve_dropbox_access_token.py)
  --access_token_secret ACCESS_TOKEN_SECRET
                        Access Token Secret (get your access token secret from
                        retrieve_dropbox_access_token.py)
  --access_type ACCESS_TYPE
                        should be "dropbox" or "app_folder" as configured for
                        your app
  -s DROPBOX_DIR, --dropbox_dir DROPBOX_DIR
                        Folder you want to download from Dropbox
  -d DEST_DIR, --dest_dir DEST_DIR
                        Folder where you want to download to (default:
                        script_dir/download)
  -r, --remove_downloaded_files
                        Remove files downloaded from dropbox remotely


Prerequisites:

Dropbox Python SDK 
https://www.dropbox.com/developers/core/sdk
