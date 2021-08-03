FROM python:3.9

EXPOSE 5010

WORKDIR /flask-session-tutorial

COPY requirements.txt /flask-session-tutorial
RUN pip install  -r requirements.txt --upgrade pip

COPY . /flask-session-tutorial

CMD python routes.py