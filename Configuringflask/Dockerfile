FROM python:3.9

EXPOSE 5004

WORKDIR /Configuringflask

COPY requirements.txt /ConfiguringFlask
RUN pip install  -r requirements.txt --upgrade pip

ENV SECRET_KEY=GDtfDCFYjD
ENV SESSION_COOKIE_NAME=my_cookie
ENV PROD_DATABASE_URI=my_prod_db
ENV DEV_DATABASE_URI=my_dev_db

COPY . /Configuringflask

CMD python app.py
