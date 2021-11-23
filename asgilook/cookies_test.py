import falcon
import random
import time

class TestCookies:
    async def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = (
            'get cookie'
        )
        resp.set_cookie('my_cookie', f'{random.randint(10000,99999)}',
                        max_age=60*60*24*10, path='/')

    async def on_post(self, req, resp):
        my_cookie_values = req.get_cookie_values('my_cookie')
        # print(req.headers)
        if my_cookie_values:
            v = my_cookie_values[0]
        else:
            v = "no cookie"

        data = await req.stream.read()
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        now_ = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        text = f'{now_=}, {data=}, {v=}, success cookie'
        print(text)
        resp.text = (
            text
        )


