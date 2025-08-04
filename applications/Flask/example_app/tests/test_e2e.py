# 端到端测试

import time
import unittest
from playwright.sync_api import sync_playwright
import re
from app import create_app, db, fake
from app.models import User, Role
import threading


class E2ETestCase(unittest.TestCase):
  pcm = None
  browser = None

  @classmethod
  def setUpClass(cls):
    import os
    print(os.getpid())  # make sure process gone when test done!

    cls.pcm = sync_playwright().start()
    # headless=False: view broweres
    cls.browser = cls.pcm.chromium.launch(headless=False)

    # create the application
    cls.app = create_app(config_name='testing')
    cls.app_context = cls.app.app_context()
    cls.app_context.push()

    # create the database and populate with some fake data
    db.create_all()
    Role.insert_roles()
    fake.users(10)
    fake.posts(10)

    # add an administrator user
    admin_role = Role.query.filter_by(name='Administrator').first()
    admin = User(email='john@example.com',
                 username='john', password='cat',
                 role=admin_role, confirmed=True)
    db.session.add(admin)
    db.session.commit()

    # start the Flask server in a thread
    cls.server_thread = threading.Thread(target=cls.app.run,
                                         kwargs={'debug': False})
    cls.server_thread.setDaemon(True)  # as a daemon thread!
    cls.server_thread.start()

    # give the server a second to ensure it is up
    time.sleep(1)

  @classmethod
  def tearDownClass(cls):
    if cls.browser:

      # stop the flask server and the browser
      # _page = cls.browser.new_page()
      # _page.goto('http://localhost:5000/shutdown')
      # print(_page.content())
      # cls.server_thread.join() # not wait daemon

      cls.browser.close()
      cls.pcm.stop()

      # destroy database
      db.drop_all()
      db.session.remove()

      # remove application context
      cls.app_context.pop()

  def setUp(self):
    if not self.browser:
      print('Web browser not available')
      self.skipTest('Web browser not available')
    else:
      self.page = self.browser.new_page()

  def tearDown(self):
    pass

  def test_admin_home_page(self):
      # navigate to home page
    self.page.goto('http://localhost:5000/')
    self.assertTrue(re.search('Hello,\s+Stranger!',
                              self.page.content()))

    # navigate to login page
    self.page.get_by_text('Log In').click()
    self.assertIn('<h1>Login</h1>', self.page.content())

    # login
    self.page.get_by_label('email').fill('john@example.com')
    self.page.get_by_label('password').fill('cat')
    self.page.locator('id=submit').click()
    self.assertTrue(re.search('Hello,\s+john\s+!', self.page.content()))

    # navigate to the user's profile page
    self.page.get_by_text('Profile').click()
    self.assertIn('<h1>john</h1>', self.page.content())
