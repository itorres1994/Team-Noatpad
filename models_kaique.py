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