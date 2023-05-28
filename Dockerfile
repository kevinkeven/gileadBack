FROM python:3.11.3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /gilead

WORKDIR /gilead

RUN pip install --upgrade pip

RUN pip install -r requirements.txt