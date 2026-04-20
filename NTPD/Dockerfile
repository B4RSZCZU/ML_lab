# Oparty był na oficjalnym obrazie z Pythonem (np. python:3.9-slim);
FROM python:3.9-slim

# Kopiował pliki aplikacji i plik requirements.txt do kontenera;
WORKDIR /app
COPY requirements.txt .
COPY main.py .

# Instalował niezbędne zależności Pythona;
RUN pip install --no-cache-dir -r requirements.txt

# Uruchamiał serwer;
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]