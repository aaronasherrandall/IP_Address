from urllib.request import urlopen
from bs4 import BeautifulSoup

class IPLocationFinder:
	def __init__(self):
		self.keycdn = "https://tools.keycdn.com/geo?host="

	def findIpLocation(self, ipaddr):
		self.keycdn = self.keycdn + ipaddr
		html_page = urlopen(self.keycdn)
		soup = BeautifulSoup(html_page, 'html.parser')

		jasonData = soup.find("table").text.strip()
		jasonData = jasonData.splitlines()

		dataLength = len(jasonData ) -1;
		for x in range(0, dataLength, 2):
			if jasonData[x] and jasonData[ x +1]:
				data = jasonData[x] + " = " + jasonData[ x +1]
				print(data)

	def startApp(self, ipaddr):
		if not ipaddr:
			print("Please enter a valid ip address!")
		else:
			self.findIpLocation(ipaddr)


if __name__ == "__main__":
	ipLoc = IPLocationFinder()
	ipLoc.startApp("123.216.148.109")