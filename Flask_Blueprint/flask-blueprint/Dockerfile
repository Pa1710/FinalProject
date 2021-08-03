FROM python:3.9

EXPOSE 5006

WORKDIR /flask-blueprint

COPY requirements.txt /flask-blueprint
RUN pip install  -r requirements.txt --upgrade pip

COPY . /flask-blueprint

CMD python app.py
