set -o errexit

pip install -r requeriments.txt

python manage.py migrate
