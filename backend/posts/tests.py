from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='first post')
        Post.objects.create(description='post description here')

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEquals(expected_object_name, 'first post')

    def test_description_content(self):
        post = Post.objects.get(id=2)
        expected_object_name = f'{post.description}'
        print(expected_object_name)
        self.assertEquals(expected_object_name, 'post description here')