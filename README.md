git clone https://github.com/Chetan-Gudagamanal/url-shortner-backend-with-django-mongodb.git

cd url-shortner-backend-with-django-mongodb/

python3 -m venv <VIRTUAL-ENVIRONMENT-NAME>
source <VIRTUAL-ENVIRONMENT-NAME>/bin/activate

pip install -r requirements.txt

# Create .env file inside urlShortner Dir and update values as in .env.example file
cp .env.example ./urlShortner/.env

python manage.py runserver
