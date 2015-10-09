#This script plays with misftit
from misfit import Misfit
from misfit.auth import MisfitAuth
import pandas as pd
import os, time

class MyFitness():
    def __init__(self,path):
        """Initialize the object
        """
        credentials = pd.read_csv(os.path.join(path,'credentials.csv'))
        self._client_id = credentials['client_id'][0]
        self._client_secret = credentials['client_secret'][0]
        self._access_token = credentials['access_token'][0]
        self.misfit = Misfit(self._client_id, self._client_secret, self._access_token)

    def getProfile(self):
        profile = self.misfit.profile().data
        return profile

    def getGoals(self,start_date = '2015-10-1', end_date = time.strftime("%Y-%m-%d")):
        goals = self.misfit.goal(start_date,end_date)
        goals_dict = {'date':[],'targetPoints':[],'points':[]}
        for i in range(0,len(goals)):
            goal = goals[i]
            goals_dict['date'].append(str(goal.date.date()))
            goals_dict['targetPoints'].append(goal.targetPoints)
            goals_dict['points'].append(goal.points)

        return pd.DataFrame(goals_dict)
            

if __name__ == '__main__':
    path = '/Users/cgirabawe/SideProjects/Misfit'
    mf = MyFitness(path)
