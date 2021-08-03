FROM python:3.9

EXPOSE 5007

WORKDIR /assets

COPY requirements.txt /assets
RUN pip install  -r requirements.txt --upgrade pip

COPY . /assets

CMD python app.py
