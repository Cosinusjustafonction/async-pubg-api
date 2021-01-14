import aiohttp
import asyncio
class pypubgi(object):

    def __init__(self,token):
        self.token = token
        self.header = {"Accept": "application/vnd.api+json", "Authorization": f"Bearer {token}"}
    
    async def request(self, query):
        async with aiohttp.ClientSession(headers=self.header) as session:
            async with session.get(query) as response:
                return await response.json()
    
    async def current_seasons(self ):
        url = "https://api.pubg.com/shards/steam/seasons"
        dictionary = await self.request(url)

        try :
            rank = dict(dictionary).get("data")
            for i in rank :
                if i.get('attributes').get('isCurrentSeason') == True :
                    season = i.get('id')
        except  Exception as e   :
            season = e

        return season
    

    #async def stats(self , season , account_id) : 
        #url = "https://api.pubg.com/shards/steam/players/{}/seasons/{}".format(account_id , season)
    
    
    async def id_from_username(self , username) : 
        url = "https://api.pubg.com/shards/steam/players?filter[playerNames]={}".format(username)
        _id = dict(await self.request(url)).get("data")[0].get("id")
        return _id
