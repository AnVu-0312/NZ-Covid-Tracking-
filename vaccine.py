import sys
import scrapy 
from scrapy.crawler import CrawlerProcess
import json
import pandas as pd

class Vaccine_data(scrapy.Spider):
    name = "Vaccine_data"
    def start_requests(self):
        url = "https://www.health.govt.nz/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-vaccine-data"
        yield scrapy.Request (url = url, callback = self.parse)
    def parse (self, response):
        data ={}
        df_vaccine = pd.DataFrame(data, columns=['DHB of residence', 'Fully vacc','Population'])
        vaccine_xpath = response.xpath('//*[@class="table-style-two table"]//tbody/tr')
        for row in vaccine_xpath[13:35]:    
            data = {
                'DHB of residence': row.xpath('th//text()').extract_first(),
                'Fully vacc': row.xpath('td[3]//text()').extract_first(),
                'Population' : row.xpath('td[5]//text()').extract_first(),
            }
            df_vaccine = df_vaccine.append(data, ignore_index=True)
        df_vaccine.to_json(r'vaccine_data.json',orient="records")
process = CrawlerProcess()
process.crawl(Vaccine_data)
process.start()