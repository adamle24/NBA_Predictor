from sklearn.linear_model import LogisticRegression
from app.model.preprocess import preprocess
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def getModel():
    df = pd.read_csv('csv/game.csv')

    x, y, scaler = preprocess(df)
    
    model = LogisticRegression(random_state=42)

    model.fit(x, y)

    # Save model and scaler (use scalar when predicting)
    joblib.dump(model, "app/model/logreg_model2.pkl")
    joblib.dump(scaler, "app/model/scaler2.pkl")
    return model

if __name__ == "__main__":
    from app.model.get_model import getModel
    getModel()
    print("Model has been trained and saved")