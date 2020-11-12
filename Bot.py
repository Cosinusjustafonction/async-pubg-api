import aiohttp

import aiohttp
import asyncio
class Bot:
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
