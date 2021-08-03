FROM python:3.9

EXPOSE 5009

WORKDIR /flask-login-tutorial

COPY requirements.txt /flask-login-tutorial
RUN pip install  -r requirements.txt --upgrade pip

COPY . /flask-login-tutorial

CMD python routes.py