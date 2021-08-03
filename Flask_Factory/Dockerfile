FROM python:3.9

EXPOSE 5005

WORKDIR /Flask_Factory

COPY requirements.txt /Flask_Factory
RUN pip install  -r requirements.txt --upgrade pip

COPY . /Flask_Factory

CMD python app.py
