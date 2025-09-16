from django.test import TestCase
from django.urls import reverse
from cms.models import Page, Nav, SubNav


class CMSViewsTest(TestCase):

    def setUp(self):
        """
        Create common test data for all tests.
        This runs before each test method.
        """
        # Create a Page
        self.page = Page.objects.create(
            permalink="home",
            title="Home Page",
            content="<h1>Welcome to CMS</h1>",
            active=True
        )

        # Create Nav and SubNav
        self.nav = Nav.objects.create(
            name="Main",
            link="/main/",
            position=1,
            active=True
        )
        self.subnav = SubNav.objects.create(
            nav=self.nav,
            name="Sub Main",
            link="/sub-main/",
            position=1,
            active=True
        )

    def test_home_page_view(self):
        """Home page should return 200 OK"""
        response = self.client.get(reverse("cms:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to CMS")

    def test_custom_page_view(self):
        """Custom page should return 200 OK"""
        Page.objects.create(
            permalink="test-page",
            title="Test Page",
            content="<p>Hello Test</p>",
            active=True
        )
        response = self.client.get("/test-page/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello Test")

    def test_404_for_nonexistent_page(self):
        """Non-existent pages should return 404"""
        response = self.client.get("/does-not-exist/")
        self.assertEqual(response.status_code, 404)

    def test_nav_items_render(self):
        """Navigation items should be present in the response"""
        response = self.client.get(reverse("cms:home"))
        self.assertContains(response, "Main")
        self.assertContains(response, "Sub Main")
