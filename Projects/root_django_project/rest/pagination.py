

from rest_framework.pagination import LimitOffsetPagination

# creating own pagination class
class MyLimitOffSetPagination(LimitOffsetPagination):
    # default limit means only 5 data from api
    default_limit = 5




# for more details visit--> https://django-rest-framework.org/api-guide/pagination/