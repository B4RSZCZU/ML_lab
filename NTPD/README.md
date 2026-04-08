# Titanic Survival Prediction API
## Opis
Aplikacja typu REST API zbudowana w FastAPI, która wykorzystuje model Logistic Regression do przewidywania szansy przeżycia pasażera Titanica na podstawie ich danych.

## Instrukcja uruchomienia
**Pamiętaj, aby uuruchamiać w odpowiednim katalogu!**

### Lokalnie
Jeśli chcesz uruchomić aplikację bezpośrednio:
1. Stwórz środowisko wirtualne: `python -m venv venv`
2. Aktywuj: `.\venv\Scripts\activate`
3. Zainstaluj biblioteki: `pip install -r requirements.txt`
4. Uruchom serwer: `python -m uvicorn main:app --reload`
Aplikacja będzie dostępna pod adresem: `http://127.0.0.1:8000`

### Docker
Aby zbudować i uruchomić aplikację w kontenerze:
1. Zbuduj obraz: `docker build -t titanic-api .`
2. Uruchom kontener: `docker run -d -p 8000:8000 --name titanic-container titanic-api`

### Docker Compose
Aby uruchomić aplikację wraz z dodatkowymi usługami:
1. Uruchom komendę: `docker-compose up -d`
To automatycznie zbuduje obrazy, stworzy sieć `titanic-net` i wystawi porty.

---

## Konfiguracja i Zasoby

### Parametry i zmienne
* **Port aplikacji:** Domyślnie `8000`. Można go zmienić w pliku `docker-compose.yml` w sekcji `ports`.
* **Host:** Wewnątrz kontenera aplikacja nasłuchuje na `0.0.0.0`
* **Zmienne środowiskowe:** Parametry modelu `C` oraz `max_iter` są zdefiniowane w `main.py`.
* **Input Schema:** 
- `Pclass` (int): Klasa biletu (1, 2 lub 3)
- `Sex` (int): Płeć (0 = mężczyzna, 1 = kobieta)
- `Age`	(float): Wiek pasażera
- `SibSp` (int): Liczba rodzeństwa / małżonków na pokładzie
- `Parch` (int): Liczba rodziców / dzieci na pokładzie
- `Fare` (float): Opłata za bilet

**Przykładowy JSON:**
```json
{
  "Pclass": 3,
  "Sex": 0,
  "Age": 22.0,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25
}
```

### Wymagane zasoby
* **RAM:** Minimum 512 MB.
* **CPU:** 1 rdzeń

---

## Testowanie
Po uruchomieniu możesz przetestować predykcję za pomocą komendy cURL:
```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"Pclass\": 3, \"Sex\": 0, \"Age\": 22.0, \"SibSp\": 0, \"Parch\": 0, \"Fare\": 7.25}"
```