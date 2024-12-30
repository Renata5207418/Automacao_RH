from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (SampleView, BuscarCurriculoView, DashboardRHView, ManageJobsView, EditVagaView, EditCandidatoView,
                    DeleteCandidatoView, DeleteVagaView, export_to_xlsx, home_view, login_view, logout_view)

urlpatterns = [
    path(
        '',
        home_view,
        name='home'
    ),
    path(
        "index/",
        SampleView.as_view(template_name="index.html"),
        name="index",
    ),
    path(
        "page_2/",
        BuscarCurriculoView.as_view(),
        name="page-2",
    ),
    path(
        "page_3/",
        DashboardRHView.as_view(),
        name="page-3",
    ),
    path(
        "manage_jobs/",
        ManageJobsView.as_view(),
        name="manage-jobs",
    ),
    path(
        "manage_jobs/edit/<int:id>/",
        EditVagaView.as_view(),
        name="edit-vaga",

    ),
    path(
        "edit/<int:id>/",
        EditCandidatoView.as_view(),
        name="edit-candidato",
    ),
    path(
        "edit-vaga/<int:id>/",
        EditVagaView.as_view(),
        name="edit-vaga",
    ),
    path(
        "delete/<int:id>/",
        DeleteCandidatoView.as_view(),
        name="delete-candidato",
    ),
    path(
        "delete-vaga/<int:id>/",
        DeleteVagaView.as_view(),
        name="delete-vaga",
    ),

    path(
        "export_to_xlsx/",
        export_to_xlsx,
        name="export_to_xlsx"
    ),
    path(
        "login/",
        login_view,
        name="login"
    ),
    path(
        "logout/",
        logout_view,
        name="logout"
    ),

] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]) + static(settings.MEDIA_URL,
                                                                                     document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
