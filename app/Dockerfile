FROM python:3.9-slim

WORKDIR /app

RUN mkdir -p /app/data

COPY app/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY app/app.py /app/

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]