# 用户模型测试

import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
  def test_password_setter(self):
    u = User(username='john')
    u.password = 'cat'
    self.assertTrue(u.password_hash is not None)

  def test_no_password_getter(self):
    u = User(username='john', password='cat')
    # 预期抛出异常
    with self.assertRaises(AttributeError):
      u.password

  def test_password_verification(self):
    u = User(username='john')
    u.password = 'cat'
    self.assertTrue(u.verify_password('cat'))
    self.assertFalse(u.verify_password('dog'))

  def test_password_salts_are_random(self):
    u1 = User(username='john', password='cat')
    u2 = User(username='susan', password='cat')
    self.assertTrue(u1.password_hash != u2.password_hash)