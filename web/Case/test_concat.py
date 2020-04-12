from web.Page.Concat import Concat


class Testconcat:
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'

    def setup(self):
        self.concat=Concat(reuse=True)

    def test_add(self):
        self.concat.addmember()