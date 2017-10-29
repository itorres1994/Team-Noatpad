from django.db import models

# Create your models here.

# class Car(models.Model):
#     """
#     Model representing the Car profile.
#     """
#     make = models.CharField(max_length=50, help_text="Enter the make of the car.")
#     model = models.CharField(max_length=50, help_text="Enter the model of the car.")
#     year = models.IntegerField(max_length=10, help_text="Enter the year of the car.")
#     engine_type = models.CharField(max_length=50, help_text="Enter the engine type of the car.")
#     repairs = models.CharField(max_length=100, help_text ="Enter the repair if any for the car")
#     mileage = models.IntegerField(max_length=15, help_text="Enter the mileage of the car")
#     oil_type = models.CharField(max_length=50, help_text="Enter the oil type of the car.")
#     color = models.CharField(max_length=50, help_text="Enter the color of the car.")
#     registration = models.CharField(max_length=50, help_text="Enter the registration of the car.")
#     vin_number = models.IntegerField(max_length = 50, help_text="Enter the vin number of the car")
#
#     def __str__(self):
#         """
#         String for representing the Model object (in Admin site etc.)
#         """
#         return self.year + " " + self.color + " " + self.make + " " + self.model
#
# class Repair(models.Model):
#     """
#     Model representing the Repair profile.
#     """
#     name = models.CharField(max_length=200, help_text="Enter the name for the repair.")
#     cost = models.IntegerField(max_length=20, help_text="Enter them cost for the repair")
#     technician = models.CharField(Technician, help_text="Select the technician for the repair")#double check/unique_id??
#     date_made: models.DateField(null=True, blank=False)
#
#     def __str__(self):
#         """
#         String for representing the Model object (in Admin site etc.)
#         """
#         return self.name
#
# class Technician(models.Model):
#     """
#     Model representing the Technician profile .
#     """
#     fname = models.CharField(max_length=30, help_text="Enter your first name.")
#     lname = models.CharField(max_length=30, help_text="Enter your last name.")
#     street = models.CharField(max_length=100, help_text="Enter the street adress of the technician.")
#     city = models.CharField(max_length=100, help_text="Enter the city of the technician.")
#     company = models.CharField(max_length=100, help_text="Enter the company of the technician.")
#     other_info = models.ManyToManyField(TechAddedInfo, help_text="Additional Information")
#
#     def __str__(self):
#         """
#         String for representing the Model object (in Admin site etc.)
#         """
#         return self.fname + " " + self.lname + " " + self.company
#
# class TechAddedInfo(models.Model):
#     """
#     Model representing the Technician Information.
#     """
#     unique_id = models.ForeignKey(Technician, on_delete=models.CASCADE)#Add unique id to Technician
#     information_name = models.CharField(max_length=200, help_text="Information Category")
#     information_contents = models.CharField(max_length=200, help_text="Information to Add")
#
#     def __str__(self):
#         """
#         String for representing the Model object (in Admin site etc.)
#         """
#         return self.information_name + " " + self.information_contents
#
# class UserAddedInfo(models.Model):
#     """
#     Model representing the User Information.
#     """
#     unique_id = models.ForeignKey(User, on_delete=models.CASCADE) #add unique id to User
#     information_name = models.CharField(max_length=200, help_text="Information Category")
#     information_contents = models.CharField(max_length=200, help_text="Information to Add")
#
#     def __str__(self):
#         """
#         String for representing the Model object (in Admin site etc.)
#         """
#         return self.information_name + " " + self.information_contents

class Phone(models.Model):
    """
    Model representing the Phone profile.
    """
    unique_id = models.CharField(max_length=30, help_text="Enter your ID.")
    number = models.CharField(max_length=15, help_text="Enter your phone number.")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.number

