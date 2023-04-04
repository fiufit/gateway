FROM python:3.10

WORKDIR /code

COPY ./poetry.lock /code/poetry.lock
COPY ./pyproject.toml /code/pyproject.toml

RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY ./src /code/src

EXPOSE ${PORT}

CMD ["python", "./src/main.py"]
