FROM python:3.9-slim

WORKDIR /home

RUN pip install --upgrade pip &&\
    pip install numpy pandas sqlalchemy psycopg2-binary

COPY entities.py /home
COPY functions.py /home
COPY main.py /home

CMD [ "python", "/home/main.py" ]