from django.db import models

# Create your models here.

class Firstname(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    created = models.DateTimeField("data created")
    

class Lastname(models.Model):
    def __str__(self):
        return self.lastname
    lastname = models.CharField(max_length=50)                            # kitap adi
    created = models.DateTimeField("data created")                    # olusturma tarihi
    firstname = models.ForeignKey(Firstname, on_delete = models.CASCADE)     # burada foreign key ilk isim olarak tanimlandi. Bu silinince butun bilgiler silinecek


class Phonenumber(models.Model):
    def __str__(self):
        return self.number
    number = models.CharField(max_length=50)                            # kitap adi
    created = models.DateTimeField("data created")                    # olusturma tarihi
    firstname = models.ForeignKey(Firstname, on_delete = models.CASCADE)     # burada foreign key ilk isim olarak tanimlandi. Bu silinince butun bilgiler silinecek
    phone = models.DecimalField(decimal_places=1, max_digits=10, null=True)

class Email(models.Model):
    def __str__(self):
        return self.email
    email = models.CharField(max_length=50)                            # kitap adi
    created = models.DateTimeField("data created")                    # olusturma tarihi
    firstname = models.ForeignKey(Firstname, on_delete = models.CASCADE)     # burada foreign key ilk isim olarak tanimlandi. Bu silinince butun bilgiler silinecek

class Yourmessage(models.Model):
    def __str__(self):
        return self.message
    message = models.CharField(max_length=50)                            # kitap adi
    created = models.DateTimeField("data created")                    # olusturma tarihi
    firstname = models.ForeignKey(Firstname, on_delete = models.CASCADE)     # burada foreign key ilk isim olarak tanimlandi. Bu silinince butun bilgiler silinecek

