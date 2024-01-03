from django.contrib import admin
from . models import Order, Package, Proposal, Review
# Register your models here.
admin.site.register(Order)
admin.site.register(Package)
admin.site.register(Proposal)
admin.site.register(Review)