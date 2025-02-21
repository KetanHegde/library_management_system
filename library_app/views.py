from django.shortcuts import render
from .models import Author,Book,Book_issued,User
from django.db import IntegrityError
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseBadRequest
from django.template.loader import render_to_string


def home_page(request):
    return render(request,'index.html')

def issue_book(request):
    if request.method=="POST":
        book_id = request.POST.get("book_id")
        user_id = request.POST.get("user_id")
        try:
            book = Book.objects.get(book_id = book_id)
        except Book.DoesNotExist:
            return render(request, 'issue.html', {"message":"Book Doesn't exist in Library", "color":"red"})
        try:
            user = User.objects.get(user_id = user_id)
        except User.DoesNotExist:
            return render(request, 'issue.html', {"message":"User Doesn't exist", "color":"red"})
        
        try:
            Book_issued.objects.create(book_id = book, user_id = user)
        except IntegrityError as e:
            return render(request, 'issue.html', {"message":"This Book has already been issued","color":"red"})
        

        recipient_list = [user.user_email]
        subject = "Issue of a Book details"
        authors = Author.objects.filter(book_id=book_id)
        context = {"user":user,"book":book,"authors":authors}
        body_html = render_to_string('issue_email.html', context)
        body_text = render_to_string('issue_email.txt', context)
        try:
            send_mail(
                subject,
                body_text,
                'Ketan Hegde',  
                recipient_list,
                html_message=body_html,
            )
        except BadHeaderError:
            return HttpResponseBadRequest('Invalid header found.')
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")
        return render(request, 'issue.html', {"message":"Issued Successfully","color":"green"})
    return render(request,'issue.html')

def return_book(request):
    if request.method == "GET":
        book_user_id = request.GET.get('search', '')
        if book_user_id:
            if book_user_id.isdigit():
                books_issued = Book_issued.objects.filter(book_id=book_user_id)
                if not books_issued.exists():
                    return render(request, "return.html",{"message":"Book has not been issued to anyone or Invalid Book ID"})
            else:
                books_issued = Book_issued.objects.filter(user_id=book_user_id)
                if not books_issued.exists():
                    return render(request, "return.html",{"message":"User doesn't have any books issued or Invalid User ID"})
            return render(request, 'return.html', {"books_issued":books_issued})
        return render(request, 'return.html')
    if request.method == "POST":
        book_id = request.POST.getlist("checked")
        book_issued = []
        for bid in book_id:
            book_issued.append(Book_issued.objects.get(book_id=bid))
        try:
            user = User.objects.get(user_id = book_issued[0].user_id_id)
        except Exception as e:
            return render(request,'return.html') 
        # book_issued.delete()
        books_list = []
        for b in book_issued:
            book_object = b.book_id
            books_list.append(book_object)
            b.delete()
        recipient_list = [user.user_email]
        subject = "Return of Books details"
        book_with_authors = []
        for book in books_list:
            book_with_authors.append({"book":book,"authors":Author.objects.filter(book_id=book.book_id)})
        context = {"user":user,"book_with_authors":book_with_authors}
        body_html = render_to_string('return_email.html', context)
        body_text = render_to_string('return_email.txt', context)
        try:
            send_mail(
                subject,
                body_text,
                'Ketan Hegde',  
                recipient_list,
                html_message=body_html,
            )
        except BadHeaderError:
            return HttpResponseBadRequest('Invalid header found.')
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")
        return render(request, "return.html",{"smessage":"Books have been returned Successfully"})
    return render(request,'return.html')

def add_book(request):
    if request.method=="POST":
        title = request.POST.get("title")
        publishername = request.POST.get("publishername")
        publishyear = request.POST.get("publishyear")
        author_list = request.POST.get("authors")
        book = Book.objects.create(book_title=title,publisher_name=publishername,pub_year = publishyear)
        for author in author_list.split(", "):
            Author.objects.create(book_id = book, author_name = author)
        return render(request, 'add_book.html', {"message":"New Book Data has been Inserted Successfully"})
    return render(request,'add_book.html')

def add_user(request):
    if request.method == "POST":
        userid = request.POST.get("userid")
        name = request.POST.get("name")
        number = request.POST.get("number")
        email = request.POST.get("email")
        dob = request.POST.get("dob")
        address = request.POST.get("address")

        # Check if the user already exists with the given user ID
        existing_user = User.objects.filter(user_id=userid).first()
        if existing_user:
            return render(request, 'add_user.html', {"message": "User with this ID already exists.", "color":"red"})

        # If no existing user, create a new user
        User.objects.create(user_id=userid, user_name=name, user_number=number, user_email=email, user_dob=dob, user_address=address)
        
        # Send confirmation email
        recipient_list = [email]
        subject = "Thank You for Registering with us"
        context = {'name': name}
        body_html = render_to_string('email.html', context)
        body_text = render_to_string('email.txt', context)
        
        try:
            send_mail(
                subject,
                body_text,
                'Ketan Hegde',  
                recipient_list,
                html_message=body_html,
            )
        except BadHeaderError:
            return HttpResponseBadRequest('Invalid header found.')
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")

        return render(request, 'add_user.html', {"message": "New User Data has been Inserted Successfully"})

    return render(request, 'add_user.html')

def user_info(request):
    if request.method == "GET":
        query = request.GET.get('search', '')
        if query:
            sb = User.objects.filter(user_id__icontains=query)
            if sb.exists():    
                return render(request, 'user_info.html', {"sb": sb})
            else:
                return render(request, 'user_info.html', {"flag": True})
    return render(request,'user_info.html')

                  
def book_info(request):
    ba = {}
    if request.method == "GET":
        query = request.GET.get('search', '')
        if query:
            if query.isdigit():
                sb = Book.objects.filter(book_id=query)
            else:
                sb = Book.objects.filter(book_title__icontains=query)
            if sb.exists():
                for book in sb:
                    authors = Author.objects.filter(book_id=book.book_id)
                    ba[book] = authors
                return render(request, 'book_info.html', {"ba":ba})
            else:
                return render(request, 'book_info.html', {"flag": True})
    return render(request,'book_info.html')
