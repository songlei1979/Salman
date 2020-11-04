from rest_framework import routers
from .api import MemberViewSet, BookiewSet, SuburbViewSet, LoanViewSet, AuthorViewSet

router = routers.DefaultRouter()
router.register('api/members', MemberViewSet,'Members')
router.register('api/books', BookiewSet,'Books')
router.register('api/suburbs', SuburbViewSet,'Suburbs')
router.register('api/loans', LoanViewSet,'Loans')
router.register('api/authors', AuthorViewSet,'Authors')



urlpatterns = router.urls