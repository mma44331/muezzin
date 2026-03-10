FROM python:3.13-slim

WORKDIR /app

COPY Service_e/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY shards/ ./shards/

COPY Service_e/ .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

