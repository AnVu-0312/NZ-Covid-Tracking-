import json
import scrapy 
from scrapy.crawler import CrawlerProcess

class Covid_case(scrapy.Spider):
    name = "Covid_case_crawling"

    def start_requests(self):
        urls = ["https://www.health.govt.nz/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-current-cases/"]
        for url in urls:
            yield scrapy.Request (url = url, callback = self.parse)
    def parse (self, response):
        print("\n\n\n\n\n\n\n\n\n\n")
        print(response.css('.table-style-two>tbody>tr').extract_first())
        print("\n\n\n\n\n\n\n\n\n\n")
        # self.log(response)

        # for row in response.xpath('//*[@class="table-style-two table"]//tbody/tr'):
        for row in response.css('.table-style-two>tbody>tr'):
            yield {
                'first' : row.xpath('td[1]//text()').extract_first(),
                'last': row.xpath('td[2]//text()').extract_first(),
                'handle' : row.xpath('td[3]//text()').extract_first(),
            }
            # print(row)  
            test = {
                'first' : row.xpath('td[1]//text()').extract_first(),
                'last': row.xpath('td[2]//text()').extract_first(),
                'handle' : row.xpath('td[3]//text()').extract_first(),
            }

            # test = row.xpath('td[1]//text()').extract_first()
            # test = {}
            # test['first'] = row.xpath('td[1]//text()').extract_first()
            # test['second'] = row.xpath('td[2]//text()').extract_first()
            print("***************\n\n\n")
            # print(row.xpath('td[1]//text()').extract_first())
            # print(json.dump(test))
            print(test)
            print(json.dumps(test))
            print("\n\n\n-----------------\n\n\n")

process = CrawlerProcess()
process.crawl(Covid_case)
process.start()

