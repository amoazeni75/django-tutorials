from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from first_app import models
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'first_app/cbv_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # add your parameters here
        context['insert_me_variable'] = "Hello, I'am from views.py"
        return context


class SchoolListView(ListView):
    model = models.School
    # school_list: when a class inherit from the "ListView" class, it automatically create a
    # dictionary with the name : "mode_name + _ + list" which contains all model instances
    context_object_name = 'schools'  # when you write this line, the above dictionary will rename to what you want


class SchoolDetailVeiw(DetailView):
    model = models.School
    context_object_name = 'school_detail'
    template_name = 'first_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')  # we do not allow the user to change the address of the school
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('first_app:list')
