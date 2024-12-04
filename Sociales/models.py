from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class Roles(models.TextChoices):
    FORMER = 'FORMER_STUDENT' ,'Cựu học sinh'
    LECTURER = 'LECTURER', 'Giảng viên'
    ADMIN = 'ADMIN', 'Quản trị viên'
class User(AbstractUser ,BaseModel):
    username = models.CharField(max_length=50,unique=True)
    verified = models.BooleanField(default=False)
    role = models.CharField(choices=Roles.choices , max_length=50)
    avatar_user = CloudinaryField('avatar',blank =True, default="https://res.cloudinary.com/dxiawzgnz/image/upload/v1732632586/pfvvxablnkaeqmmbqeit.png")
    cover_photo = CloudinaryField('cover' , blank = True ,null =True)




