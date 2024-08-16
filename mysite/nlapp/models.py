from django.db import models

class Subscriber(models. Model):

    email = models.EmailField(unique=True) # The argument (unique=True) ensures that the same email is not stored twice in the database!
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email