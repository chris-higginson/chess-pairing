# algorithm for organising chess tournament pairing
import re
import numpy as np
import pandas as pd


class player():
    '''object to record information on each player, 
    some of which is relational and history-dependent'''

    def __init__(self,
                 name,
                 affiliation,
                 TELO = 1200,
                 history = [],
                 chessdotcom_username = [],
                 lichess_username = []):
    	''''''
        self.name = name
        self.affiliation = affiliation
        self.TELO = TELO
        self.history = history
        self.chessdotcom_username
        self.lichess_username

    @property
    def history(self):
    	return self._history

    @affiliation.setter 
    def history(self, value):
    	self._history = value

###

# pairing mechanism 

## essential rules:
# 1. No rematches
# 2. No repeat byes for the same person
# 3. Non-top-scorers with same absolute colour preference can't match (why only non-top-scorers?)

## process:
# 1. Round one: Inputs: sorted players:
#		Separate players into two groups (G1, G2), with the bottom group containing any remainder
# 		If there is a remainder, the last player in G2 receives a one-point bye
#		Match #1 of G1 with #1 of G2, etc (i.e. #1 with #(N//2)+1)
#		Allocate colours (randomly?)
#			output: list of pairs of players and un-paired players (i.e. Bye)
# 2. Other rounds: Sorted players with history:
#		

# 		





## colour preference function

def colour_pref(colours):
    """Determine player colour preference for next round
    
    Input: String of previously played colours, or pd.DataFrame 
    
    Output: 
        Preference for white (-ve) or black (+ve)
        Absolute value represents preference strength
        Prioritises preference based on recent game history, 
            instead of overall colour balance
    """
    if type(colours) == str:
        if re.search("[Ww]{2,}$", colours):
            return(4)
        if re.search("[Bb]{2,}$", colours):
            return(-4)
        count = colours.lower().count("w") - colours.lower().count("b")
        if abs(count) >= 1:
            return(count)*2
        if count == 0:
            if re.search("[Ww]$", colours):
                return(1)
            if re.search("[Bb]$", colours):
                return(-1)
        return(0)
    
    else:
        ans = np.array([0 for i in colours])
        ans[colours.str.contains("[Ww]$")] = 1
        ans[colours.str.contains("[Bb]$")] = -1
        count = np.asarray(colours.str.count("[Ww]") - 
        	colours.str.count("[Bb]"))
        ans[abs(count)>=1] = count[abs(count)>=1]*2
        ans[colours.str.contains("[Ww]{2,}$")] = 4
        ans[colours.str.contains("[Bb]{2,}$")] = -4
        return(ans.tolist())