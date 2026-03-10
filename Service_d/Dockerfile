FROM python:3.13-slim

WORKDIR /app

COPY Service_d/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY shards/ ./shards/

COPY Service_d/ .

CMD ["python", "main.py"]

