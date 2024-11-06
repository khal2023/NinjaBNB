# FROM python:3.11

# RUN pip install pipenv

# COPY . /app

# WORKDIR /app

# RUN pipenv install --system --deploy

# CMD ["python", "app.py"]

FROM python:3.11

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]