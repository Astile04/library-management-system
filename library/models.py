from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13,unique=True)
    published_date = models.DateField()
    available_copies = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"
    