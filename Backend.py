import glob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

def get_date_data():
    names = []
    for name in glob.glob('diary/*.txt'):
        names.append(name)
    return names

def getPosNeg(names):
    analizer = SentimentIntensityAnalyzer()
    pos = []
    neg = []
    for name in names:
        with open(name, 'r') as file:
            entry = file.read()
            score = analizer.polarity_scores(entry)
            print(score)
            pos.append(score['pos'])
            neg.append(score['neg'])

    return pos, neg


def dates_again():
    dates = get_date_data()
    dates_ok = []
    for date in dates:
        dates_ok.append(date[6:-4])
    return dates_ok











