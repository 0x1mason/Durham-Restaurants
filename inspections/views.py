from django.views.generic import ListView, DetailView
from inspections.models import Establishment


class EstablishmentList(ListView):
    model = Establishment
    context_object_name = 'establishments'
    template_name = 'inspections/establishment_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        objects = self.model.objects.all()
        if query:
            objects = objects.filter(premise_name__icontains=query)
        objects = objects.filter(status='ACTIVE', est_type=1)
        objects = objects.order_by('premise_name')
        return objects


class EstablishmentDetail(DetailView):
    model = Establishment
    context_object_name = 'establishment'

    def get_context_data(self, **kwargs):
        context = super(EstablishmentDetail, self).get_context_data(**kwargs)
        establishment = context['establishment']
        context['inspections'] = establishment.inspections.order_by('-insp_date')
        return context
