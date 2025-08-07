from django.db import models

class SiteStatus(models.Model):
    open_to_work = models.BooleanField(default=True)

    def __str__(self):
        return "Open to Work" if self.open_to_work else "Not Open to Work"




class Project(models.Model):
    STATUS_CHOICES = [
        ('live', 'Live'),
        ('coming_soon', 'Coming Soon'),
    ]

    title = models.CharField(max_length=200)
    image_url = models.URLField(
        max_length=500,
        help_text="Paste the URL of the project image (e.g. hosted on Imgur, Cloudinary, etc.)"
    )
    description = models.TextField()
    tech_stack = models.CharField(
        max_length=300,
        help_text="Comma-separated tech tags (e.g. Django, JavaScript, CSS)"
    )
    live_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='live')

    def __str__(self):
        return self.title



    def tech_tags(self):
        # Split the tech_stack string by commas and strip whitespace
        return [tag.strip() for tag in self.tech_stack.split(',')]

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    learn_more_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
