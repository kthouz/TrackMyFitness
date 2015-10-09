#This script plays with misftit
from misfit import Misfit
from misfit.auth import MisfitAuth
from pprint import pprint
import pandas as pd
import os, time

class MyFitness():
    """
    This class creates a misfit object which can be used by the user
    to access his/her profile, retrieve historical data on his/her goals,
    daity activity, performance and analysis.
    Later, the class will be extended to allow the user to look at his/her
    friends' data
    """
    def __init__(self,path):
        """
        Initialize my fitness object object
        path: str, path to the directory which contains credentials file
        """
        credentials = pd.read_csv(os.path.join(path,'credentials.csv'))
        self._client_id = credentials['client_id'][0]
        self._client_secret = credentials['client_secret'][0]
        self._access_token = credentials['access_token'][0]
        self.misfit = Misfit(self._client_id, self._client_secret, self._access_token)

    def getProfile(self):
        """
        This method returns data on the user's profile
        """
        print "Fetching user's profile ... ";
        profile = self.misfit.profile().data
        print "Done!"
        return profile

    def getGoals(self,start_date = '2015-10-1', end_date = time.strftime("%Y-%m-%d")):
        """
        This method return goals between
        start_date: str, starting date
        end_date: str, end date
        dates should be given in string  format as yyyy-mm-d or format("%Y-%m-%d") 
        """
        goals = self.misfit.goal(start_date,end_date)
        goals_dict = {'date':[],'targetPoints':[],'points':[]}

        print "Fetching user's goals ... "
        for i in range(0,len(goals)):
            goal = goals[i]
            goals_dict['date'].append(str(goal.date.date()))
            goals_dict['targetPoints'].append(goal.targetPoints)
            goals_dict['points'].append(goal.points)

        print len(goals), " goals found :-)"

        return pd.DataFrame(goals_dict)

    def getActivity(self):
        pass

    def analyzePerformance(self):
        pass
            

if __name__ == '__main__':
    path = '/Users/cgirabawe/SideProjects/Misfit'
    myfitness = MyFitness(path)

    user_profile = myfitness.getProfile()
    pprint(user_profile)

    user_goals = myfitness.getGoals()
    print user_goals
