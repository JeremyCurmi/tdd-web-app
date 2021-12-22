FROM python:3.7-slim

RUN apt-get update && apt-get install gcc -y && apt-get clean

COPY requirements.txt /app/requirements.txt

WORKDIR app

RUN pip install --user -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY . .

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PYTHONPATH "${PYTHONPATH}:/app/"

EXPOSE 5000

CMD ["python", "main.py"]