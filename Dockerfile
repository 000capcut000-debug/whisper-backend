FROM python:3.10

RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Render uses $PORT variable automatically
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"]
