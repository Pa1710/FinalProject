FROM python:3.9

EXPOSE 5001

WORKDIR /Jinga

COPY requirements.txt /Jinga
RUN pip install  -r requirements.txt --upgrade pip

COPY . /Jinga
CMD python routes.py
