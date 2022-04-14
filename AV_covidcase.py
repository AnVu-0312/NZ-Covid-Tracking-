import scrapy 
from scrapy.crawler import CrawlerProcess

class Covid_case(scrapy.Spider):
    name = "Covid_case_crawling"

    def start_requests(self):
        url = 'https://www.health.govt.nz/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-current-cases'
        yield scrapy.Request (url = url, callback = self.parse)
    def parse (self, response):
        html_file = 'web_body.html'
        with open( html_file, 'wb' ) as fout:            
            fout.write( response.body )
  


process = CrawlerProcess()
process.crawl(Covid_case)
process.start()
print(dc_dict) 