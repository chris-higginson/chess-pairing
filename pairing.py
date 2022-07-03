# algorithm for organising chess tournament pairing

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
    def affiliation(self):
    	return self._affiliation

    @affiliation.setter 
    def affiliation(self, value):
    	self._affiliation = value

###

# pairing mechanism 


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