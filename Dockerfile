FROM python:3

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /code

COPY src/ .

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]