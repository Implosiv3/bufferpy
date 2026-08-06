class BufferException(Exception):
    """
    Base exception for the Buffer client.
    """


class AuthenticationError(BufferException):
    """
    Authentication with the Buffer API failed.
    """


class NetworkError(BufferException):
    """
    A network error occurred while communicating with Buffer.
    """


class GraphQLError(BufferException):
    """
    The GraphQL API returned one or more errors.
    """

    def __init__(
        self,
        errors: list[dict]
    ):
        self.errors = errors

        message = '\n'.join(
            error.get('message', 'Unknown GraphQL error')
            for error in errors
        )

        super().__init__(message)


class ValidationError(BufferException):
    """
    The provided data is not valid.
    """