# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from hoos.views import admin_login, admin_view, logout_view, user_map, admin_map, review_events, approve_event, admin_event_listings, user_view, submit_event, user_event_listings
# from django.urls import reverse, resolve

# class TestUrls(StaticLiveServerTestCase):
#     def setUp(self):
#         self.url_func_name_permissions = [
#             ('authenticate', admin_login, None),
#             ('home_admin', admin_view, 'admin'),
#             ('admin_logout', logout_view, 'admin'),
#             ('admin_map', admin_map, 'admin'),
#             ('admin_home', admin_view, 'admin'),
#             ('review_event', review_events, 'admin'),
#             ('approve_event', approve_event, 'admin'),
#             ('admin_event_listings', admin_event_listings, 'admin'),
#             ('admin_home_logout', logout_view, 'admin'),

#             ('home_user', user_view, 'user'),
#             ('submit_event', submit_event, 'user'),
#             ('user_logout', logout_view, 'user'),
#             ('user_home_logout', logout_view, 'user'),
#             ('user_home', user_view, 'user'),
#             ('user_map', user_map, 'user'),
#             ('user_event_listings', user_event_listings, 'user')
#         ]
    
#     def test_all_pages_resolve_depending_on_permission(self):
#         # TODO: filter based on user
#         for name, func, permission in self.url_func_name_permissions:
#             url = reverse(name)
#             self.assertEquals(resolve(url).func, func)

#     def test_admin_page_resolves_if_admin():
#         pass

#     def test_admin_page_does_not_exist_if_not_admin():
#         pass

# class TestFunctionality(StaticLiveServerTestCase):
#     def setUp(self):
#         return super().setUp()

#     def tearDown(self):
#         return super().tearDown()
    
#     def test_user_submits_event():
#         pass

#     def test_admin_approves_user_event():
#         pass

#     def test_admin_rejects_user_event():
#         pass

#     def user_submits_invalid_event():
#         # multiple tests for each error
#         # error message should be present
#         pass