# class PhoneTimings(models.Model):
#     """
#     Model representing the PhoneTimings
#     """
#     unique_id = models.ForeignKey(Phone, help_text="Select a Phone.")
#     timing = models.DateField(null=True, blank=True)
#
#     def __str__(self):
#         """
#         String for representing the Model object (in Admin site etc.)
#         """
#         return self.timing
#
# class EmailTimings(models.Model):
#     """
#     Model representing the EmailTimings.
#     """
#     email = models.ForeignKey(Email, help_text="Select a email.")
#     timing = models.DateField(null=True, blank=True)
#
#     def __str__(self):
#         """
#         String for representing the Model object (in Admin site etc.)
#         """
#         return self.timing
#
# class Settings(models.Model):
#     """
#     Model representing the Settings.
#     """
#     email_timings = models.ForeignKey(EmailTimings, help_text="Select an email timing.")
#     phone_timings = models.ForeignKey(PhoneTimings, help_text="Select a phone timing.")
#
#     def __str__(self):
#         """
#         String for representing the Model object (in Admin site etc.)
#         """
#         return self.email_timings+ " " + self.phone_timings
#
# class Email(models.Model):
#     """
#     Model representing the Email.
#     """
#     unique_id = models.CharField(max_length=30, help_text="Enter your ID.")
#     user =  models.CharField(max_length=30, help_text="Enter your Name.")
#     address = models.EmailField(max_length=254, help_text="Enter your Email.")
#
#     def __str__(self):
#         """
#         String for representing the Model object (in Admin site etc.)
#         """
#         return self.address
#
# class Notifications(models.Model):
#     """
#     Model representing the notifications page."""
#     email_timings = models.ManyToManyField(PhoneTimings, help_text="When should you be notified?")
#     phone_timings = models.ManyToManyField(EmailTimings, help_text="When should you be notified?")
#     repair = models.ForeignKey(Repair, on_delete=models.CASCADE)
#     date = models.DateField(null=True, blank=False)
#     technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
#
#     def __str__(self):
#         """
#         String for representing the Model object (in Admin site etc.)
#         """
#         return self.repair
#
# class License(object):
#     """
#     docstring for License.
#     """
#     unique_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     license_num = models.CharField(max_length = 50, help_text = "Enter your license number")
#     license_class = models.CharField(max_length = 50, help_text = "Enter your license class")
#     expiration_date = models.DateField(null=False, blank=False)
#
#     def __str__(self):
#         """
#         String for representing the Model object (in Admin site etc.)
#         """
#         return self.license_num
#
# class Insurance(models.Model):
#     """
#     Model representing the insurance page."""
#     unique_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     insurance_num = models.CharField(max_length = 30, help_text = "Enter your insurance number")
#     company= models.CharField(max_length = 30, help_text = "Enter your company")
#     coverage = models.CharField(max_length = 30, help_text = "Enter your coverage")
#     # policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
#     expiration_date = models.DateField(null=True, blank=False)
#
#     def __str__(self):
#         """
#         String for representing the Model object (in Admin site etc.)
#         """
#         return self.insurance_num

# class User(models.Model):
#     """
#     Model representing the User profile.
#     """
#     fname = models.CharField(max_length=30, help_text="Enter your first name.")
#     lname = models.CharField(max_length=30, help_text="Enter your last name.")
#     password = models.CharField(max_length=30, help_text="Enter your password.")
#     cars = models.ManyToManyField(Car, help_text="Select a car for this User.")
#     phone = models.ForeignKey(Phone, help_text="Select a phone for this User.")
#     license = models.ForeignKey(License, help_text="Select a license for this User.")
#     insurance = models.ForeignKey(Insurance, help_text="Select a insurance for this User.")
#     technician = models.ManyToManyField(Technician, help_text="Select a Technician for this User.")
#     other_info = models.ForeignKey(UserAddedInfo, help_text="Enter user info.")
#     settings =  models.ForeignKey(Settings, help_text="Select a phone for this User.")
#     notifications = models.ForeignKey(Notifications, help_text="Notifications for this User.")
#     unique_id = models.CharField(max_length=30, help_text="Enter your ID.")
#
#     def __str__(self):
#         """
#         String for representing the Model object (in Admin site etc.)
#         """
#         return self.fname + " " + self.lname
#


