FROM python:3.9
EXPOSE 5002

WORKDIR /WTForms

COPY requirements.txt /WTForms
RUN pip install  -r requirements.txt --upgrade pip

COPY . /WTForms

CMD python routes.py
