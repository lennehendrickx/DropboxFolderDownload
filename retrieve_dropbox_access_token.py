# Include the Dropbox SDK libraries
from dropbox import client, rest, session

# parse commandline arguments
parser = argparse.ArgumentParser(description='Download all files from a dropbox folder.')
parser.add_argument('--app_key', help='App Key (get your app key from the Dropbox developer website)',required=True)
parser.add_argument('--app_secret', help='App Secret (get your app secret from the Dropbox developer website)',required=True)
parser.add_argument('--access_type', help='should be "dropbox" or "app_folder" as configured for your app',required=True)
args = parser.parse_args()

sess = session.DropboxSession(args.app_key, args.app_secret, args.access_type)

request_token = sess.obtain_request_token()

# Make the user sign in and authorize this token
url = sess.build_authorize_url(request_token)
print "url:", url
print "Please authorize in the browser. After you're done, press enter."
raw_input()

# This will fail if the user didn't visit the above URL and hit 'Allow'
access_token = sess.obtain_access_token(request_token)
print "access token key:", access_token.key
print "access token secret:", access_token.secret

client = client.DropboxClient(sess)
print "linked account:", client.account_info()
