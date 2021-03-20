from django.db import models

# Create your models here.
class projects(models.Model):
    project_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.project_name}"

class sub_projects(models.Model):
    sub_project_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.sub_project_name}"

class HP(models.Model):
    project_hp = models.ForeignKey(projects, on_delete=models.CASCADE, related_name="project")
    sub_project_hp = models.ForeignKey(sub_projects, on_delete=models.CASCADE, related_name="sub_project")
    planned_hours = models.FloatField()
    consumed_hours = models.FloatField()
    consumed_hours_p = models.FloatField()
    total_task = models.IntegerField()
    done_task = models.IntegerField()
    done_task_p = models.FloatField()

    def __str__(self):
        return f"{self.project_hp}, {self.sub_project_hp}, {self.planned_hours}, {self.consumed_hours}, {self.consumed_hours_p}, {self.total_task}, {self.done_task}, {self.done_task_p} "