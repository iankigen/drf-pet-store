from rest_framework.pagination import PageNumberPagination


class PuppiesPaginantion(PageNumberPagination):
	page_size = 10
