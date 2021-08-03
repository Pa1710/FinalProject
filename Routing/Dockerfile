FROM python:3.9

EXPOSE 5003

WORKDIR /Routing

COPY requirements.txt /Routing
RUN pip install  -r requirements.txt --upgrade pip

COPY . /Routing

CMD python app.py
