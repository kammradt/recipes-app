from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls))
]


# In the code above, the router class generates the following URL patterns:
# /recipes/ - Create and Read operations can be performed on this route.
# /recipes/{id} - Read, Update and Delete operations can be performed on this route.
