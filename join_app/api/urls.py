from rest_framework import routers
from .view import ContactViewSet, TaskViewSet
router = routers.SimpleRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'tasks', TaskViewSet)
# router.register(r'tasks', TaskViewSet)
urlpatterns = router.urls
