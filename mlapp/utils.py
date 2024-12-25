from joblib import load

def load_model():
    model = load('./mlapp/model/sentiment_pipeline.joblib')
    return model