import requests

def getHTMLTEXT(url):
	try:
		r = requests.get(url,timeout=30)
		r.raise_for_status()
		r.encodig = r.apparent_encoding
		print("实际请求的URL是:",r.url)
		return r.text
	except：
		return "产生异常"

if __name__ == "__main__":
		url = "https://www.miyoushe.com/sr/"
		print(getHTMLTEXT(url))