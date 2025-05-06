FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy both the app folder and the model file
COPY app/ ./app
COPY app/model.pkl ./app/model.pkl

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

