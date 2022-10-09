# from django import forms
# from django.forms import formset_factory
# from .models import Driver


# drivers = Driver.objects.filter(active=True)

# class PostRaceForm(forms.Form):
#     points = forms.IntegerField(
#         label="points",
#         min_value=0, 
#         max_value=26, 
#         required=False
#         )

# PostRaceFormSet = formset_factory(PostRaceForm)

# formset = PostRaceFormSet()
# for 