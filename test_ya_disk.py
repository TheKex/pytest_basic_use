import pytest
from dotenv import load_dotenv
from os import getenv
import ya_disk_api.yandex_disk as yd


@pytest.fixture(scope='class')
def yd_uploader():
    print('----- load_dotenv -----')
    load_dotenv()
    token = getenv('YA_DISK_TOKEN')
    yd_up = yd.YaDiskUploader(token=token)
    return yd_up


class TestYaDisk:
    @pytest.mark.parametrize(
        'path, expected_resp_codes',
        [
            ('/test1010100101010', [200, 201]),
            ('/', [409])
        ]
    )
    def test_create_folder(self, yd_uploader, path, expected_resp_codes):
        resp = yd_uploader.create_folder(path)
        assert resp.status_code in expected_resp_codes
        yd_uploader.delete_folder(path)

    def test_auth_error(self):
        ya_disk = yd.YaDiskUploader('')
        path = '/test10101010292929292010'
        resp = ya_disk.create_folder(path)
        assert resp.status_code == 401


