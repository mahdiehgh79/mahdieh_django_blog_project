from django.test import TestCase

from django.contrib.auth.models import  User
from .models import Post
from django.shortcuts import reverse

class BlogPostTest(TestCase):
     @classmethod
     def setUpTestData(cls):
         cls.user = User.objects.create(username='user1' )

         cls.post = Post.objects.create(
         title="post",
         text='this is mmmmm',
         statues=Post.STATUES_CHOISES[0],
         author=cls.user,
     )
     #def setUp(self):


     def test_post_list_Url(self):
         response = self.client.get('/blog/')
         self.assertEqual(response.status_code,200)
     def test_post_list_view_Url_by_name(self):
         response = self.client.get(reverse('posts_list'))
         self.assertEqual(response.status_code, 200)
     def test_post_title_blog(self):
         response = self.client.get(reverse('posts_list'))
         self.assertContains(response,self.post.title)

     def test_post_detail_Url(self):
         response = self.client.get(f'/blog/{self.post.id}/')
         self.assertEqual(response.status_code, 200)
     def test_post_detail_view_Url_by_name(self):
         response = self.client.get(reverse('posts_detail', args=[self.post.id]))
         self.assertEqual(response.status_code, 200)




