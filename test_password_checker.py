import unittest
from password_checker import check_password_strength

class TestPasswordChecker(unittest.TestCase):
    def test_strong_password(self):
        self.assertEqual(check_password_strength("Passw0rd!")[0], True)

    def test_missing_uppercase(self):
        self.assertEqual(check_password_strength("passw0rd!")[0], False)

    # 添加更多测试用例...

if __name__ == '__main__':
    unittest.main()