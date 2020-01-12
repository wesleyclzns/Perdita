# -*- coding: utf-8 -*-

import scrapy, json

class BrazilianStocks(scrapy.Spider):

    name = 'brazilian_stocks'
    start_urls = ['https://br.advfn.com/indice/ibovespa']

    def parse(self, response):

        data = [];
        stock_list = response.css('.stock-list tr')

        for stock in stock_list:

            name = stock.css('.Column1 a::text').get()
            ticker = stock.css('.Column2 a::text').get()
            price = stock.css('.Column3::text').get()
            variation = stock.css('.Column7::text').get()

            if unicode(ticker) == 'None' : continue

            stock = {
                'ticker': ticker,
                'name': name,
                'price': price,
                'variation': variation
            }

            data.append(stock)

        with open("output/{0}.json".format(self.name), 'w') as f:
            json.dump(data, f)