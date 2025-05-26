from rest_framework.exceptions import APIException


class YouHaveAlreadyRate(APIException):
    status_code = 400
    default_code = "bad_request"
    default_detail = "have already rated this article."
