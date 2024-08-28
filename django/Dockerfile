FROM python:latest
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["bash","run.sh"]
