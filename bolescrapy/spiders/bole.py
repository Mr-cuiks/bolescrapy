# -*- coding: utf-8 -*-
import scrapy
from bolescrapy.items import BolescrapyItem
from scrapy.http import Request


class BoleSpider(scrapy.Spider):
    name = 'bole'
    # allowed_domains = ['python.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        dict_tital = {}
        items = response.xpath('//div[@class="post floated-thumb"]')
        for item_each in items:
            title = item_each.css('.post-meta .archive-title::text').extract()[0]
            href = item_each.css('.post-meta .archive-title::attr(href)').extract()[0]
            img = item_each.css('.post-thumb img::attr(src)').extract()[0]
            yield Request(url=href, callback=self.parse_article)
            # dict_tital.update({titles[i]: hrefs[i]})
        # print(dict_tital)
        next_url = response.css('.next.page-numbers::attr(href)').extract()[0]
        if next_url:
            yield Request(url=next_url, callback=self.parse)

    def parse_article(self, response):
        title = response.css('.entry-header h1::text').extract_first('')
        articles = response.css('.entry p::text').extract()
        article = ''
        for i in articles:
            article = article + i
        tag = response.css('.entry-meta-hide-on-mobile a::text').extract_first('')
        par_num = response.css('.vote-post-up h10::text').extract_first('0')
        creat_date = response.css('.entry-meta-hide-on-mobile::text').extract_first('').replace('\t', '').replace('\n',
                                                                                                                  '').replace(
            '\r', '').replace(' ', '')
        fav_num = response.css('.bookmark-btn::text').extract_first('')
        comment_num = response.css('.btn-bluet-bigger.href-style.hide-on-480::text').extract_first('')
        Item = BolescrapyItem()
        Item['title'] = title
        Item['article'] = article
        Item['tag'] = tag
        Item['par_num'] = par_num
        Item['creat_date'] = creat_date
        Item['fav_num'] = fav_num
        Item['comment_num'] = comment_num
        yield Item
