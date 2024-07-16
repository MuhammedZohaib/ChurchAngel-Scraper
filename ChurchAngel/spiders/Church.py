import scrapy
from urllib.parse import urlencode, urljoin
from ChurchAngel.items import ChurchangelItem

class ChurchSpider(scrapy.Spider):
    name = "Church"
    start_urls = ["https://www.churchangel.com/directory"]
    p = 2
    _ = 1721121434754
    
    def parse(self, response):
        for church in response.css("div.sabai-col-xs-9.sabai-directory-main"):
            church_item = ChurchangelItem()
            church_item["title"] = church.css("div.sabai-directory-title a::text").get(default="N/A"),
            church_item["church_category"] = church.css("div.sabai-directory-category a::text").get(default="N/A"),
            church_item["church_tel"] = church.css("div.sabai-directory-contact-tel span.sabai-hidden-xs::text").get(default="N/A"),
            church_item["church_description"] = str(church.css("div.sabai-directory-body::text").get(default="N/A")).replace("\n", "").strip(),
            church_item["church_website"] = church.css("div.sabai-directory-contact-website a::attr('href')").get(default="N/A"),
            church_item["church_link"] = church.css("div.sabai-directory-title a::attr('href')").get(default="N/A"),
            church_item["church_category_link"] = church.css("div.sabai-directory-category a::attr('href')").get(default="N/A")
            yield church_item
        
        url = response.css('div.sabai-pull-right > div > a:last-child::attr("href")').get()
        param = {
            "p": self.p,
            "category": 0,
            "zoom": 15,
            "is_mile": 1,
            "directory_radius": 0,
            "view": "list",
            "__ajax": "#sabai-content .sabai-directory-listings-container",
            "_": self._
        }
        
        url_with_params = urljoin(url, '?' + urlencode(param))
        if url is not None:
            yield response.follow(url=url_with_params, callback=self.parse)   
            self.p =  self.p + 1
            self._ = self._ + 1

            