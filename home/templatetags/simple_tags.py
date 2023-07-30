from django.template import Library
from home.models import Categorie
from home.forms import SubcribtionForm

register = Library()

@register.simple_tag
def global_category():
    categories = Categorie.objects.all()
    return categories

@register.simple_tag
def global_form():
    form = SubcribtionForm()
    return form