FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY . /app/
USER root
EXPOSE 80
RUN pip install -r /app/requirements.txt
WORKDIR /app/web
CMD ["uvicorn", "web.main:app", "--host", "0.0.0.0", "--port", "80"]
