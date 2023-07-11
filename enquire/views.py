from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from shared.models import Country
from enquire import serializers
from enquire import models
from sendgrid import SendGridAPIClient
from django.core.mail import send_mail
from rest_framework import permissions


class EnquireList(generics.ListAPIView):
    queryset = models.Enquire.objects.all()
    serializer_class = serializers.EnquireSerializer


class EnquireCreate(generics.CreateAPIView):
    queryset = models.Enquire.objects.all()
    serializer_class = serializers.EnquireSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        form_data = response.data
        country_all = Country.objects.all()
        destinations_country = ", ".join([country.name for country in country_all])
        email = form_data.get("email")

        subject = f"New Enquiry by {form_data.get('first_name').upper()} {form_data.get('last_name')} from Gilead summit holidays"
        send_mail(
            subject,
            f"""
                Dear Recipient,

                I hope this email finds you well. I would like to bring to your attention a new enquiry received through our Gilead Summit Holidays Website. Please find the details below:

                Sender's Information:
                - First Name: {form_data.get("first_name").upper()}
                - Last Name: {form_data.get("last_name")}
                - Email: {form_data.get("email")}
                - Phone Number: {form_data.get("phone_number")}
                - Country: {form_data.get("country")}

                Travel Details:
                - Destination: {destinations_country}
                - Travel Date: {form_data.get("travel_date")}
                - Travel Duration: {form_data.get("travel_duration")}
                - Travel Type: {form_data.get("travel_type")}
                - Number of Adults: {form_data.get("adults")}
                - Number of Children: {form_data.get("children")}
                - Special Requests: {form_data.get("special_request")}

                Please take the necessary steps to respond to this enquiry promptly and provide the sender with the required information or assistance. Kindly ensure that the sender's email and contact details are correctly recorded for effective communication.
                """,
            "gileadsummitholidays@gmail.com",
            ["kevinkevendev@gmail.com", "gileadsummitholidays@gmail.com"],
        )
        return response


class EnquirerDelete(generics.DestroyAPIView):
    queryset = models.Enquire.objects.all()
    serializer_class = serializers.EnquireSerializer


class ContactUsList(generics.ListAPIView):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer


class ContactUsCreate(generics.CreateAPIView):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        form_data = response.data
        email = form_data.get("email")
        subject = f"New Contact from {form_data.get('first_name'.upper())} {form_data.get('last_name')} from Gilead summit holidays"
        send_mail(
            subject,
            f"""
                Dear Recipient,

                I hope this email finds you well. I would like to bring to your attention a new enquiry received through our Gilead website. Please find the details below:

                Sender's Information:
                - First Name: {form_data.get("first_name")}
                - Last Name: {form_data.get("last_name")}
                - Email: {form_data.get("email")}
                - Phone Number: {form_data.get("phone_number")}
                - Country: {form_data.get("country")}

                Message:
                - Message: {form_data.get("message")}

                Please take the necessary steps to respond to this enquiry promptly and provide the sender with the required information or assistance. Kindly ensure that the sender's email and contact details are correctly recorded for effective communication.
                """,
            "gileadsummitholidays@gmail.com",
            ["kevinkevendev@gmail.com", "gileadsummitholidays@gmail.com"],
        )
        return response


class ContactUsRetrieveDelete(generics.RetrieveDestroyAPIView):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer
