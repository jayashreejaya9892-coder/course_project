FROM python:3.12-slim

WORKDIR /app

COPY library.py .

CMD ["python", "library.py"]
