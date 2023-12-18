from .models import Skill, Profile
from projects.models import Project
from django.db.models import Q


def search_profiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__iexact=search_query)

    users = Profile.objects.distinct().filter(Q(name__icontains=search_query) |
                                              Q(short_info__icontains=search_query) |
                                              Q(skill__in=skills))

    return users, search_query


def search_projects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    projects = Project.objects.distinct().filter(Q(owner__name__icontains=search_query) |
                                                 Q(title__icontains=search_query) |
                                                 Q(description__icontains=search_query))

    return projects, search_query
