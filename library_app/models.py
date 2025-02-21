from django.db import models
class Book(models.Model):
    book_id = models.BigAutoField(primary_key=True)
    book_title = models.CharField(max_length=40)
    publisher_name = models.CharField(max_length=30)
    pub_year = models.IntegerField()

class Author(models.Model):
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    author_name = models.CharField(max_length=40)

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=10)
    user_name = models.CharField(max_length=40)
    user_number = models.CharField(max_length=15)
    user_email = models.EmailField()
    user_dob = models.DateField()
    user_address = models.TextField()

class Book_issued(models.Model):
    book_id = models.OneToOneField(Book,primary_key=True,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    date_out = models.DateTimeField(auto_now=True)
