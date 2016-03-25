import json
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DetailView

from .models import Book, Publisher
from .forms import PublisherForm


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'publishers'


class PublisherDetail(DetailView):

    model = Publisher

    def get_context_data(self, **kwargs):
        # We grab the variable pk from the urlpattern
        publisher_id = self.kwargs['pk']

        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.filter(publisher_id=publisher_id)

        return context

def publisher_new(request, template='books/publisher_new.html'):
    if request.method == 'POST':
        form = PublisherForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state_province = form.cleaned_data['state_province']
            publisher = Publisher(name=name, address=address, city=city,
                    state_province=state_province)
            publisher.save()
            return_status = {"success": "Transmission received."}

            return HttpResponse(json.dumps(return_status),
                    content_type='application/json', status=200)

        else:
            errors = form.errors

            return HttpResponse(json.dumps(errors),
                    content_type='application/json', status=400)

    # It's not a post, so just render the blank form.
    else:
        form = PublisherForm()

    return render(request, template, {'form':form})
