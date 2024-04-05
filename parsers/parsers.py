import requests
from bs4 import BeautifulSoup
class parser():
    def __init__(self):
        pass

    def get_page(self,url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        return response.text

class techcrunch_parser(parser):
    newsfeed_url="https://techcrunch.com/category/startups/"
    def create_search_url(self,query):
        return f"https://search.techcrunch.com/search;_ylt=AwrhS3cMLg5mPoEG4RqnBWVH;_ylc=X1MDMTE5NzgwMjkxOQRfcgMyBGZyA3RlY2hjcnVuY2gEZ3ByaWQDd2lYX0hqYnZRWWkxT1FxbU5NdVRWQQRuX3JzbHQDMARuX3N1Z2cDOARvcmlnaW4Dc2VhcmNoLnRlY2hjcnVuY2guY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAM3BHF1ZXJ5A2Rpc2NvcmQEdF9zdG1wAzE3MTIyMDU0NjU-?p={query}&fr2=sb-top&fr=techcrunch"
    def search_startup(self,startup_name):
        ret=[]
        url=self.create_search_url(startup_name)
        text=self.get_page(url)
        soup = BeautifulSoup(text, "html.parser")
        divs = soup.find_all("div", class_="d-tc")
        for div in divs:

            h_tags=div.find_all("h4",class_="pb-10")
            for h_tag in h_tags:
                a_tags=h_tag.find_all("a")
                for a_tag in a_tags:
                    buf={"url":a_tag["href"],"header":a_tag.text}
                    ret.append(buf)
        return ret
    def search_latest_news(self):
        ret=[]
        url=self.newsfeed_url
        text=self.get_page(url)
        soup = BeautifulSoup(text, "html.parser")
        h_tags=soup.find_all("h2",class_="post-block__title")
        for h_tag in h_tags:
            a_tags=h_tag.find_all("a")
            for a_tag in a_tags:
                buf = {"url": a_tag["href"], "header": clear_garbage(a_tag.text)}
                ret.append(buf)
        return ret
    def download_text(self,url):
        text = self.get_page(url)
        soup = BeautifulSoup(text, "html.parser")
        divs=soup.find_all("div",class_="article-content")
        ret=""
        for div in divs:
            ret+=div.text+"\n"
        return ret

        pass



def clear_garbage(text):
    garbage=["\n","\t"]
    for i in garbage:
        text=text.replace(i," ")
    return text