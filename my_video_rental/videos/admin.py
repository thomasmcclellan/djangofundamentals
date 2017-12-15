from django.contrib import admin
from . import models
# Register your models here.
# MovieAdmin => name of admin.site.register(models.Movie) + Admin
class MovieAdmin(admin.ModelAdmin):
  fields = ['title','release_year','length']
  # Add search bar => values for what can be found
  search_fields = ['title','length']
  # Add filter for what is shown => values that can be filtered
  list_filter = ['release_year','length']
  # Show which features are displayed without clicking on individual items
  # Values that are shown => the first is a link to edit screen
  list_display = ['title','release_year','length',]
  # Ability to edit field without clicking into edit screen => not recommended if more than one admin
  # list_editable = ['length',]

admin.site.register(models.Customer)
admin.site.register(models.Movie,MovieAdmin)