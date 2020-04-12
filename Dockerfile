FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /dollarvote
WORKDIR /dollarvote
COPY requirements.txt /dollarvote/
RUN pip install -r requirements.txt
COPY . /dollarvote/
EXPOSE 8080
