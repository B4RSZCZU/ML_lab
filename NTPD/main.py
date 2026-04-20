# Importy
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ------------- MODEL ----------------------------------------------------------------
# Zbiór z poprzednich laboratoriów oraz jego czyszczenie
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df_clean = df[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']].copy()
df_clean['Sex'] = df_clean['Sex'].map({'male': 0, 'female': 1})
df_clean['Age'] = df_clean['Age'].fillna(df_clean['Age'].median())
kolumny_do_int8 = ['Survived', 'Pclass', 'Sex', 'SibSp', 'Parch']
df_clean[kolumny_do_int8] = df_clean[kolumny_do_int8].astype('int8')
df_clean['Age'] = df_clean['Age'].astype('float32')
df_clean['Fare'] = df_clean['Fare'].astype('float32')

# Tworzenie zbioru treningowego oraz testowego
X = df_clean.drop('Survived', axis=1)
y = df_clean['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

param_max_iter = 1000
param_C = 0.1

# Tworzenie modelu oraz trening
model = LogisticRegression(C=param_C, max_iter=param_max_iter)
model.fit(X_train, y_train)

# Obliczenie metryki na zbiorze testowym
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

# ----------------APLIKACJA------------------------------------------------------------------
app = FastAPI()

env = os.getenv("ENVIRONMENT", "default")

# Format danych
class PassengerData(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float

# Zad 1
@app.get("/")
def root():
    return {"message": "Hello world!"}

# Zad 4
@app.get("/info")
def get_info():
    return {
        "model_type": "LogisticRegression",
        "features": ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"],
        "target": "Survived",
        "accuracy": round(float(acc), 4,
        "environment": app_env                
    }

# Zad 4
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Zad 2 i 3
@app.post("/predict")
def predict_survival(data: PassengerData):
    try:
        # model_dump() zamiast .dict()
        input_df = pd.DataFrame([data.model_dump()])
        prediction = model.predict(input_df)
        return {
            "prediction": int(prediction[0]),
            "survived": bool(prediction[0])
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Błąd danych: {str(e)}")
