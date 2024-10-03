FROM python:3.12.6

WORKDIR /app

RUN adduser --disabled-password user
RUN chown -R user /app
USER user

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY app.py .
COPY ./models/ /app/models
COPY ./schemas ./schemas
COPY ./services ./services

CMD python -m uvicorn app:app --host 0.0.0.0
