FROM  python:alpine

WORKDIR /app

RUN pip install Faker && pip install requests

COPY *py .

CMD ["python","fake_data_gen.py"]




