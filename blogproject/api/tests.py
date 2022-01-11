from django.test import TestCase
from rest_framework.utils import json

from .models import Posts
from rest_framework import status


class CreateTestCase(TestCase):
    def test_can_create_posts(self):
        data = {
             "title": "Hello cui",
             "content": "Hello world dang dang"
        }
        response = self.client.post("/posts", data=data)
        self.assertEqual(Posts.objects.count(), 1)

    def test_can_get_posts(self):
        response = self.client.get("/posts")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        pay = Posts.objects.create(title="example ", content="content example")
        return pay

    def test_can_delete_posts(self):
        posts = self.create_post()
        pk = posts.pk
        get_posts = Posts.objects.get(pk=posts.pk)
        del_posts = get_posts.delete()
        self.assertFalse(Posts.objects.filter(pk=pk).exists())

    def test_can_retrieve_posts(self):
        posts = self.create_post()
        pk = posts.pk
        self.assertTrue(Posts.objects.filter(pk=pk).exists())

    def test_can_update_posts(self):
        posts = self.create_post()
        data = {
            "title": "Update Hello cui",
            "content": "Update Hello world dang dang"
        }
        resp = self.client.patch('/posts/{}'.format(posts.pk),
                                 content_type='application/json',
                                 data=json.dumps(data))
        posts.refresh_from_db()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(posts.title, 'Update Hello cui')

