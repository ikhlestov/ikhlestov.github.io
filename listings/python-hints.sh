# ==========================================
# serve current folder to web
# python2
python -m SimpleHTTPServer
# python3
python3 -m http.server

# ==========================================
# create new virualenv
virtualenv -p /usr/local/bin/python2.7 env_name
# create new vierualenv with venv without pip
python3.6 -m venv $ENV_NAME --without-pip
source $ENV_NAME/bin/activate
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
# or with pip just
python3.6 -m venv $ENV_NAME

# ==========================================
# unistall all existing packages
pip freeze | xargs pip uninstall -y

# ==========================================
# check for PEP8 errors
pep8 --first --show-source --show-pep8 
