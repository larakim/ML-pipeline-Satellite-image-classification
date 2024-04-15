# FROM python:3.8-slim

# WORKDIR /app

# COPY . .

# RUN pip install -r requirements.txt
# EXPOSE 8501
# ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

# CMD ["python3", "app.py"]
CMD ["streamlit", "run", "app.py"]