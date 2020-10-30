# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:29:15 2019

@author: Guilherme
"""

import numpy as np
from github import Github
from datetime import datetime
import time

def api_wait_search(git):
  limits = git.get_rate_limit()
  if limits.core.remaining <= 2:
    seconds = (limits.core.reset - datetime.now()).total_seconds()
    print ("Waiting for %d seconds ..." % (seconds))
    time.sleep(seconds)
    print ("Done waiting - resume!")
    

# SAVE SESSION - pip install dill
"""
import dill                            #pip install dill
filename = 'resposDatabBase.pkl'
dill.dump_session(filename)

import dill                            #pip install dill
filename = 'backup_final.pkl'
dill.dump_session(filename)
"""

# LOAD SESSION - pip install dill
"""
import dill
filename = 'globalsave.pkl'
dill.load_session(filename)
"""
repos = {}
totalClosedIssuesByDate = {}
totalOpenIssuesByDate = {}

ACCESS_TOKEN = 'd46ac61a3fcb307991e7d992841dd420d90efdf5'
SECOND_ACCESS_TOKEN = '6a4d1bb0d08f88e0780ac09f76f711807ca6b8c7'
g = Github(SECOND_ACCESS_TOKEN)

#get reset timestemp g.get_rate_limit().core.raw_data

"""
for repo in g.search_repositories(query):
    print(repo)
"""
date = '2019-09-30'
dateSrt = 'created:' + date
queryOpen = 'author:app/dependabot-preview is:open language:JavaScript is:pr ' + dateSrt
queryClosed = 'author:app/dependabot-preview is:closed language:JavaScript is:pr ' + dateSrt

totalOpenIssuesByDate[date] = g.search_issues(queryOpen).totalCount
totalClosedIssuesByDate[date] = g.search_issues(queryClosed).totalCount

count = 0
"""
Get list of repos
"""
for issue in g.search_issues(queryOpen):
    count = count + 1
    print(issue.repository.full_name)
    repos[issue.repository.full_name] = issue.repository.full_name
    print(count)
    
import dill
filename = 'resposDatabBase.pkl'
dill.dump_session(filename)

"""
Get list of repos
"""

class Dict2Obj(object):
    """
    Turns a dictionary into a class
    """
 
    #----------------------------------------------------------------------
    def __init__(self, dictionary):
        """Constructor"""
        for key in dictionary:
            setattr(self, key, dictionary[key])

class pullRequest(object):
    """
        Class implementing pull request object.
    """
    def __init__(self, pull):
        self.title = pull.title
        self.user = pull.user.login
        self.created_at = pull.created_at
        self.state = pull.state
        self.merged_at = pull.merged_at
        self.merged = pull.merged
        self.labels = [k.name for k in pull.labels]
      
list_repos = [ k for k in repos ]
list_repos_info = []
count = 0

accessList = [ACCESS_TOKEN, SECOND_ACCESS_TOKEN,
              ACCESS_TOKEN, SECOND_ACCESS_TOKEN,
              ACCESS_TOKEN, SECOND_ACCESS_TOKEN,
              ACCESS_TOKEN, SECOND_ACCESS_TOKEN,
              ACCESS_TOKEN, SECOND_ACCESS_TOKEN,
              ACCESS_TOKEN, SECOND_ACCESS_TOKEN,
              ACCESS_TOKEN, SECOND_ACCESS_TOKEN,
              ACCESS_TOKEN, SECOND_ACCESS_TOKEN,
              ACCESS_TOKEN, SECOND_ACCESS_TOKEN,
              ACCESS_TOKEN, SECOND_ACCESS_TOKEN,
              ACCESS_TOKEN, SECOND_ACCESS_TOKEN,
              ACCESS_TOKEN, SECOND_ACCESS_TOKEN,
              ACCESS_TOKEN, SECOND_ACCESS_TOKEN,
              ACCESS_TOKEN, SECOND_ACCESS_TOKEN,
              ACCESS_TOKEN, SECOND_ACCESS_TOKEN]

minimum = 950
maximum = 1000

for index in range(17):
    g = Github(accessList[index])
    minimum += 40
    maximum += 40
    count = minimum
    list_repos_splited = list_repos[minimum:maximum]
    
    for repo_name in list_repos_splited:
    
        repo = g.get_repo(repo_name)
        count = count + 1
        print(str(count) + ' of ' + str(maximum))
        repo_info = { 'repo_name': repo_name,
                     'stars': repo.stargazers_count,
                     'contributors': repo.get_contributors().totalCount,
                     'issues': [] }
        
        repo_info = Dict2Obj(repo_info)
        #for pull in repo.get_pulls('all'):
        for issue in repo.get_issues(state='all', creator='dependabot-preview[bot]'):
            if issue.user.login == 'dependabot-preview[bot]':
                pull = 0
                try:
                    pull = issue.as_pull_request()/
                except:
                    print('It is not a PR')
                if pull != 0:
                    repo_info.issues.append(pullRequest(pull))
        list_repos_info.append(repo_info)
    
   
import pickle
with open('list_repos_info.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump([list_repos_info], f)
    
    
    
# Getting back the objects:
#with open('list_repos_info.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
#    list_repos_info = pickle.load(f)
    
