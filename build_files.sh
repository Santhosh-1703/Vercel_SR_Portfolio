set -o errexit

pip install -r requirements.txt

python3.11 manage.py collectstatic
python3.11 manage.py migrate
