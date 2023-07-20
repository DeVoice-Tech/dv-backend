# DeVoice - Backend
## Development environment setup

```
# install redis-server
sudo apt install redis-server

# run redis-server
redis-server

# test redis-server
redis-cli ping # you should get PONG

# clone the repo
git clone https://github.com/sakhawy/dv-backend
cd dv-backend

# setup virtual environment
python -m venv venv

# activate virtual environment
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# setup database
python manage.py migrate

# run server
python manage.py runserver
```