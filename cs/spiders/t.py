import scrapy


class QuotesSpider(scrapy.Spider):
    name = "t"

    def start_requests(self):
        urls = [
            'http://127.0.0.1:8000/tc',
            # 'https://www.baidu.com',
        ]
        # for ip in ["taobao", "tmall", "jd"]:
        for shop_id in ["leqee", "ahc", "bbb", "ccc", "ddd"]:
            for url in urls:
                c = {"my_cookie": str(shop_id)}
                yield scrapy.Request(url=url, callback=self.parse, cookies=c,
                                     meta={'cc': c, "download_slot": str(shop_id)}, dont_filter=True)

    def parse(self, response, **kwargs):
        text = response.text
        # print(response.__dir__())
        # print(response.headers)
        print(text)
        for i in range(100, 999):
            yield scrapy.FormRequest(url='http://127.0.0.1:8000/tc',
                                     formdata={"data_key": f"data_value_{i}"},
                                     callback=self.parse_info, cookies=response.meta["cc"],
                                     dont_filter=True, meta=response.meta)

    def parse_info(self, response, **kwargs):
        print(response.text)