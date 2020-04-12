
import pytest



from web.Page.Index import Index

class Testindex:
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def setup(self):
        self.index = Index(reuse=True)

    # def test_download(self):
    #     self.index.download()
    #
    # def test_invite(self):
    # self.index.invite()
    @pytest.mark.repeat(3)
    def test_addmember(self):
        self.index.addmember()

    def test_leadconcat(self):
        self.index.leadconcat()

    def test_memberjoin(self):
        self.index.memberjoin()


    def test_messagequnfa(self):
        self.index.messagequnfa()

    @pytest.mark.parametrize('a', [1, 2])
    def test_kehulianxi(self,a):
        self.index.kehulianxi(a)

    def test_daka(self):
        self.index.daka()


    def teardown(self):
        pass
