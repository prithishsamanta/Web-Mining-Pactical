#concurrent crawler has the slight modification from sequential crawler where it uses multithreading concept which makes it faster
#constructor invokes __init__ function which assigns and formats the base url
#number of threads used are 5
#assign a data structure for scrapped pages
#then extract all the urls in runscrapper function


#The following python code is for a Concurrent Crawler which uses the concept of threads to crawls a website. The website which is crawled in this code is the Apple Website

import requests
import multiprocessing
from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse

class MultiThreadScraper:
    #content = list()

    def __init__(self, burl):
        self.burl = burl
        self.rurl = '{}://{}'.format(urlparse(self.burl).scheme, urlparse(self.burl).netloc)
        #ThreadPoolExecutor uses a pool of threads to execute calls asynchronously
        self.pool = ThreadPoolExecutor(max_workers = 5)
        self.scraped_pages = set([]) #crawled history urls
        self.to_crawl = Queue() #crawl frontier
        self.to_crawl.put(self.burl)

    def parse_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a', href=True)
        for l in links:
            url = l['href']
            if url.startswith('/') or url.startswith(self.rurl):
                url = urljoin(self.rurl, url)
                if url not in self.scraped_pages:
                    self.to_crawl.put(url) #crawl frontier

    def post_scrape_callback(self, reslt):
        result = reslt.result()
        if result and result.status_code == 200:
            self.parse_links(result.text) #method to extract the links
            self.scrape_info(result.text) #method tot extract the contents

    def scrape_page(self, url):
        try:
            reslt = requests.get(url, timeout=(3, 30))
            return reslt
        except requests.RequestsException:
            return


    def scrape_info(self, html):
        soup = BeautifulSoup(html, "html5lib")
        text = soup.get_text(strip = True)
        print(text)
        return
    
    def rn_scrpr(self):
        while True:
            try:
                print("\n name of the Process: \n", multiprocessing.current_process().name)
                target_url = self.to_crawl.get(timeout = 1000)
                if target_url not in self.scraped_pages:
                    #not in history URL
                    print("Scrapping URL: {}".format(target_url))
                    self.scraped_pages.add(target_url)
                    job = self.pool.submit(self.scrape_page, target_url)
                    job.add_done_callback(self.post_scrape_callback)
            except Empty:
                return
            except Exception as e:
                print(e)
                continue

#creating the main 
if __name__ == '__main__':
    print("CODE FOR CONCURRENT CRAWLER")
    s = MultiThreadScraper("https://www.apple.com/in/?afid=p238%7CsdUuvv563-dc_mtid_187079nc38483_pcrid_537406547405_pgrid_109516736379_&cid=aos-IN-kwgo-brand--slid---product-")
    s.rn_scrpr()
    
