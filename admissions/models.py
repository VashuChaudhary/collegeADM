from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    seats = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.code})"

class AdmissionApplication(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField()
    
    # Academic Information
    previous_school = models.CharField(max_length=200)
    grade_10_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    grade_12_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    
    # Course Selection
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    # Application Status
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    applied_date = models.DateTimeField(auto_now_add=True)
    
    # Documents
    birth_certificate = models.FileField(upload_to='documents/', null=True)
    marksheet_10 = models.FileField(upload_to='documents/', null=True)
    marksheet_12 = models.FileField(upload_to='documents/', null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course.name}"
