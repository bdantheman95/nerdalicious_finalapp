from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'nerdalicious_excavate/home.html', context)


def mockup(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'nerdalicious_excavate/mockup.html', context)


def proposal(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'nerdalicious_excavate/proposal.html', context)


def geoproc(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'nerdalicious_excavate/geoproc.html', context)