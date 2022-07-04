FROM python:3.8



WORKDIR /code
COPY ./data.json /code/data.json
COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./API.py /code/app/API.py

CMD ["uvicorn", "app.API:app", "--host", "0.0.0.0", "--port", "8000"]