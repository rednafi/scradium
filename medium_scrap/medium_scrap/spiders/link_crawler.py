# stories_spider.py
import scrapy
from tqdm import tqdm
from .sources import BASE_URLS, YEAR_RANGE, MONTH_RANGE


class LinkAgg:
    def __init__(self):
        self.base_urls = BASE_URLS
        self.year_list = YEAR_RANGE
        self.month_list = MONTH_RANGE
        self.link_list = []

    def get_links(self):
        for base_url in self.base_urls:
            for year in self.year_list:
                for month in self.month_list:
                    link = base_url + year + "/" + month
                    self.link_list.append(link)

        return self.link_list


class StoriesSpider(scrapy.Spider):
    name = "links"

    def start_requests(self):
        urls = LinkAgg().get_links()

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # For All Stories
    def parse(self, response):
        for story in response.css("div.postArticle"):
            yield {
                "nameOfPublication": story.css("a.ds-link::text").getall()[-1],
                "nameOfAuthor": story.css("a.ds-link::text").get(),
                "linkOfAuthorProfile": story.css("a::attr(href)").get(),
                "articleTitle": story.css(
                    "div.postArticle-content section div.section-content div h3::text"
                ).get(),
                "articleLink": story.css(
                    "div.postArticle-readMore a::attr(href)"
                ).get(),
                "postingTime": story.css("time::attr(datetime)").get(),
            }
