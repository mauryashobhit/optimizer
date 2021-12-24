from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import  CreateUserForm
from django.contrib import messages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from django.http import HttpResponse,HttpRequest
import yfinance as yf
import plotly
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objs as go
from plotly.graph_objs import Line
import streamlit as st
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import requests
import bs4


def index(request):
    return render(request,"index.html")

def optimize(request):
    return render(request,'optimize.html')

def google(request):
    google = yf.download(tickers='GOGL', period='5y', interval='1d')
    google.to_csv("google.csv")
    df=pd.read_csv("google.csv")
    df["Normed_Return"]=df["Adj Close"]/df.iloc[0]["Adj Close"]
    data=[go.Line(x=df["Date"],y=df["Adj Close"])]
    fig = go.Figure(data = data,layout = go.Layout(title='Google adj closing price',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Closing Price')))
    fig=plot(fig,output_type="div")

    data1=[go.Line(x=df["Date"],y=df["Volume"])]
    fig1=go.Figure(data = data1,layout = go.Layout(title='Google Volume',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Volume')))
    fig1=plot(fig1,output_type="div")
    data2=[go.Line(x=df["Date"],y=df["Normed_Return"])]
    fig2 = go.Figure(data = data2,layout = go.Layout(title='Google Return',
                                       xaxis = dict(title = 'Date'), yaxis = dict(title = 'Return')))
    fig2=plot(fig2,output_type="div")
    return render(request,"google.html",context={'fig':fig,'fig1':fig1,'fig2':fig2})

def cisco(request):
    cisco = yf.download(tickers='CSCO', period='5y', interval='1d')
    cisco.to_csv("cisco.csv")
    df=pd.read_csv("cisco.csv")
    df["Normed_Return"]=df["Adj Close"]/df.iloc[0]["Adj Close"]
    data=[go.Line(x=df["Date"],y=df["Adj Close"])]
    fig = go.Figure(data = data,layout = go.Layout(title='Cisco adj closing price',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Closing Price')))
    fig=plot(fig,output_type="div")

    data1=[go.Line(x=df["Date"],y=df["Volume"])]
    fig1=go.Figure(data = data1,layout = go.Layout(title='Cisco Volume',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Volume')))
    fig1=plot(fig1,output_type="div")
    data2=[go.Line(x=df["Date"],y=df["Normed_Return"])]
    fig2 = go.Figure(data = data2,layout = go.Layout(title='Cisco Return',
                                       xaxis = dict(title = 'Date'), yaxis = dict(title = 'Return')))
    fig2=plot(fig2,output_type="div")
    return render(request,"cisco.html",context={'fig':fig,'fig1':fig1,'fig2':fig2})

def facebook(request):
    facebook = yf.download(tickers='FB', period='5y', interval='1d')
    facebook.to_csv("facebook.csv")
    df=pd.read_csv("facebook.csv")
    df["Normed_Return"]=df["Adj Close"]/df.iloc[0]["Adj Close"]
    data=[go.Line(x=df["Date"],y=df["Adj Close"])]
    fig = go.Figure(data = data,layout = go.Layout(title='Facebook adj closing price',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Closing Price')))
    fig=plot(fig,output_type="div")

    data1=[go.Line(x=df["Date"],y=df["Volume"])]
    fig1=go.Figure(data = data1,layout = go.Layout(title='Facebook Volume',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Volume')))
    fig1=plot(fig1,output_type="div")
    data2=[go.Line(x=df["Date"],y=df["Normed_Return"])]
    fig2 = go.Figure(data = data2,layout = go.Layout(title='Facebook Return',
                                       xaxis = dict(title = 'Date'), yaxis = dict(title = 'Return')))
    fig2=plot(fig2,output_type="div")
    return render(request,"facebook.html",context={'fig':fig,'fig1':fig1,'fig2':fig2})


def apple(request):
    apple = yf.download(tickers='AAPL', period='5y', interval='1d')
    apple.to_csv("apple.csv")
    df=pd.read_csv("apple.csv")
    df["Normed_Return"]=df["Adj Close"]/df.iloc[0]["Adj Close"]
    data=[go.Line(x=df["Date"],y=df["Adj Close"])]
    fig = go.Figure(data = data,layout = go.Layout(title='Apple adj closing price',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Closing Price')))
    fig=plot(fig,output_type="div")

    data1=[go.Line(x=df["Date"],y=df["Volume"])]
    fig1=go.Figure(data = data1,layout = go.Layout(title='Apple Volume',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Volume')))
    fig1=plot(fig1,output_type="div")
    data2=[go.Line(x=df["Date"],y=df["Normed_Return"])]
    fig2 = go.Figure(data = data2,layout = go.Layout(title='Apple Return',
                                       xaxis = dict(title = 'Date'), yaxis = dict(title = 'Return')))
    fig2=plot(fig2,output_type="div")
    return render(request,"apple.html",context={'fig':fig,'fig1':fig1,'fig2':fig2})


def forecast_google(request):
    google = yf.download(tickers='GOGL', period='5y', interval='1d')
    google.to_csv("google.csv")
    google=pd.read_csv("google.csv")
    df_train1=google[["Date","Adj Close"]]
    df_train1=df_train1.rename(columns={"Date":"ds","Adj Close":"y"})
    m=Prophet()
    m.fit(df_train1)
    future=m.make_future_dataframe(periods=30)
    forecast=m.predict(future)
    fig1=plot_plotly(m,forecast)
    fig1.update_layout(width=1500,height=500)
    fig1=plot(fig1,output_type="div")
    fig2= go.Figure(data=[go.Table(
    header=dict(values=list(google.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[google.Date,google.High,google.Low, google.Open, google.Close,google["Adj Close"],google.Volume],
               fill_color='lavender',
               align='left'))
               ])
    fig2=plot(fig2,output_type="div")
    return render(request,"google_forecast.html",context={"fig1":fig1,"fig2":fig2})

def forecast_cisco(request):
    cisco = yf.download(tickers='CSCO', period='5y', interval='1d')
    cisco.to_csv("cisco.csv")
    cisco=pd.read_csv("cisco.csv")
    df_train2=cisco[["Date","Adj Close"]]
    df_train2=df_train2.rename(columns={"Date":"ds","Adj Close":"y"})
    m_cisco=Prophet()
    m_cisco.fit(df_train2)
    future_cisco=m_cisco.make_future_dataframe(periods=30)
    forecast_cisco=m_cisco.predict(future_cisco)
    fig1=plot_plotly(m_cisco,forecast_cisco)
    fig1.update_layout(width=1500,height=500)
    fig1=plot(fig1,output_type="div")
    fig2= go.Figure(data=[go.Table(
    header=dict(values=list(cisco.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[cisco.Date,cisco.High,cisco.Low, cisco.Open, cisco.Close, cisco["Adj Close"],cisco.Volume],
               fill_color='lavender',
               align='left'))
               ])
    fig2=plot(fig2,output_type="div")
    return render(request,"cisco_forecast.html",context={"fig1":fig1,"fig2":fig2})

def forecast_facebook(request):
    fb = yf.download(tickers='FB', period='5y', interval='1d')
    fb.to_csv("facebook.csv")
    facebook=pd.read_csv("facebook.csv")
    df_train3=facebook[["Date","Adj Close"]]
    df_train3=df_train3.rename(columns={"Date":"ds","Adj Close":"y"})
    m_facebook=Prophet()
    m_facebook.fit(df_train3)
    future_facebook=m_facebook.make_future_dataframe(periods=30)
    forecast_facebook=m_facebook.predict(future_facebook)
    fig1=plot_plotly(m_facebook,forecast_facebook)
    fig1.update_layout(width=1500,height=500)
    fig1=plot(fig1,output_type="div")
    fig2= go.Figure(data=[go.Table(
    header=dict(values=list(facebook.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[facebook.Date,facebook.High,facebook.Low, facebook.Open, facebook.Close, facebook["Adj Close"],facebook.Volume],
               fill_color='lavender',
               align='left'))
               ])
    fig2=plot(fig2,output_type="div")
    return render(request,"facebook_forecast.html",context={"fig1":fig1,"fig2":fig2})

def forecast_apple(request):
    aapl = yf.download(tickers='AAPL', period='5y', interval='1d')
    aapl.to_csv("apple.csv")
    apple=pd.read_csv("apple.csv")
    df_train4=apple[["Date","Adj Close"]]
    df_train4=df_train4.rename(columns={"Date":"ds","Adj Close":"y"})
    m_apple=Prophet()
    m_apple.fit(df_train4)
    future_apple=m_apple.make_future_dataframe(periods=30)
    forecast_apple=m_apple.predict(future_apple)
    fig1=plot_plotly(m_apple,forecast_apple)
    fig1.update_layout(width=1500,height=500)
    fig1=plot(fig1,output_type="div")
    fig2= go.Figure(data=[go.Table(
    header=dict(values=list(apple.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[apple.Date,apple.High,apple.Low, apple.Open, apple.Close, apple["Adj Close"],apple.Volume],
               fill_color='lavender',
               align='left'))
               ])
    fig2=plot(fig2,output_type="div")
    return render(request,"apple_forecast.html",context={"fig1":fig1,"fig2":fig2})

def user(request):
    return render(request,"user.html")

def user_apple(request):
    apple = yf.download(tickers='AAPL', period='5y', interval='1d')
    apple.to_csv("apple.csv")
    df=pd.read_csv("apple.csv")
    df["Normed_Return"]=df["Adj Close"]/df.iloc[0]["Adj Close"]
    data=[go.Line(x=df["Date"],y=df["Adj Close"])]
    fig = go.Figure(data = data,layout = go.Layout(title='Apple adj closing price',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Closing Price')))
    fig=plot(fig,output_type="div")

    data1=[go.Line(x=df["Date"],y=df["Volume"])]
    fig1=go.Figure(data = data1,layout = go.Layout(title='Apple Volume',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Volume')))
    fig1=plot(fig1,output_type="div")
    data2=[go.Line(x=df["Date"],y=df["Normed_Return"])]
    fig2 = go.Figure(data = data2,layout = go.Layout(title='Apple Return',
                                       xaxis = dict(title = 'Date'), yaxis = dict(title = 'Return')))
    fig2=plot(fig2,output_type="div")
    return render(request,"user_apple.html",context={'fig':fig,'fig1':fig1,'fig2':fig2})

def user_google(request):
    google = yf.download(tickers='GOGL', period='5y', interval='1d')
    google.to_csv("google.csv")
    df=pd.read_csv("google.csv")
    df["Normed_Return"]=df["Adj Close"]/df.iloc[0]["Adj Close"]
    data=[go.Line(x=df["Date"],y=df["Adj Close"])]
    fig = go.Figure(data = data,layout = go.Layout(title='Google adj closing price',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Closing Price')))
    fig=plot(fig,output_type="div")

    data1=[go.Line(x=df["Date"],y=df["Volume"])]
    fig1=go.Figure(data = data1,layout = go.Layout(title='Google Volume',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Volume')))
    fig1=plot(fig1,output_type="div")
    data2=[go.Line(x=df["Date"],y=df["Normed_Return"])]
    fig2 = go.Figure(data = data2,layout = go.Layout(title='Google Return',
                                       xaxis = dict(title = 'Date'), yaxis = dict(title = 'Return')))
    fig2=plot(fig2,output_type="div")
    return render(request,"user_google.html",context={'fig':fig,'fig1':fig1,'fig2':fig2})

def user_facebook(request):
    facebook = yf.download(tickers='FB', period='5y', interval='1d')
    facebook.to_csv("facebook.csv")
    df=pd.read_csv("facebook.csv")
    df["Normed_Return"]=df["Adj Close"]/df.iloc[0]["Adj Close"]
    data=[go.Line(x=df["Date"],y=df["Adj Close"])]
    fig = go.Figure(data = data,layout = go.Layout(title='Facebook adj closing price',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Closing Price')))
    fig=plot(fig,output_type="div")

    data1=[go.Line(x=df["Date"],y=df["Volume"])]
    fig1=go.Figure(data = data1,layout = go.Layout(title='Facebook Volume',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Volume')))
    fig1=plot(fig1,output_type="div")
    data2=[go.Line(x=df["Date"],y=df["Normed_Return"])]
    fig2 = go.Figure(data = data2,layout = go.Layout(title='Facebook Return',
                                       xaxis = dict(title = 'Date'), yaxis = dict(title = 'Return')))
    fig2=plot(fig2,output_type="div")
    return render(request,"user_facebook.html",context={'fig':fig,'fig1':fig1,'fig2':fig2})

def user_cisco(request):
    cisco = yf.download(tickers='CSCO', period='5y', interval='1d')
    cisco.to_csv("cisco.csv")
    df=pd.read_csv("cisco.csv")
    df["Normed_Return"]=df["Adj Close"]/df.iloc[0]["Adj Close"]
    data=[go.Line(x=df["Date"],y=df["Adj Close"])]
    fig = go.Figure(data = data,layout = go.Layout(title='Cisco adj closing price',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Closing Price')))
    fig=plot(fig,output_type="div")

    data1=[go.Line(x=df["Date"],y=df["Volume"])]
    fig1=go.Figure(data = data1,layout = go.Layout(title='Cisco Volume',
                                           xaxis = dict(title = 'Date'), yaxis = dict(title = 'Volume')))
    fig1=plot(fig1,output_type="div")
    data2=[go.Line(x=df["Date"],y=df["Normed_Return"])]
    fig2 = go.Figure(data = data2,layout = go.Layout(title='Cisco Return',
                                       xaxis = dict(title = 'Date'), yaxis = dict(title = 'Return')))
    fig2=plot(fig2,output_type="div")
    return render(request,"user_cisco.html",context={'fig':fig,'fig1':fig1,'fig2':fig2})



def registerPage(request):
	if request.user.is_authenticated:
		return redirect('login')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')


		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('user')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('user')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('index')


def calculate(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
    amount=float(amount)
    google = yf.download(tickers='GOGL', period='5y', interval='1d')
    cisco = yf.download(tickers='CSCO', period='5y', interval='1d')
    aapl = yf.download(tickers='AAPL', period='5y', interval='1d')
    fb = yf.download(tickers='FB', period='5y', interval='1d')
    google.to_json("google.json")
    cisco.to_json("cisco.json")
    aapl.to_json("apple.json")
    fb.to_json("facebook.json")

    stocks=pd.DataFrame({"google":google["Adj Close"],"cisco":cisco["Adj Close"],"apple":aapl["Adj Close"],"facebook":fb["Adj Close"]})

    log_ret=np.log(stocks/stocks.shift(1))

    np.random.seed(101)
    num_ports=25000
    all_weights=np.zeros((num_ports,len(stocks.columns)))
    ret_arr=np.zeros(num_ports)
    vol_arr=np.zeros(num_ports)
    sharp_arr=np.zeros(num_ports)
    for ind in range(num_ports):
        weights=np.array(np.random.random(4))
        weights=weights/np.sum(weights)
        all_weights[ind:]=weights
        ret_arr[ind]=np.sum((log_ret.mean()*weights)*252)
        vol_arr[ind]=np.sqrt(np.dot(weights.T,np.dot(log_ret.cov()*252,weights)))
        sharp_arr[ind]=ret_arr[ind]/vol_arr[ind]

    max=sharp_arr.argmax()
    p=[]
    for w in all_weights[max]:
        amt=w*amount
        p.append(amt)
    return render(request,"optimize.html",{"p":p})

def news(request):
    list=[]
    list1=[]
    results=requests.get("https://economictimes.indiatimes.com/markets/stocks/news")
    soup=bs4.BeautifulSoup(results.text,"lxml")
    details = soup.findAll('div',attrs={"class":"eachStory"})
    title=soup.findAll('div',attrs={"class":"eachStory"})
    for x in title:
        list.append(x.find('h3').text)
    for i in details:
        list1.append(i.find('p').text)
    return render(request,"news.html",context={"list":list,"list1":list1})
