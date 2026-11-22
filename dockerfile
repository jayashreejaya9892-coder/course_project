FROM python:3.14

WORKDIR /app

COPY library.py .

CMD ["python", "library.py"]
