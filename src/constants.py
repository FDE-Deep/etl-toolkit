import requests

from exceptions import RetryableError

RETRYABLE_STATUS_CODE = {429, 500, 502, 503, 504}

RETRYABLE_EXCEPTIONS = (
    RetryableError,
    requests.exceptions.ConnectTimeout,
    requests.exceptions.Timeout,
)
