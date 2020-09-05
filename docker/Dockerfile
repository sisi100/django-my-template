FROM python:3

ENV PATH=$PATH:/root/.local/bin
ENV PYTHONUNBUFFERED 1

ADD requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

RUN mkdir /code
WORKDIR /code
ADD . /code/

CMD python manage.py runserver 0.0.0.0:8000