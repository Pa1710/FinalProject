FROM python:3.9

EXPOSE 5003

WORKDIR /Routing_Flask

COPY requirements.txt /Routing_Flask
RUN pip install  -r requirements.txt --upgrade pip

COPY . /Routing_Flask

CMD python app.py