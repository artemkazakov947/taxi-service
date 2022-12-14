from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("taxi:driver-detail", kwargs={'pk': self.pk})


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, related_name="cars")

    def __str__(self):
        return self.model


class Message(models.Model):
    title = models.CharField(max_length=63)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="authors")
    liked = models.ManyToManyField(Driver, related_name="likes", blank=True, default=None)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"Message: {self.text} About: {self.title}" \
               f"from: {self.author}"

    @property
    def nums_of_like(self):
        return self.liked.all().count()


class Like(models.Model):
    LIKE_CHOICES = (
        ("Like", "Like"),
        ("Unlike", "Unlike"),
    )
    post = models.ForeignKey(Message, on_delete=models.CASCADE)
    user = models.ForeignKey(Driver, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default="Like", max_length=10)

    def __str__(self):
        return str(self.post)
