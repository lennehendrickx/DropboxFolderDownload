DropboxFolderDownload
=====================

DropboxFolderDownload lets you do perform an automated download of all files in a given dropbox folder.

Use retrieve_dropbox_access_token.py to retrieve the access token.
This is needed to authenticate without user interaction to dropbox.

<pre>
usage: retrieve_dropbox_access_token.py [-h] --app_key APP_KEY --app_secret
                                        APP_SECRET --access_type ACCESS_TYPE

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
</pre>

Use download_all_files_from_dropbox_folder.py to download any dropbox folder.

<pre>
  usage: download_all_files_from_dropbox_folder.py [-h] --app_key APP_KEY
                                                 --app_secret APP_SECRET
                                                 --access_token_key
                                                 ACCESS_TOKEN_KEY
                                                 --access_token_secret
                                                 ACCESS_TOKEN_SECRET
                                                 --access_type ACCESS_TYPE
                                                 [-s DROPBOX_DIR]
                                                 [-d DEST_DIR] [-r]

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

</pre>
Prerequisites:

* Dropbox Python SDK 
  
  <pre>https://www.dropbox.com/developers/core/sdk</pre>

* Argparse module (standard in 2.7 and up)

  <pre>https://pypi.python.org/pypi/argparse</pre>
