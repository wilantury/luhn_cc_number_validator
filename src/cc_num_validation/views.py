# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import luhn, check_issuer


# Endpoint to validate a credit card number
@api_view(['POST'])
def CardValidation(request):
    cc_number = request.data.get("cc_number")
    isValid = luhn(cc_number)
    if isValid:
        issuer = check_issuer(cc_number)
        if issuer:
            return Response({"Issuer":issuer}, status=status.HTTP_200_OK)
        return Response({"Issuer":"Is not possible to findout he Credit Card Issuer, Altough the CC number is valid"}, status=status.HTTP_200_OK)
    return Response({"Error":"The Credit card number is invalid"}, status=status.HTTP_200_OK)
