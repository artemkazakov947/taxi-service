from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    DriverListView,
    DriverDetailView,
    DriverCreateView,
    DriverLicenseUpdateView,
    DriverDeleteView,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    toggle_assign_to_car,
    MessageListView,
    MessageCreateView,
    header_about,
    header_contacts,
    MessageDetailView,
    like_message,
)

urlpatterns = [
    path("", index, name="index"),
    path("about/", header_about, name="about"),
    path("contacts/", header_contacts, name="contacts"),

    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer-list"),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update",
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete",
    ),

    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/create/", CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("cars/<int:pk>/toggle-assign/", toggle_assign_to_car, name="toggle-car-assign"),

    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/create/", DriverCreateView.as_view(), name="driver-create"),
    path(
        "drivers/<int:pk>/update/",
        DriverLicenseUpdateView.as_view(),
        name="driver-update",
    ),
    path("drivers/<int:pk>/delete/", DriverDeleteView.as_view(), name="driver-delete"),
    path("review/", MessageListView.as_view(), name="message-list"),
    path("review/like/", like_message, name="message-like"),
    path("review/create/", MessageCreateView.as_view(), name="message-create"),
    path("review/<int:pk>/", MessageDetailView.as_view(), name="message-detail")
]

app_name = "taxi"
