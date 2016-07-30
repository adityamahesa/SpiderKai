from scrapy import cmdline


def main():
    cmdline.execute('scrapy crawl bookingspider'.split())


if __name__ == '__main__':
    main()
