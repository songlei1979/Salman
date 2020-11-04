from hall.models import Member, Book, Suburb, Loan, Author
from rest_framework import viewsets, permissions
from .serializers import MemberSerializer, BookSerializer, SuburbSerializer, LoanSerializer, AuthorSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MemberSerializer

class BookiewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookSerializer

class SuburbViewSet(viewsets.ModelViewSet):
    queryset = Suburb.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SuburbSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LoanSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AuthorSerializer

