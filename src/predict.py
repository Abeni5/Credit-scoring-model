# predict.py

import joblib
import pandas as pd

def load_model(model_path):
    """Load the trained model from the specified path."""
    model = joblib.load(model_path)
    return model

def make_prediction(model, input_data):
    """Make a prediction using the trained model and input data."""
    prediction = model.predict(input_data)
    return prediction

def main(input_data_path, model_path):
    """Main function to load the model and make predictions."""
    # Load the trained model
    model = load_model(model_path)
    
    # Load input data
    input_data = pd.read_csv(input_data_path)
    
    # Make predictions
    predictions = make_prediction(model, input_data)
    
    # Output predictions
    print(predictions)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Make predictions using a trained model.")
    parser.add_argument("input_data_path", type=str, help="Path to the input data CSV file.")
    parser.add_argument("model_path", type=str, help="Path to the trained model file.")
    
    args = parser.parse_args()
    
    main(args.input_data_path, args.model_path)