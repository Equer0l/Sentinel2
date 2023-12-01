FROM python:3.11.6
WORKDIR /BackendDevOps
COPY . /BackendDevOps
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]