from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Suburb(models.Model):
    SuburbID = models.AutoField(primary_key=True)
    SuburbName = models.CharField(max_length=20, null=False, blank=False)

class Author(models.Model):
    AuthorID = models.AutoField(primary_key=True)
    Lastname = models.CharField(max_length=25, null=False, blank=False)
    Firstname = models.CharField(max_length=25, null=False, blank=False)

class Member(models.Model):
    MemberID = models.AutoField(primary_key=True)
    Lastname = models.CharField(max_length=25, null=False, blank=False)
    Firstname = models.CharField(max_length=25, null=False, blank=False)
    DateOfBirth = models.DateField(null=False, blank=False)
    StreetAddress = models.CharField(max_length=25, null=False, blank=False)
    Suburb = models.ForeignKey(Suburb, on_delete=models.CASCADE, to_field='SuburbID', null=False, blank=False)
    EmailAddress = models.CharField(max_length=30, null=False, blank=False)
    PhoneNumber = models.CharField(max_length=16, null=False, blank=False)
    membertypes = (
        ('Adult', 'Adult'),
        ('Child', 'Child'),
    )
    MembershipType = models.CharField(max_length=5, choices=membertypes, null=False, blank=False)

class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=40, null=False, blank=False)
    NumberOfPages = models.IntegerField(validators=[MaxValueValidator(2000), MinValueValidator(10)], null=False, blank=False)
    DatePulished = models.DateField(null=False, blank=False)
    statusList = (
        ('Available', 'Available'),
        ('Loaned', 'Loaned'),
        ('Damaged', 'Damaged'),
    )
    Status = models.CharField(max_length=9, choices=statusList, null=False, blank=False)
    Notes = models.CharField(max_length=100, choices=statusList, null=True, blank=True)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE, to_field='AuthorID', null=False, blank=False)

class Loan(models.Model):
    loanID = models.AutoField(primary_key=True)
    Member = models.ForeignKey(Member, on_delete=models.CASCADE, to_field='MemberID', null=False, blank=False)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, to_field='BookID', null=False, blank=False)
    LoadDate = models.DateField(null=False, blank=False)


