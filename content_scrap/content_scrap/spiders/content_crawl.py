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
        self.articlelink_list = self.df["articleLink"].tolist()
        return self.articlelink_list


class StoriesSpider(scrapy.Spider):
    name = "content_scrap"

    def start_requests(self):
        agg = LinkAgg()
        articlelink_list = agg.get_links()
        urls = articlelink_list

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # For All Stories
    def parse(self, response):

        yield {
            "nameOfPublication": response.css("div.ab.af.ag h2 > a::text").getall()[-1],
            "nameOfAuthor": response.css("div.ab.af.ag h2 > a::text").getall()[-2],
            "articleTile": response.css("title::text").get(),
            "content": response.css("p::text").getall(),
            "postingTime": response.css("meta::attr(content)").getall()[10]}