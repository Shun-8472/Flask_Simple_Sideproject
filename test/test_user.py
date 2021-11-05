import unittest
from main import app
import json
from rich import print
from rich.console import Console
console = Console()

class SettingBase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.userName = "Admin"
        self.password = "998756"
        self.role = "1"
    
    # def teardown(self):
    #     db.session.remove()
    #     db.drop_all()

    def logIn(self):
        payload = json.dumps({"name": self.userName, "password": self.password, "role": self.role})
        
        headers = {
            # Json Web Token
            'Authorization': 'Bearer {}'.format('')
        }
        response = self.app.post("/users", data = payload, content_type='application/json', headers = headers)

        return response


class CheckUserAndLogin(SettingBase):

    def test_logIn(self):
        response = self.logIn()
        self.assertEqual(response.status_code, 200)

    # test Password is less than six digits
    def test_logIn_password(self):
        # 測試密碼少於六位數
        self.password = '123'
        response = self.logIn()
        self.assertEqual(response.status_code, 433)
    