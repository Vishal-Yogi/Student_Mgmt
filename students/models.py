from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)

    maths = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    hindi = models.IntegerField()
    english = models.IntegerField()

    email = models.EmailField()
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"

    @property
    def total_marks(self):
        return self.maths + self.physics + self.chemistry + self.hindi + self.english

    @property
    def percentage(self):
        return round(self.total_marks / 5, 2)

    @property
    def status(self):
        subjects = [self.maths, self.physics, self.chemistry, self.hindi, self.english]
        failed_subjects = sum(1 for marks in subjects if marks < 33)

        if failed_subjects == 0:
            return "Pass"
        elif failed_subjects <= 2:
            return "ATKT"
        else:
            return "Fail"
