# libAssistant

Library Assistant Microservices \
Administration with MYSQL/Django Rest Framework \
Main with MYSQL/FLASK \
Internal API between Main and Administration using RabbitMQ

# Installation

## Admin API

Run following commands:\
**cd admin\
.\env\Scripts\activate \
docker-compose up --build \
docker-compose exec backend sh \
python manage.py makemigrations \
python manage.py migrate**

## Main API

Run following commands:\
**cd main\
docker-compose up --build\
docker-compose exec backend sh\
python manage.py db migrate\
python manage.py db upgrade**

## Frontend

You should have NodeJS installed (https://nodejs.org/en/)\
Once you have NodeJS installed, install Yarn globally (https://classic.yarnpkg.com/en/docs/install/)\
\
Run following commands:\
**cd frontend\
yarn\
yarn start**
