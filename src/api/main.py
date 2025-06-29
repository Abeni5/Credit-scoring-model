from fastapi import FastAPI
from src.api.pydantic_models import YourModel  # Import your Pydantic models here
from src.predict import predict_function  # Import your prediction function here

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Credit Risk Model API"}

@app.post("/predict/")
def predict(data: YourModel):
    prediction = predict_function(data)  # Call your prediction function with the input data
    return {"prediction": prediction}