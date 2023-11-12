# from selenium import webdriver
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from django.urls import reverse, resolve
# import time


# class TestLogin(StaticLiveServerTestCase):

#     def setUp(self):
#         self.browser = webdriver.Chrome()

#     def tearDown(self):
#         self.browser.close()

#     def test_login_as_user(self):
#         self.browser.get(self.live_server_url)

#         time.sleep(10)
#         alert = self.browser.find_element_by_class_name('noproject-wrapper')
#         self.assertEquals(
#             alert.find_elements_by_tag_name('h2').text,
#             'HoosHappenings Google Login'
#         )


#     def test_login_as_admin(self):
#         assert True
