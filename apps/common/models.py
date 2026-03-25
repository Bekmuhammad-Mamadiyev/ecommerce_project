from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

extension = {
    'video':['mp4', 'mov'],
    'music':['mp3', 'wav'],
    'image':['jpg', 'jpeg','png'],
    'document':['pdf','docx']
}
class Media(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = 'image', _('Image')
        VIDEO = 'video', _('Video')
        FILE = 'document', _('Document')
        MUSIC = 'music', _('Music')

    file = models.FileField(_('document'), upload_to='media/%Y/%m', validators=[FileExtensionValidator(['jpg', 'jpeg','heif', 'png','pdf','mp3','mp4','docx','wav','mov'])])
    type = models.CharField(_('type'),max_length=30, choices=MediaType.choices)

    def clean(self):
        file_ext = self.file.name.split('.')[-1]
        if self.type in extension and file_ext in extension[self.type]:
            return self.file
        raise ValidationError(_('File extension not allowed'))


    def __str__(self):
        return self.type

class Settings(models.Model):
    home_image = models.ForeignKey(Media, related_name='home_images', on_delete=models.CASCADE)
    home_title = models.CharField(_('home title'), max_length=200)
    home_subtitle = models.CharField(_('home subtitle'), max_length=200)

    def __str__(self):
        return self.home_title

class Country(models.Model):
    name = models.CharField(_('name'), max_length=120)
    code = models.CharField(_('code'), max_length=2)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(_('name'), max_length=150)
    country = models.ForeignKey("Country", related_name='regions', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class OurInstagramStory(models.Model):
    image = models.ForeignKey(Media, related_name='instagram_stories', on_delete=models.CASCADE)
    story_link = models.URLField(_('story link'), max_length=200)

    def __str__(self):
        return self.story_link


class CustomerFeedback(models.Model):
    description = (models.TextField(_('description'), max_length=200))
    rank = models.IntegerField(_('rank'), )
    customer_name = models.CharField(_('customer name'), max_length=200)
    customer_position = models.CharField(_('customer position'), max_length=200)
    customer_image = models.ForeignKey(Media, related_name='customer_images', on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name