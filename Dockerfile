FROM python:3-slim
ADD . /owasp
WORKDIR /owasp
RUN pip install -r requirements.txt