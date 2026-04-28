from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author, Book, Member
from .serializers import AuthorSerializer, BookSerializer, MemberSerializer


@api_view(['GET','POST'])
def book_list_api(request):
    if request.method=='GET':
        books =Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','POST'])
def author_list_api(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','POST'])
def member_list_api(request):

    if request.method=='GET':
        members =Member.objects.all()
        serializer = MemberSerializer(members,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer = MemberSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

@api_view(['GET','PUT','DELETE'])
def book_detail_api(request,pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error':'Book not found'},status=404)
    
    if request.method=='GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method=='DELETE':
        book.delete()
        return Response({'message': 'Book deleted'})

@api_view(['GET','PUT','DELETE'])
def author_detail_api(request,pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response({'error':'Author not found'},status=404)
    
    if request.method=='GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = AuthorSerializer(author,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method=='DELETE':
        author.delete()
        return Response({'message':'author deleted'})

@api_view(['GET','PUT','DELETE'])
def member_detail_api(request,pk):
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return Response({'error':'member not found'},status=404)
    
    if request.method=='GET':
        serializer = MemberSerializer(member)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer = MemberSerializer(member,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method=='DELETE':
        member.delete()
        return Response({'message':'member deleted'})