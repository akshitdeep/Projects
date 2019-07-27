import tweepy
from textblob import TextBlob  # text/tweet parse
from tweepy import OAuthHandler
import re
from tkinter import *
import tkinter as tk
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


obj=Tk()
obj.geometry("500x500")
obj.title('Graphical Representation of Sentiment Analysis')

photo =tk.PhotoImage(file="twitter_PNG28.png")
pic = tk.Label(obj, image=photo).pack(side="top")


l1=Label(text='Name of the Twitter User ', fg = "black", font = "Helvetica 12 bold")
l1.pack()

e1=Entry()
e1.pack()

l2=Label(text='Number of tweets ', fg = "black", font = "Helvetica 12 bold")
l2.pack()

e2=Entry()
e2.pack()


api_key = "TL7RyLnfilYH6xaoAlS0XFDCg"
api_secret_key = "u5uBn4P62PMIxT4uwUVTl1Ycx4rsfByFs6jl2e4SQ9zDjPIzCO"

access_token = "919434545924935681-2woCDEXuXQdhJewDaCRBqHBYmi5SFDN"
access_token_secret = "T29jqUm6rZqsRYO7AGc47GlgYTaAaN5OtJD0DATo1uBjh"

auth = OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print('login is success')


def get_sentiment(tweet):

    analysis = TextBlob(tweet)

    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


def clean_data(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())


def fetch_data(leader, c=5):
    res = api.search(q=leader, count=c)

    out = []

    for r in res:
        t = clean_data(r.text)
        print(t)
        sent = get_sentiment(t)
        out.append(sent)

    return out


def get_name():
    name = e1.get()
    count = e2.get()

    out = fetch_data(name,count)
    print(name, '-----------------------')
    print(out)
    print(len(out))
    pc=0
    nc=0
    nn=0
    for i in out:
        if i == 'positive':
            pc+= 1
        elif i == 'negative':
            nc+= 1
        else:
            nn+= 1
    print('pc :',pc,'nc :',nc,'nn :',nn)
    pc=(pc/len(out))*100
    nc = (nc / len(out)) * 100
    nn=(nn/len(out))*100
    print('Postive tweets :', pc,'%','negative tweets',nc,'%', 'neutral tweets',nn,'%')

    lpc=[pc]
    lnc=[nc]
    lnn=[nn]
    df = pd.DataFrame(data={'positive':lpc,'negative':lnc,'neutral':lnn})
    df.plot(kind='bar')
    plt.xlabel('Sentiment')
    plt.ylabel('Percentage')
    plt.title('Sentiment Analysis')
    plt.show()

b1=Button(text='Search', font = "Helvetica 10 bold", command=get_name)
b1.pack()

b2=Button(text='Quit', font = "Helvetica 10 bold", command=quit)
b2.pack()
#obj.configure(background='black')


obj.mainloop()





