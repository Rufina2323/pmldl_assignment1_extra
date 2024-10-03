FROM python:3.12.6

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY app.py .

CMD streamlit run app.py
