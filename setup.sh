echo "First install Python 3 from https://www.python.org/downloads/"

pip install virtualenv
virtualenv -p python3 ./env --no-site-packages
source env/bin/activate
pip install numpy
pip install scipy
pip install -r requirements.txt

echo "Then setup the config!"
