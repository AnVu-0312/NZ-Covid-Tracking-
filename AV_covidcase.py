import json
import pandas as pd
import sys
import scrapy 
from scrapy.crawler import CrawlerProcess

class Covid_case(scrapy.Spider):
    name = "Covid_case_crawling"

    def start_requests(self):
        urls = ["https://www.health.govt.nz/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-current-cases/"]
        for url in urls:
            yield scrapy.Request (url = url, callback = self.parse)
    def parse (self, response):
            data ={}
            df_covidcase = pd.DataFrame(data, columns=['Location', 'Active','Recovered','Deceased','Total', 'Change in last 24 hours'])
            covid_case_css = response.xpath('//*[@class="table-style-two table"]//tbody/tr')
            for row in covid_case_css:
                data = {
                    'Location' : row.xpath('td[1]//text()').extract_first(),
                    'Active': row.xpath('td[2]//text()').extract_first(),
                    'Recovered' : row.xpath('td[3]//text()').extract_first(),
                    'Deceased' : row.xpath('td[4]//text()').extract_first(),
                    'Total' : row.xpath('td[5]//text()').extract_first(),
                    'Change in last 24 hours' : row.xpath('td[6]//text()').extract_first()
                    }
                df_covidcase = df_covidcase.append(data,ignore_index = True)
            df_covidcase.to_json(r'covid_case.json',orient="records")
            
process = CrawlerProcess()
process.crawl(Covid_case)
process.start()

