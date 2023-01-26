import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer

from flask import Flask, request, jsonify

with open("model.bin", "rb") as file:
    model = pickle.load(file)

dv = DictVectorizer(sparse=False)

def predict_match(df, dv, model):
    data = pd.DataFrame(df,index=range(0,len(df)))
    data= data.applymap(lambda s:s.lower().replace(' ', '_') if type(s) == str else s)
    data.columns = [x.lower().replace(' ', '_') for x in data.columns]
    data.columns = [x.lower().replace(':', '') for x in data.columns]
    data.columns = [x.lower().replace('*', '') for x in data.columns]
    data.columns = [x.lower().replace('.', '') for x in data.columns]

    data['date'] = pd.to_datetime(data['date'])
    data['day'] = data['date'].dt.day
    data['month'] = data['date'].dt.month
    data['year'] = data['date'].dt.year
    data = data.drop('date', axis=1)

    data['ground'] = data['venue'].replace(['home'], 1)
    data['ground'] = data['ground'].replace(['away'], 0)

    data['foreign_league'] = data['uefa'].replace(['active'], 1)
    data['foreign_league'] = data['foreign_league'].replace(['inactive'], 0)

    data['time'] = data['season'].replace(['early'], 0)
    data['time'] = data['time'].replace(['middle'], 1)
    data['time'] = data['time'].replace(['late'], 2)

    data['difficulty'] = data['opposition'].replace(['tough'], 2)
    data['difficulty'] = data['difficulty'].replace(['medium'], 1)
    data['difficulty'] = data['difficulty'].replace(['easy'], 0)

    data['current_form'] = data['form'].replace(['top'], 2)
    data['current_form'] = data['current_form'].replace(['decent'], 1)
    data['current_form'] = data['current_form'].replace(['poor'], 0)

    data = data.drop(['venue','uefa','season','year','opposition','form'],axis=1)
    Dict_Test = data.to_dict(orient='records')
    X = dv.fit_transform(Dict_Test)
    pred = model.predict_proba(X)[:, 1]


    
    return pred[0]


app = Flask("Klopp's Liverpool")


@app.route('/predict', methods=['POST'])
def predict():
    match = request.get_json()

    pred = predict_match(match, dv, model)
 
    answer = round(pred,2)
#round(float(pred[0]),3) * 100
    if answer > 0.468:
        result = {
            'Prediction': 'Safe to bet on Liverpool FC',
            'Odds': answer 
        }
        print(result)
    else:
        result = {
            'Prediction': 'Not safe to bet on Liverpool FC',
            'Odds': answer
        }
        print(result)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)