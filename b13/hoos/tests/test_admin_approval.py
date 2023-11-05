from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class TestPagesResolve(StaticLiveServerTestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_submission_page_resolves():
        pass

    def test_admin_page_resolves_if_admin():
        pass

    def test_admin_page_does_not_exist_if_not_admin():
        pass

class TestFunctionality(StaticLiveServerTestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_user_submits_event():
        pass

    def test_admin_approves_user_event():
        pass

    def test_admin_rejects_user_event():
        pass

    def user_submits_invalid_event():
        # multiple tests for each error
        # error message should be present
        pass

