import dota2api
import time

class APIInterface:
    def CheckTime(self):
        if time.time() - self.prevAccess < 1:
            time.sleep(1)
        prevAccess = time.time()

    def __init__(self, key):
        self.api = dota2api.Initialise(key)
        self.prevAccess = time.time()

    def GetMatchDetails(self, matchID):
        self.CheckTime()
        return self.api.get_match_details(match_id = matchID)

    def GetTopLiveGames(self):
        self.CheckTime()
        return self.api.get_top_live_games()

    def GetGameItems(self):
        self.CheckTime()
        return self.api.get_top_live_games()


dota2 = APIInterface("4962850F832F2E41426EC211FC5F6108")
for key, value in dota2.GetMatchDetails(1000193456).iteritems():
    print key, value
#print dota2.GetTopLiveGames()

