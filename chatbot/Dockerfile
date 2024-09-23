FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y bash

EXPOSE 8505

CMD ["chainlit", "run", "app.py", "--host", "0.0.0.0", "--port", "8505"]