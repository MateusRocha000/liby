import requests
import xml.etree.ElementTree as ET

class Api():
	def __init__(self):
		self.key = 'nJnSnY5HiDBworJBSyeHQ'
		self.secret = 'Saaou7wsoAEft0mGJaeaZiSTmXvz0WHqfRBlW199A'
		self.url = 'https://www.goodreads.com/search/index.xml'

	def findBooks(self, q):
		params = {
			'q' : q,
			'key' : self.key,
			'format' : 'json',
		}

		r = requests.get(self.url, params=params)

		return r

a = Api()
r = a.findBooks('o guia do mochileiro')
print(r.text)
xml = ET.fromstring(r.text)