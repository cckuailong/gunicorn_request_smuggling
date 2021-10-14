FROM python:3.6
WORKDIR /app
RUN pip install gunicorn==20.0.4 Flask==1.1.2 eventlet==0.30.2
COPY app.py ./
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "-k", "eventlet"]
