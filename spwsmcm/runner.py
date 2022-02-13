import scraper_helper as sh

from collect_data.spiders.reviews_asin import ReviewsSpider
import scrapy

if __name__ == '__main__':
    import time
    startTime = time.time()
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import getProjectSettings
    settings = getProjectSettings()
    process = CrawlerProcess(settings)
    process.crawl(ReviewsSpider)
    process.start()
    print("\n\n\n\n{:.5f} Seconds".format(time.time() - startTime))
