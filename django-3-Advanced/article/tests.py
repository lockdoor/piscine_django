from django.test import TestCase
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from .models import Article, UserFavouriteArticle
import sys


# Create your tests here.
class MyTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="test_password")

    def test_register_user(self):
        response = self.client.post("/register/", {
            'username': 'test_user2', 
            'password1': 'test_password', 
            'password2': 'test_password'},follow=True)
        self.assertEqual(response.status_code, 200) 
        # print(response.redirect_chain, file=sys.stderr)
        self.assertEqual(response.redirect_chain[0][0], '/login/') #should redirect to login page
        user = User.objects.filter(username='test_user2').exists()
        self.assertTrue(user)

    def test_favourites_must_login(self):
        response = self.client.get("/favourites/", follow=True)
        self.assertEqual(response.request['PATH_INFO'], "/login/")

    def test_publications_must_login(self):
        response = self.client.get("/publications/", follow=True)
        self.assertEqual(response.request['PATH_INFO'], "/login/")

    def test_publish_must_login(self):
        response = self.client.get("/publish/", follow=True)
        self.assertEqual(response.request['PATH_INFO'], "/login/")

    def test_un_register_user_can_not_login(self):
        response = self.client.login(username="test_fake_user", password="test_fake_password")
        self.assertFalse(response)

    def test_register_user_can_login(self):
        response = self.client.login(username="test_user", password="test_password")
        self.assertTrue(response)

    def test_not_login_user_can_register(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)

    def test_login_user_can_not_register(self):
        self.client.login(username="test_user", password="test_password")
        response = self.client.get("/register/")
        self.assertNotEqual(response.status_code, 200) #it should redirect 301

    def test_login_user_can_publish(self):
        data = {
            "title": "test_article",
            "synopsis": "test_synopsis",
            "content": "test_content"
        }
        self.client.login(username="test_user", password="test_password")
        self.client.post("/en/publish/", data, follow=True)
        article = Article.objects.filter(title="test_article").first()
        self.assertIsNotNone(article)

    def test_user_can_not_favorite_twice(self):
        data = {
            "title": "test_article",
            "synopsis": "test_synopsis",
            "content": "test_content"
        }
        self.client.login(username="test_user", password="test_password")

        self.client.post("/en/publish/", data, follow=True)
        article = Article.objects.filter(title="test_article").first()
        self.assertIsNotNone(article)
        self.assertEqual(article.title, data['title'])

        # first add favourite
        self.client.post('/en/add_favourtite/', {"article":article.pk})
        favouriteExist = UserFavouriteArticle.objects.filter(article=article, user=self.user).count()
        self.assertEqual(favouriteExist, 1)

        # second add favourite
        with self.assertRaises(IntegrityError):
            self.client.post('/en/add_favourtite/', {"article":article.pk}, raise_request_exception=True)
