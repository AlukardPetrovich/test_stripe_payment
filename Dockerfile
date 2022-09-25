FROM python:3.7-slim
COPY ./ /app
RUN pip install -r /app/requirements.txt
WORKDIR /app/test_rishat/
CMD ["gunicorn", "test_rishat.wsgi:application", "--bind", "0:8000" ] 
