#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 02:07:06 2019

@author: Adamlkl
"""
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='adamlkl', api_key='IRt8PniwKeuYgg1zTEoz')

import numpy as np
import random

def compute_data(n):
    x, y = 0, 0
    for c in range(n):
        (dx, dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return(x,y)

def random_walk_2d(n1, n2):
    x = [0]
    y = [0]
    for c in range(n1):
        tx, ty = compute_data(n2)
        x.append(tx+np.random.normal())
        y.append(ty+np.random.normal())
    
    trace1 = go.Scatter(
        x=x,
        y=y,
        mode='markers',
        name='Random Walk',
        marker=dict(
            color=[i for i in range(len(x))],
            size=8,
            colorscale='Greens',
            showscale=True
        )
    )
    data = [trace1]
    
    #plotting in your profile 
    py.iplot(data, filename='random-walk-2d')
    
    #plotting on a html page
    fig= go.Figure(data=data)
    plotly.offline.plot(fig, auto_open=True)

def random_walk_1d():        
    x = [0]
    
    for j in range(10000):
        step_x = random.randint(0,1)
        if step_x == 1:
            x.append(x[j] + 1 + 0.05*np.random.normal())
        else:
            x.append(x[j] - 1 + 0.05*np.random.normal())
            
    y = [0.05*np.random.normal() for j in range(len(x))]
            
    trace1 = go.Scatter(
        x=x,
        y=y,
        mode='markers',
        name='Random Walk in 1D',
        marker=dict(
            color=[i for i in range(len(x))],
            size=7,
            colorscale=[[0, 'rgb(178,10,28)'], [0.50, 'rgb(245,160,105)'],
                        [0.66, 'rgb(245,195,157)'], [1, 'rgb(220,220,220)']],
            showscale=True,
        )
    )
    
    layout = go.Layout(
        yaxis=dict(
            range=[-1, 1]
        )
    )
        
    data = [trace1]
    fig= go.Figure(data=data, layout=layout)
    
    #plotting in your profile 
    py.iplot(fig, filename='random-walk-1d')
    
    #plotting on a html page
    plotly.offline.plot(fig, auto_open=True)


def make_graph(n):
    if n == 1:
        random_walk_1d()
    else: 
        random_walk_2d(1000,50)

#construct random walk scatter chart: 1 for 1d; 2 for 2d
make_graph(2)