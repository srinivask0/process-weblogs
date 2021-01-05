FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/ingestion/src
COPY requirements_ingestion.txt /opt/services/ingestion/src
WORKDIR /opt/services/ingestion/src
RUN pip install -r requirements_ingestion.txt
COPY . /opt/services/ingestion/src
EXPOSE 5672

CMD ["python", "ingestion.py"]
