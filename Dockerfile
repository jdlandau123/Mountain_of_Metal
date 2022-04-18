FROM python:3

WORKDIR /mountain-of-metal-container

ADD . /mountain-of-metal-container

#RUN set -xe \
#    && apt-get update -y \
#    && apt-get install -y python3 \
#    && apt-get install -y python3-pip

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]

# CMD [ "python3", "manage.py", "runserver", "127.0.0.1:8000" ]

# CMD [ "python3", "manage.py", "runserver", "localhost:8000" ]