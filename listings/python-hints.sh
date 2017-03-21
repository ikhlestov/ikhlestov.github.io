# ==========================================
# serve current folder to web
# python2
$ python -m SimpleHTTPServer
# python3
$ python3 -m http.server

# ==========================================
# create new virualenv
$ virtualenv -p /usr/local/bin/python2.7 env_name

# ==========================================
# unistall all existing packages
$ pip freeze | xargs pip uninstall -y

# ==========================================
# check for PEP8 errors
$ pep8 --first --show-source --show-pep8 
