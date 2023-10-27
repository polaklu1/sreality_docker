import scrapy
import json


class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page=1']

    def __init__(self):
        """
        Initialize spider class
        """
        super().__init__()
        self.page_idx = 1
        self.url_template = 'https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page={}'

    def parse(self, response, **kwargs):
        """
        Parse JSON data from sreality API
        :param response:
        :return:
        """
        data = json.loads(response.body)
        for item in data['_embedded']['estates']:
            title = item['name'].replace('\xa0', ' '),
            locality = item['locality'],
            image_url = item['_links']['image_middle2'][0]['href']

            yield {
                'title': title,
                'locality': locality,
                'image_url': image_url
            }

        self.page_idx += 1
        next_page = self.url_template.format(self.page_idx)

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
