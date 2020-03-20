from django.db import models


class TodoApp(models.Model):
    # id: int
    reminder = models.CharField(max_length=50)
    alarm_time = models.DateTimeField()
    reason = models.TextField(default='null')
    start_time = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.reminder)

    class Meta:
        verbose_name_plural = "List of Todo Items"
