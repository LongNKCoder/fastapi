FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY ./app /source/app
COPY requirements.txt /source
EXPOSE 80
RUN pip install -r /source/requirements.txt
WORKDIR /source
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
