import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from django.http import HttpResponse,HttpRequest
import yfinance as yf
from django.http import HttpResponse
from django.shortcuts import  render, redirect

google = yf.download(tickers='GOGL', period='5y', interval='1d')
cisco = yf.download(tickers='CSCO', period='5y', interval='1d')
aapl = yf.download(tickers='AAPL', period='5y', interval='1d')
fb = yf.download(tickers='FB', period='5y', interval='1d')

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
