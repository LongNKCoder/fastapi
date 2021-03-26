FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY . /app
RUN pip install -r /app/requirements.txt
RUN useradd -ms /bin/bash api
RUN chmod -R 777 /app
RUN chown -R api:api /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]
USER api
