from django.db import models
import uuid
import datetime


# Create your models here.
class TechAddedInfo(models.Model):
    """
    Model representing the Technician Information.
    """
    # unique_id = models.ForeignKey(Technician, on_delete=models.CASCADE) #Add unique id to Technician
    information_name = models.CharField(max_length=200, help_text="Information Category", default="info name")
    information_contents = models.CharField(max_length=200, help_text="Information to Add", default="info content")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.information_name + ": " + self.information_contents


class Technician(models.Model):
    """
    Model representing the Technician profile .
    """
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fname = models.CharField(max_length=30, help_text="Enter technician first name.", blank=False, null=False)
    lname = models.CharField(max_length=30, help_text="Enter technician last name.", blank=False, null=False)
    street = models.CharField(max_length=100, help_text="Enter the street address of the technician.",
                              blank=False, null=False)
    city = models.CharField(max_length=100, help_text="Enter the city of the technician.",
                            blank=False, null=False)
    company = models.CharField(max_length=100, help_text="Enter the company of the technician.", blank=True, null=True)
    other_info = models.ManyToManyField(TechAddedInfo, help_text="Additional Information", blank=True, null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.fname + " " + self.lname


class Car(models.Model):
    """
    Model representing the Car profile.
    """
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    make = models.CharField(max_length=50, help_text="Enter the make of the car.", null=False, default="make")
    model = models.CharField(max_length=50, help_text="Enter the model of the car.", null=False, default="model")
    year = models.IntegerField(max_length=10, help_text="Enter the year of the car.", null=False, default=1)
    engine_type = models.CharField(max_length=50, help_text="Enter the engine type of the car.", null=True)
    # repairs = models.ForeignKey(Repair, on_delete=models.CASCADE, blank=True, null=True)
    mileage = models.IntegerField(max_length=15, help_text="Enter the mileage of the car", null=True)
    oil_type = models.CharField(max_length=50, help_text="Enter the oil type of the car.", null=True)
    color = models.CharField(max_length=50, help_text="Enter the color of the car.", null=False, default="color")
    registration = models.CharField(max_length=50, help_text="Enter the registration of the car.",
                                    blank=True, null=True)
    vin_number = models.CharField(max_length=50, help_text="Enter the vin number of the car", null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.year) + " " + str(self.color) + " " + str(self.make) + " " + str(self.model)


class Repair(models.Model):
    """
    Model representing the Repair profile.
    """
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, help_text="Enter the name for the repair.")
    cost = models.CharField(max_length=20, help_text="Enter them cost for the repair")
    technician = models.ForeignKey(Technician, help_text="Select the technician for the repair", blank=True, null=True)
    car = models.ForeignKey(Car, blank=False, help_text="Select the car that was repaired")
    date_made = models.DateField(null=False, blank=False, default=datetime.date.today())

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name + ": " + self.cost


class UserAddedInfo(models.Model):
    """
    Model representing the User Information.
    """
    information_name = models.CharField(max_length=200, help_text="Information Category", default="info name")
    information_contents = models.CharField(max_length=200, help_text="Information to Add", default="info content")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.information_name + ": " + self.information_contents


class Phone(models.Model):
    """
    Model representing the Phone profile.
    """

    number = models.CharField(primary_key=True, max_length=15,
                              help_text="Enter your phone number.",
                              default="0000000000")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.number


class PhoneTimings(models.Model):
    """
    Model representing the PhoneTimings
    """
    phone = models.ForeignKey(Phone, help_text="Select a Phone.")
    frequency = models.IntegerField(help_text="How many times should you be reminded?", blank=False, default=1)

    TYPE = (
        ('w', 'Weeks Before'),
        ('d', 'Days Before'),
    )

    reminder = models.CharField(max_length=1, choices=TYPE, blank=True, default='w', help_text="Alert Type")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.phone.__str__() + ": " + self.reminder


class Email(models.Model):
    """
    Model representing the Email.
    """

    # user = models.CharField(max_length=30, help_text="Enter your Name.")
    address = models.EmailField(primary_key=True, max_length=254,
                                help_text="Enter your Email.",
                                default="you@example.com")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.address


class EmailTimings(models.Model):
    """
    Model representing the EmailTimings.
    """
    email = models.ForeignKey(Email, help_text="Select an email.")
    frequency = models.IntegerField(help_text="How many times should you be reminded?", blank=False, default=1)

    TYPE = (
        ('w', 'Weeks Before'),
        ('d', 'Days Before'),
    )

    reminder = models.CharField(max_length=1, choices=TYPE, blank=True, default='w', help_text="Alert Type")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.email.__str__() + ": " + self.reminder


class Settings(models.Model):
    """
    Model representing the Settings.
    """
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.ForeignKey(Email, help_text="Select an email")
    phone = models.ForeignKey(Phone, help_text="Select a phone")
    # email_timings = models.ForeignKey(EmailTimings, help_text="Select an email timing.")
    # phone_timings = models.ForeignKey(PhoneTimings, help_text="Select a phone timing.")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.email.__str__() + ", " + self.phone.__str__()


class Notifications(models.Model):
    """
    Model representing the notifications page.
    """
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email_timings = models.ManyToManyField(PhoneTimings, help_text="When should you be notified via email?")
    phone_timings = models.ManyToManyField(EmailTimings, help_text="When should you be notified via phone?")
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True, blank=False)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.date.__str__() + " - " + self.technician.__str__() + ": " + self.repair.__str__()


class License(models.Model):
    """
    docstring for License.
    """
    license_num = models.CharField(primary_key=True, max_length=50, help_text="Enter your license number")
    license_class = models.CharField(max_length=50, help_text="Enter your license class")
    expiration_date = models.DateField(null=False, blank=False)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.license_num


class Insurance(models.Model):
    """
    Model representing the insurance page."""
    insurance_num = models.CharField(primary_key=True, max_length=30, help_text="Enter your insurance number",
                                     default="Ins. #")
    company = models.CharField(max_length=30, help_text="Enter your company", blank=False, null=True)
    coverage = models.CharField(max_length=30, help_text="Enter your coverage", blank=False, null=True)
    # policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    expiration_date = models.DateField(null=True, blank=False)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.insurance_num


class User(models.Model):
    """
    Model representing the User profile.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fname = models.CharField(max_length=30, help_text="Enter your first name.")
    lname = models.CharField(max_length=30, help_text="Enter your last name.")
    password = models.CharField(max_length=30, help_text="Enter your password.")
    cars = models.ManyToManyField(Car, help_text="Select a car for this User.",
                                  default=True, null=True)
    phone = models.ForeignKey(Phone, help_text="Select a phone for this User.",
                              blank=True, null=True)
    license = models.ForeignKey(License, help_text="Select a license for this User.",
                                blank=True, null=True)
    insurance = models.ForeignKey(Insurance, help_text="Select a insurance for this User.",
                                  blank=True, null=True)
    technician = models.ManyToManyField(Technician, help_text="Select a Technician for this User.",
                                        blank=True, null=True)
    other_info = models.ForeignKey(UserAddedInfo, help_text="Enter user info.", blank=True, null=True)
    settings = models.ForeignKey(Settings, help_text="Select settings")
    notifications = models.ForeignKey(Notifications, help_text="Notifications for this User.",
                                      blank=True, null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.fname + " " + self.lname
