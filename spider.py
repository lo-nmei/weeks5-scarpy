#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

results = []

def parse(response):
    for comment in response.css('div.comment-list-item'):
        result['name'] = comment.xpath('.//a[@class="username"]/text()').extract_first().strip()
        result['conent'] = comment.xpath('.//p/text()').extract_first()
        results.append(result)

def has_next_page(response):
    classes = response.xpath('//li[contains(@class="next-page")]/@class').extract_first()
    return 'disabled' not in classes

def goto_next_page(driver):
    elem = driver.find_element_by_xpath('//li[@class="next-page"]')
    elem.click()

def wait_page_return(driver,page):
    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element(
            (By.XPATH,'//ul[@class="pagination"]/li[@class="active"]'),
            str(page)
        )
    )

def spider():
    driver = webdriver.PhantomJS()
    url = "https://shiyanlou/courses/427"
    driver.get(url)
    page = 1
    while True:
        wait_page_return(driver,page)
        html = driver.page_sourse
        response = HtmlResponse(url=url, body=html.encode('utf-8'))
        parse(response)
        if not has_next_page(response):
            break
        page += 1
        goto_next+page(driver)
    with open('/home/shiyanlou/comments.json','w') as f:
        f.write(json.dumps(results))


if __name__ == "__main__":
    spider()
