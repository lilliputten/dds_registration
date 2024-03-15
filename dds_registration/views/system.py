# @module views
# @changed 2024.03.13, 16:09

from django.contrib.sites.models import Site  # To access site properties
from django.shortcuts import render

from django.views.generic import TemplateView

import logging


LOG = logging.getLogger(__name__)


# Misc...


class RobotsView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'

    def get_context_data(self, **kwargs):
        context = super(RobotsView, self).get_context_data(**kwargs)
        context['domain'] = Site.objects.get_current().domain
        return context


# Error pages...


def page403(request, *args, **argv):
    LOG.debug('403 error')
    return render(request, '403.html', {}, status=403)


def page404(request, *args, **argv):
    LOG.debug('404 error')
    return render(request, '404.html', {}, status=404)


def page500(request, *args, **argv):
    LOG.debug('500 error')
    return render(request, '500.html', {}, status=500)


__all__ = [
    RobotsView,
    page403,
    page404,
    page500,
]