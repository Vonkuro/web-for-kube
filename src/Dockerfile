FROM python:3.11-alpine

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code/src


CMD ["fastapi", "run", "src/main.py"]