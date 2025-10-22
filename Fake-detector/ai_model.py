import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

def train_model():
    df = pd.read_csv("dataset/messages.csv")  # columns: ['label', 'message']
    df['label'] = df['label'].map({'ham':0, 'spam':1})
    
    X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2)
    
    vectorizer = CountVectorizer()
    X_train_cv = vectorizer.fit_transform(X_train)
    
    model = MultinomialNB()
    model.fit(X_train_cv, y_train)
    
    # Save model + vectorizer
    pickle.dump(model, open('model.pkl', 'wb'))
    pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))

def predict_message(message):
    model = pickle.load(open('model.pkl', 'rb'))
    vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
    
    message_cv = vectorizer.transform([message])
    prediction = model.predict(message_cv)[0]
    
    return "Spam (AI Model)" if prediction == 1 else "Genuine (AI Model)"
