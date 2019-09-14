# stories_spider.py
import scrapy
from tqdm import tqdm

# from .sources import BASE_URLS, YEAR_RANGE, MONTH_RANGE
import pymongo
import pandas as pd

MONGO_URI = "mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb"
MONGO_DATABASE = "mediumCrawl"
MONGO_COLLECTION = "mediumLinks"


class LinkAgg:
    def __init__(self):
        # mongo connection
        connection = pymongo.MongoClient(MONGO_URI)
        db = connection[MONGO_DATABASE]
        data = list(db[MONGO_COLLECTION].find())
        self.df = pd.DataFrame(data)

    def get_links(self):
        # retrieve data
        # self.pubname_list = self.df['nameOfPublication'].tolist()
        # self.authorname_list = self.df['nameOfAuthor'].tolist()
        # self.authorprofile_list = self.df['linkOfAuthorProfile'].tolist()
        # self.articletitle_list = self.df['articleTitle'].tolist()
        self.articlelink_list = self.df["articleLink"].tolist()
        # self.postingtime_list = self.df['postingTime'].tolist()

        # return self.pubname_list, self.authorname_list, self.authorprofile_list, self.articletitle_list, self.articlelink_list, self.postingtime_list
        return self.articlelink_list


class StoriesSpider(scrapy.Spider):
    name = "contents"

    def start_requests(self):
        agg = LinkAgg()
        articlelink_list = agg.get_links()
        urls = articlelink_list

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # For All Stories
    def parse(self, response):

        yield {
            "nameOfPublication": "",
            "nameOfAuthor": response.css("a::text").getall()[-8],
            "articleTile": response.css("div.a.b.c  h1::text").getall(),
            "content": response.css("p::text").getall(),
            "postingTime": ""
        }
