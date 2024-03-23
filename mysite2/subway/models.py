from django.db import models

from selenium import webdriver
from selenium.webdriver.common.by import By


class Outlet(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    open_hr = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()
    waze = models.URLField()

    def __str__(self):
        return self.name

    @classmethod
    def get_data(self):
        base_url = 'https://subway.com.my/find-a-subway'
        search_filter = 'kuala lumpur'

        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        driver.get(base_url)
        driver.find_element('id', 'fp_searchAddress').send_keys(search_filter)
        driver.find_element('id', 'fp_searchAddressBtn').click()
        locs = driver.find_element('id', 'fp_locationlist')
        locs = locs.find_elements(By.CLASS_NAME, 'fp_listitem')
        for loc in locs:
            name = loc.find_element(By.TAG_NAME, 'h4').text
            if name:
                lat = loc.get_attribute('data-latitude')
                long = loc.get_attribute('data-longitude')
                ctx = loc.find_element(By.CLASS_NAME, 'infoboxcontent').find_elements(By.TAG_NAME, 'p')
                address = ctx[0].text
                open_hr = '\n'.join([i.text for i in ctx[1:] if i.text.strip()])
                waze = loc.find_element(By.CLASS_NAME, 'location_right').find_elements(By.TAG_NAME, 'a')[1].get_attribute('href')
                self.objects.create(name=name, address=address, open_hr=open_hr, lat=lat, long=long, waze=waze)
        driver.quit()