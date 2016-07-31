from scrapy import cmdline


def main():
    cmdline.execute('scrapy crawl optionsspider'.split())


if __name__ == '__main__':
    main()
