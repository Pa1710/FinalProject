FROM python:3.9

EXPOSE 5008

WORKDIR /sqlalchemy

COPY requirements.txt /sqlalchemy
RUN pip install  -r requirements.txt --upgrade pip

COPY . /sqlalchemy

CMD python routes.py
