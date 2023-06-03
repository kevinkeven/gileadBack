from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from enquire import serializers
from enquire import models
from sendgrid import SendGridAPIClient
from django.core.mail import send_mail


class EnquireList(generics.ListAPIView):
    queryset = models.Enquire.objects.all()
    serializer_class = serializers.EnquireSerializer


class EnquireCreate(generics.CreateAPIView):
    queryset = models.Enquire.objects.all()
    serializer_class = serializers.EnquireSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        form_data = response.data
        firstName = form_data.get("first_name")
        email = form_data.get("email")
        subject = f"New Enquiry by {firstName} from Gilead summit holidays"
        send_mail(
            subject,
            f"""
                Dear Recipient,

                I hope this email finds you well. I would like to bring to your attention a new enquiry received through our Django website. Please find the details below:

                Sender's Information:
                - First Name: {firstName}
                - Last Name: [LatName]
                - Email: [Sender's Email]
                - Phone Number: [Sender's Phone Number]
                - Country: [Sender's Country]

                Travel Details:
                - Destination: [Selected Travel Destinations]
                - Travel Date: [Selected Travel Date]
                - Travel Duration: [Travel Duration in Days]
                - Travel Type: [Selected Travel Type]
                - Number of Adults: [Number of Adults]
                - Number of Children: [Number of Children]
                - Special Requests: [Special Requests or Additional Information]

                Please take the necessary steps to respond to this enquiry promptly and provide the sender with the required information or assistance. Kindly ensure that the sender's email and contact details are correctly recorded for effective communication.
                """,
            "admin@gilead.com",
            [email],
        )
        return response


class EnquirerDelete(generics.DestroyAPIView):
    queryset = models.Enquire.objects.all()
    serializer_class = serializers.EnquireSerializer
