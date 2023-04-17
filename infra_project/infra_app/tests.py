from django.test import Client, TestCase


class StaticPagesURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_page_shows_correct_content(self):
        """Проверка контента страниц."""
        response = self.guest_client.get('/')
        self.assertContains(response, 'У меня получилось!')

        response = self.guest_client.get('/second_page/')
        self.assertContains(response, 'А это вторая страница!')
