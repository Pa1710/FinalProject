FROM python:3.9

EXPOSE 5010

WORKDIR /flask-session

COPY requirements.txt /flask-session
RUN pip install  -r requirements.txt --upgrade pip

COPY . /flask-session

CMD python routes.py
