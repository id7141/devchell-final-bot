FROM python:3
RUN ls -liha
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 80
CMD ["python", "server-manager.py"]
