from django.db import models

# Create your models here.
'''
- Courses:
    - Title
    - Description
    - Thumbnail/Image
    
    

    - Access:
        - Anyone
        - Email required
        - Purchase required
        - User required (n/a)

    - Status:
        - Published
        - Coming Soon
        - Draft

    - Lessons
        - Title
        - Description
        - Video
        - Status: Published, Coming Soon, Draft
'''

class AccessRequirement(models.TextChoices):
    ANYONE = "anyone", "Anyone"
    EMAIL_REQUIRED = "email","Email required"

class PublishStatus(models.TextChoices):
    PUBLISHED = "published","Published"
    COMING_SOON = "soon","Coming soon"
    DRAFT = "draft","Draft"
    
def handle_upload(instance, filename):
    return f"{filename}"
class Course(models.Model): 
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=handle_upload, blank=True, null=True) 
    access =models.CharField(
        max_length=10,
        choices = AccessRequirement.choices,
        default= AccessRequirement.EMAIL_REQUIRED
         
    ) 
    
    status = models.CharField(
        max_length=20, 
        choices=PublishStatus.choices,
        default= PublishStatus.DRAFT, 
    ) 
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED
    
    
class Lesson(models.Model):
    pass