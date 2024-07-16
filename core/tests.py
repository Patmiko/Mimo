from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Post

#class Post(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     user = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='post_images')
#     caption = models.TextField()
#     created_at = models.DateTimeField(default=datetime.now())
#     no_of_likes = models.IntegerField(default=0)

# class PostTestCase(TestCase):
#     def setUp(self):
#         Post.objects.create(
#             user=User.objects.get(username="admin"),
#             caption = "Test caption",
#         )
#     def 

