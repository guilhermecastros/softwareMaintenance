# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:15:50 2019

@author: Guilherme
"""

# library and dataset
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
 
"""
# Create data
df=pd.DataFrame({'x': range(1,101), 'y': np.random.randn(100)*15+range(1,101), 'z': (np.random.randn(100)*15+range(1,101))*2 })
 
# plot with matplotlib
plt.plot( 'x', 'y', data=df, marker='o', color='mediumvioletred')
plt.show()
 
# Just load seaborn and the chart looks better:
import seaborn as sns
plt.plot( 'x', 'y', data=df, marker='o', color='blue')
plt.show()

x1, y1 = zip(*sorted(totalClosedIssuesByDate.items())) # sorted by key, return a list of tuples
x2, y2 = zip(*sorted(totalOpenIssuesByDate.items()))
plt.plot(x1, y1, marker='o', color='blue')
plt.plot(x2, y2, marker='o', color='red')
plt.xticks(rotation=90)
plt.show()
"""

# Create data
x1, y1 = zip(*sorted(totalClosedIssuesByDate.items())) # sorted by key, return a list of tuples
x2, y2 = zip(*sorted(totalOpenIssuesByDate.items()))


"""
LINE CHART
"""
from cycler import cycler
fig, ax = plt.subplots(1,1)

# Create cycler object. Use any styling from above you please
monochrome = (cycler('color', ['k']) * cycler('linestyle', ['-', '--', ':', '=.']) * cycler('marker', ['s', '^','o','.', ',']))
ax.set_prop_cycle(monochrome)
ax.set_xticklabels(x1, rotation=90)

x1Array = np.array(x1)
x1Array.flatten()
y1Array = np.array(y1)
y1Array.flatten()

x2Array = np.array(x2)
x2Array.flatten()
y2Array = np.array(y2)
y2Array.flatten()

ax.set_xlabel('Dias do mês de Novembro')
ax.set_ylabel('Número de Pull-Requests')
ax.set_title('Pull-Requests realizados pelo DependaBot')

ax.plot(x1Array, y1Array)
ax.plot(x2Array, y2Array)
#ax.xticks(rotation=90)

"""
PIE CHART About The Searched Pull-Requests 
https://pythonspot.com/matplotlib-pie-chart/
"""

labels = 'Fechados', 'Abertos'
sizes = [sum(y2), sum(y1)]
colors = ['#cccccc', '#a6a6a6']
explode = (0.1, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct=lambda p : '{:.2f}%\n({:,.0f})'.format(p,p * sum(sizes)/100), shadow=True, startangle=140)
plt.axis('equal')
plt.title('Porcentagem de Pull-Requests Abertos/Fechados')
plt.show()

"""
PIE CHART About The Repositories' Pull-Requests Historic
https://pythonspot.com/matplotlib-pie-chart/
"""
#All Open/Closed PR's

numberOfClosedIssues = 0
numberOfIssues = 0
for repo in list_repos_info:
    for issue in repo.issues:
        numberOfIssues = numberOfIssues + 1
        if issue.merged:
            numberOfClosedIssues = numberOfClosedIssues + 1

labels = 'Fechados', 'Abertos'
sizes = [numberOfClosedIssues, numberOfIssues - numberOfClosedIssues]
colors = ['#cccccc', '#a6a6a6']
explode = (0.1, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct=lambda p : '{:.2f}%\n({:,.0f})'.format(p,p * sum(sizes)/100), shadow=True, startangle=140)
plt.axis('equal')
plt.title('% de Pull-Requests Abertos/Fechados')
plt.show()

#Closed security Pull Request
total = 0
numberOfSecurityIssues = 0
numberOfClosedSecurityIssues = 0
for repo in list_repos_info:
    for issue in repo.issues:
        total = total + 1
        if 'security' in issue.labels:
            numberOfSecurityIssues = numberOfSecurityIssues + 1
            if issue.merged:
                numberOfClosedSecurityIssues = numberOfClosedSecurityIssues + 1

labels = 'Fechados', 'Abertos'
sizes = [numberOfClosedSecurityIssues, numberOfSecurityIssues - numberOfClosedSecurityIssues]
colors = ['#cccccc', '#a6a6a6']
explode = (0.1, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct=lambda p : '{:.2f}%\n({:,.0f})'.format(p,p * sum(sizes)/100), shadow=True, startangle=140)
plt.axis('equal')
plt.title('% de Pull-Requests Abertos/Fechados de Segurança')
plt.show()

#list_repos_info issues labels merged
numberOfDependencyIssues = 0
numberOfClosedDependencyIssues = 0
for repo in list_repos_info:
    for issue in repo.issues:
        if 'security' not in issue.labels:
            numberOfDependencyIssues = numberOfDependencyIssues + 1
            if issue.merged:
                numberOfClosedDependencyIssues = numberOfClosedDependencyIssues + 1


labels = 'Fechados', 'Abertos'
sizes = [numberOfClosedDependencyIssues, numberOfDependencyIssues - numberOfClosedDependencyIssues]
colors = ['#cccccc', '#a6a6a6']
explode = (0.1, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct=lambda p : '{:.2f}%\n({:,.0f})'.format(p,p * sum(sizes)/100), shadow=True, startangle=140)
plt.axis('equal')
plt.title('% de Pull-Requests Abertos/Fechados de Dependência')
plt.show()


"""
Order data by stars and split by popular, random and not-popular
"""
#import random
#sorted_list_repos_info = sorted(list_repos_info, key=lambda x: x.stars, reverse=True)

#popularRepos = sorted_list_repos_info[0:345]
#randomRepos = random.sample(sorted_list_repos_info, 345)
#notPopularRepos = sorted_list_repos_info[(3459-345):3459]


#import dill                            #pip install dill
#filename = 'splitedDataByPopularity.pkl'
#dill.dump_session(filename)

popularReposClosedIssues = []
popularReposStars = []
for repo in popularRepos:
    closed = 0
    popularReposStars.append(repo.stars)
    for issue in repo.issues:
        if issue.merged:
            closed = closed + 1
    popularReposClosedIssues.append(closed/len(repo.issues)*100)
    
randomReposClosedIssues = []
randomReposStars = []
for repo in randomRepos:
    closed = 0
    randomReposStars.append(repo.stars)
    for issue in repo.issues:
        if issue.merged:
            closed = closed + 1
    randomReposClosedIssues.append(closed/len(repo.issues)*100)

notPopularReposClosedIssues = []
notPopularReposStars = []
for repo in notPopularRepos:
    closed = 0
    notPopularReposStars.append(repo.stars)
    for issue in repo.issues:
        if issue.merged:
            closed = closed + 1
    notPopularReposClosedIssues.append(closed/len(repo.issues)*100)

box_plot_data=[np.log(popularReposStars),np.log(randomReposStars),np.log(notPopularReposStars)]
plt.boxplot(box_plot_data, labels=['Populares','Aleatórios','Não Populares'])
plt.xlabel('Categoria dos Repositórios')
plt.ylabel('Nº de Estrelas (escala log)')
plt.show()

box_plot_data=[popularReposClosedIssues,randomReposClosedIssues,notPopularReposClosedIssues]
plt.boxplot(box_plot_data, labels=['Populares','Aleatórios','Não Populares'])
plt.xlabel('Categoria dos Repositórios')
plt.ylabel('% de Pull-Requests Fechados')
plt.show()


popularReposClosedSecurityIssues = []
popularReposStars = []
for repo in popularRepos:
    closed = 0
    totalSecurityIssues = 0
    for issue in repo.issues:
        if 'security' in issue.labels:
            totalSecurityIssues = totalSecurityIssues + 1
            if issue.merged:
                closed = closed + 1
    if totalSecurityIssues == 0:
        totalSecurityIssues = 1
    popularReposClosedSecurityIssues.append(closed/totalSecurityIssues*100)
    
randomReposClosedSecurityIssues = []
randomReposStars = []
for repo in randomRepos:
    closed = 0
    totalSecurityIssues = 0
    for issue in repo.issues:
        if 'security' in issue.labels:
            totalSecurityIssues = totalSecurityIssues + 1
            if issue.merged:
                closed = closed + 1
    if totalSecurityIssues == 0:
        totalSecurityIssues = 1
    randomReposClosedSecurityIssues.append(closed/totalSecurityIssues*100)

notPopularReposClosedSecurityIssues = []
notPopularReposStars = []
for repo in notPopularRepos:
    closed = 0
    totalSecurityIssues = 0
    for issue in repo.issues:
        if 'security' in issue.labels:
            totalSecurityIssues = totalSecurityIssues + 1
            if issue.merged:
                closed = closed + 1
    if totalSecurityIssues == 0:
        totalSecurityIssues = 1
    notPopularReposClosedSecurityIssues.append(closed/totalSecurityIssues*100)

box_plot_data=[popularReposClosedSecurityIssues,randomReposClosedSecurityIssues,notPopularReposClosedSecurityIssues]
plt.boxplot(box_plot_data, labels=['Populares','Aleatórios','Não Populares'])
plt.xlabel('Categoria dos Repositórios')
plt.ylabel('% de Pull-Requests Fechados de Segurança')
plt.show()


popularReposClosedDepencencyIssues = []
popularReposStars = []
for repo in popularRepos:
    closed = 0
    totalDependencyIssues = 0
    for issue in repo.issues:
        if 'security' not in issue.labels:
            totalDependencyIssues = totalDependencyIssues + 1
            if issue.merged:
                closed = closed + 1
    if totalDependencyIssues == 0:
        totalDependencyIssues = 1
    popularReposClosedDepencencyIssues.append(closed/totalDependencyIssues*100)
    
randomReposClosedDependencyIssues = []
randomReposStars = []
for repo in randomRepos:
    closed = 0
    totalDependencyIssues = 0
    for issue in repo.issues:
        if 'security' not in issue.labels:
            totalDependencyIssues = totalDependencyIssues + 1
            if issue.merged:
                closed = closed + 1
    if totalDependencyIssues == 0:
        totalDependencyIssues = 1
    randomReposClosedDependencyIssues.append(closed/totalDependencyIssues*100)

notPopularReposClosedDependencyIssues = []
notPopularReposStars = []
for repo in notPopularRepos:
    closed = 0
    totalDependencyIssues = 0
    for issue in repo.issues:
        if 'security' not in issue.labels:
            totalDependencyIssues = totalDependencyIssues + 1
            if issue.merged:
                closed = closed + 1
    if totalDependencyIssues == 0:
        totalDependencyIssues = 1
    notPopularReposClosedDependencyIssues.append(closed/totalDependencyIssues*100)

box_plot_data=[popularReposClosedDepencencyIssues,randomReposClosedDependencyIssues,notPopularReposClosedDependencyIssues]
plt.boxplot(box_plot_data, labels=['Populares','Aleatórios','Não Populares'])
plt.xlabel('Categoria dos Repositórios')
plt.ylabel('% de Pull-Requests Fechados de Dependência')
plt.show()









