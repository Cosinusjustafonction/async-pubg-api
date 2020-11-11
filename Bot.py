import aiohttp

class Bot:
	def __init__(self,token):
		self.token = token
		self.header = {"Accept": "application/vnd.api+json", "Authorization": f"Bearer {token}"}
	def request(self, query):
		async with aiohttp.ClientSession(headers=self.header) as session:
			async with session.get(query) as response:
				return response.content
	def last_season
