from django.db import models

# Create your models here.

class User(models.Model):
    """
    Model representing the User profile.
    """
    fname = models.CharField(max_length=30, help_text="Enter your first name.")
    lname = models.CharField(max_length=30, help_text="Enter your last name.")
    password = models.CharField(max_length=30, help_text="Enter your password.")
    cars = models.ManyToManyField(Car, help_text="Select a car for this User.")
    #email = unique_id
    #phone = unique_id
    #license = add relation
    #insurance
    technician = models.ManyToManyField(Technician, help_text="Select a Technician for this User.")
    #other_info = unique_id
    #settings = unique_id

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.fname + " " + self.lname



class Car(models.Model):
    """
    Model representing the Car profile.
    """
    make = models.CharField(max_length=50, help_text="Enter the make of the car.")
    model = models.CharField(max_length=50, help_text="Enter the model of the car.")
    year = models.IntegerField(max_length=10, help_text="Enter the year of the car.")
    engine_type = models.CharField(max_length=50, help_text="Enter the engine type of the car.")
    repairs = models.CharField(max_length=100, help_text ="Enter the repair if any for the car")
    mileage = models.IntegerField(max_length=15, help_text="Enter the mileage of the car")
    oil_type = models.CharField(max_length=50, help_text="Enter the oil type of the car.")
    color = models.CharField(max_length=50, help_text="Enter the color of the car.")
    registration = models.CharField(max_length=50, help_text="Enter the registration of the car.")
    vin_number = models.IntegerField(max_length = 50, help_text="Enter the vin number of the car")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.year + " " + self.color + " " + self.make + " " + self.model

class Repair(models.Model):
    """
    Model representing the Repair profile.
    """
    name = models.CharField(max_length=200, help_text="Enter the name for the repair.")
    cost = models.IntegerField(max_length=20, help_text="Enter them cost for the repair")
    technician = models.CharField(Technician, help_text="Select the technician for the repair")#double check/unique_id??
    date_made: models.DateField(null=true, blank=false)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Technician(models.Model):
    """
    Model representing the Technician profile .
    """
    fname = models.CharField(max_length=30, help_text="Enter your first name.")
    lname = models.CharField(max_length=30, help_text="Enter your last name.")
    street = models.CharField(max_length=100, help_text="Enter the street adress of the technician.")
    city = models.CharField(max_length=100, help_text="Enter the city of the technician.")
    company = models.CharField(max_length=100, help_text="Enter the company of the technician.")
    other_info = models.ManyToManyField(TechAddedInfo, help_text="Additional Information")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.fname + " " + self.lname + " " + self.company

class TechAddedInfo(models.Model):
    """
    Model representing the Technician Information.
    """
    unique_id = models.ForeignKey(Technician, on_delete=models.CASCADE)#Add unique id to Technician
    infornmation_name = models.CharField(max_length=200, help_text="Information Category")
    infornmation_contents = models.CharField(max_length=200, help_text="Information to Add")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.infornmation_name + " " + self.infornmation_contents

class UserAddedInfo(models.Model):
    """
    Model representing the User Information.
    """
    unique_id = models.ForeignKey(User, on_delete=models.CASCADE) #add unique id to User
    infornmation_name = models.CharField(max_length=200, help_text="Information Category")
    infornmation_contents = models.CharField(max_length=200, help_text="Information to Add")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.infornmation_name + " " + self.infornmation_contents

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

class PhoneTimings(models.Model):
    """
    Model representing the PhoneTimings
    """
    unique_id = models.ForeignKey(Phone, help_text="Select a Phone.")
    timing = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.timing

class EmailTimings(models.Model):
    """
    Model representing the EmailTimings.
    """
    email = models.ForeignKey(Email, help_text="Select a email.")
    timing = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.timing

class Settings(models.Model):
    """
    Model representing the Settings.
    """
    email_timings = models.ForeignKey(EmailTimings, help_text="Select an email timing.")
    phone_timings = models.ForeignKey(PhoneTimings, help_text="Select a phone timing.")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.email_timings+ " " + self.phone_timings

class Email(models.Model):
    """
    Model representing the Email.
    """
    unique_id = models.CharField(max_length=30, help_text="Enter your ID.")
    user =  models.CharField(max_length=30, help_text="Enter your Name.")
    adress = models.EmailField(max_length=254, help_text="Enter your Email.")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.adress
