import pandas as pd
import pickle
from sklearn.feature_extraction import DictVectorizer

with open('model.bin', 'rb') as file:
    nb = pickle.load(file)

dv = DictVectorizer(sparse=False)
data = {
    "Date": '2022-11-12',
    "Form": "decEnt",
    "Opposition": "poor",
    "season": "middle",
    "venue": "home",
    "Previous match": '1',
    "uEFa": "active"
}

data = pd.DataFrame(data,index=range(0,1))
data.columns = [x.lower() for x in data.columns]

data['date'] = pd.to_datetime(data['date'])
data['day'] = data['date'].dt.day
data['month'] = data['date'].dt.month
data['year'] = data['date'].dt.year
data = data.drop('date', axis=1)

data= data.applymap(lambda s:s.lower().replace(' ', '_') if type(s) == str else s)
data.columns = [x.lower().replace(' ', '_') for x in data.columns]
data.columns = [x.lower().replace(':', '') for x in data.columns]
data.columns = [x.lower().replace('*', '') for x in data.columns]
data.columns = [x.lower().replace('.', '') for x in data.columns]



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

data = data.drop(['venue','uefa','year','season','opposition','form'],axis=1)
data_dict = data.to_dict(orient='records')
X = dv.fit_transform(data_dict)
pred = nb.predict_proba(X)[:, 1]
answer = round(pred[0],2)
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

