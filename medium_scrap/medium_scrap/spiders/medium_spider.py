# stories_spider.py
import scrapy
from tqdm import tqdm

# BASE_URL = ["https://towardsdatascience.com/archive/",
#             'https://blog.exploratory.io/archive/',
#             'https://medium.com/applied-data-science/archive/',
#             'https://medium.com/center-for-data-science/archive/',
#             'https://medium.com/learning-new-stuff/archive/',
#             'https://machinelearnings.co/archive/',
#             'https://medium.com/machine-learning-for-humans/archive/',
#             'https://medium.com/mlreview/archive/',
#             'https://medium.com/open-machine-learning-course/archive/',
#             'https://blog.metaflow.fr/archive/',
#             'https://medium.com/inside-machine-learning/archive']

BASE_URL = "https://towardsdatascience.com/archive/"

YEAR_RANGE = [str(i) for i in range(2019, 2020)]
MONTH_RANGE = ["%.2d" % i for i in range(1, 3)]
# DAY_RANGE = ["%.2d" % i for i in range(1, 32)]



class LinkAgg:
    def __init__(self):
        self.base_url = BASE_URL
        self.year_list = YEAR_RANGE
        self.month_list = MONTH_RANGE
        # self.day_list = DAY_RANGE
        self.link_list = []

    def get_links(self):
        for year in self.year_list:
            for month in self.month_list:

                link = self.base_url + year + "/" + month
                self.link_list.append(link)

        return self.link_list


class StoriesSpider(scrapy.Spider):
    name = "stories"

    def start_requests(self):
        urls = LinkAgg().get_links()

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # For All Stories
    def parse(self, response):
        for story in response.css("div.postArticle"):
            yield {
                "nameOfPublication": story.css(
                    "a.ds-link::attr(data-collection-slug)"
                ).get(),
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
