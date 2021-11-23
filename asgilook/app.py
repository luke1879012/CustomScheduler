import falcon.asgi

from .config import Config
from .cookies_test import TestCookies
from .images import Images
from .store import Store


def create_app(config=None):
    config = config or Config()
    store = Store(config)
    images = Images(config, store)
    tc = TestCookies()

    app = falcon.asgi.App()
    app.add_route('/images', images)
    app.add_route('/images/{image_id:uuid}.jpeg', images, suffix='image')
    app.add_route('/tc', tc)

    return app
