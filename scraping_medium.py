import scrapy

class StoriesSpider(scrapy.StoriesSpider):
    name = "stories"

    start_urls = [
        # urls that you want to crawl
        "http://example.com/post/",
        "http://example.com/post/"
    ]

    # for all stories

    def parse(self, response):
        # replace 'path' with the actual css path where the data is located
        for story in response.css('path'):
            yield {
                # things you need to crawl
            }