from rest_framework import APIException


class CantFollowYourSelf(APIException):
    status_code = 403
    default_details = "You cant fallow your self."

    default_code = "forbidden"
