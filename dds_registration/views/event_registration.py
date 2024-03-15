# @module dds_registration/views/event_registration.py
# @changed 2024.03.13, 17:47

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.conf import settings

from functools import reduce
import traceback
import logging

from core.helpers.errors import errorToString

from ..models import (
    Event,
    Registration,
)

from .helpers import (
    event_registration_form,
    show_registration_form_success,
    get_event_registration_context,
)


LOG = logging.getLogger(__name__)


@login_required
def event_registration_new(request: HttpRequest, event_code: str):
    return event_registration_form(
        request,
        event_code=event_code,
        form_template='dds_registration/event_registration_new.html.django',
        success_redirect='event_registration_new_success',
        create_new=True,
    )


@login_required
def event_registration_edit(request: HttpRequest, event_code: str):
    return event_registration_form(
        request,
        event_code=event_code,
        form_template='dds_registration/event_registration_edit.html.django',
        success_redirect='event_registration_edit_success',
    )


@login_required
def event_registration_new_success(request: HttpRequest, event_code: str):
    return show_registration_form_success(
        request, event_code=event_code, template='dds_registration/event_registration_new_success.html.django'
    )


@login_required
def event_registration_edit_success(request: HttpRequest, event_code: str):
    return show_registration_form_success(
        request, event_code=event_code, template='dds_registration/event_registration_edit_success.html.django'
    )


@login_required
def event_registration_invoice(request: HttpRequest, event_code: str):
    # TODO: Generate invoice pdf
    template = 'dds_registration/event_registration_invoice.html.django'
    context = get_event_registration_context(request, event_code)
    return render(request, template, context)


@login_required
def event_registration_payment(request: HttpRequest, event_code: str):
    try:
        # TODO: Place payment link/info here
        template = 'dds_registration/event_registration_payment.html.django'
        context = get_event_registration_context(request, event_code)
        return render(request, template, context)
    except Exception as err:
        sError = errorToString(err, show_stacktrace=False)
        error_text = 'Can not get payment informatin for event "{}": {}'.format(event_code, sError)
        messages.error(request, error_text)
        sTraceback = str(traceback.format_exc())
        debug_data = {
            'event_code': event_code,
            'err': err,
            'traceback': sTraceback,
        }
        LOG.error('%s (redirecting to profile): %s', error_text, debug_data)
        raise Exception(error_text)


__all__ = [
    event_registration_new,
    event_registration_edit,
    event_registration_new_success,
    event_registration_edit_success,
]