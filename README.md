# KLOPP'S  LIVERPOOL EPL MATCH PREDICTOR by 🅱🅻🅰🆀



![li](https://user-images.githubusercontent.com/100685852/214846024-51910198-1951-48e6-8b1a-2c0a8056dcd8.jpg) ![liv2](https://user-images.githubusercontent.com/100685852/214846291-f3899b64-f38b-43c2-8f72-fc86ff40eb5a.jpg) ![liv](https://user-images.githubusercontent.com/100685852/214846371-205623ff-b198-4313-9353-d6607a4b140e.png)

## What it is:
This is a classifier that predicts if it is safe to bet on Liverpool football club of England NOT LOSING (win or draw) an English Premier League match under the management of Jurgen Klopp. The dataset upon which this classifier was trained is small, as there have been less than 300 EPL matches for Liverpool since Klopp assumed the managerial position in the 2015/2016 season. Again, there have 
been some tactical and individual alterations in recent times to Jurgen's style that we might have to wait a while to retrieve more data of this new style in order to train a model that is almost foolproof. Nonetheless, this classifier works just fine for now, as is evident in the screenshots below of the model accurately predicting that it would
be safe to bet on Liverpool not losing their EPL match on the 21st of January, 2023, against Chelsea FC.

You can access the dataset used in training this model in the file 'Liverpool.csv' above.

## How to run the model:
The fastest way for you to run this model is to simply get the docker image blaqadonis1993/klopps_liverpool and run it locally.

## Download the image:
```docker pull blaqadonis1993/klopps_liverpool```
## Start the service:
```docker run -it --rm -p 9696:9696 klopps_liverpool:latest```

In the terminal, run:
```python predict_test.py```

If all goes well, you should have results similar to the ones in the screenshots below:
![aa (2)](https://user-images.githubusercontent.com/100685852/214958772-0a8427db-2a22-44f2-ad1e-3ac93797b4de.PNG) 

![chelsea](https://user-images.githubusercontent.com/100685852/214958829-63b8f16f-aec4-40a6-b7cc-7896dc270699.PNG)

For the predict_test.py, enter your own values in match:
```match = {
    "Date": "2023-01-21",
    "Form": "decent",
    "Opposition": "tough",
    "season": "middle",
    "venue": "home",
    "Previous match": "0",
    "uEFa": "active"
}```
Date should be in that format: %YYYY-%MM-%DD
Form: Top means that Liverpool won at least 4 of their last 5 matches, Decent means that they won 3, Poor is less than 3.
Opposition means how much of a challenge the opposing team is. Tough is top 6 on the EPL table, or any of the Big Six anywhere top 9 on the table. Medium is any team placed between 7th and 12th, barring any of the Big Six in 7th, or 8th, or 9th positions.
Poor is any team placed outside top 12 of the table. The Big Six: Manchester City, Chelsea, Arsenal, Manchester United, Tottenham Hotspurs, and Liverpool.
Season: Early means any match that falls between 1st game of the season and the 11th game. Middle is 12-30th game. Late is 31 - 38th.
Venue: Home or Away
Previous Match: 1 is Liverpool won their last game, 0 if they did not win their last game (loss or draw).
Uefa: active if Liverpool still have European engagements at the time the match, which you want to predict its outcome, is about to take place.
