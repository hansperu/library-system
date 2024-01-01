FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./alembic.ini /code/alembic.ini

COPY ./alembic /code/alembic
COPY ./main.py /code/main.py

COPY ./compose/api/entrypoint /code/entrypoint
RUN sed -i 's/\r$//g' /code/entrypoint
RUN chmod +x /code/entrypoint

COPY ./compose/api/start /code/start
RUN sed -i 's/\r$//g' /code/start
RUN chmod +x /code/start

COPY ./src /code/src

ENTRYPOINT [ "/code/entrypoint" ]

CMD [ "/code/start" ]
