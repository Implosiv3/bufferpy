from bufferpy.exceptions import AuthenticationError, GraphQLError, NetworkError
from typing import Any, Union

import requests


class GraphQLClient:
    """
    The client that will interact with the new
    GraphQL API that is replacing the old one
    since 2026.
    """

    BASE_URL = 'https://api.buffer.com/'

    def __init__(
        self,
        api_key: str,
        timeout: int = 30,
    ) -> None:
        self._timeout = timeout

        self._session = requests.Session()

        self._session.headers.update(
            {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        )

    def execute(
        self,
        query: str,
        variables: Union[dict[str, Any], None] = None,
    ) -> dict[str, Any]:
        """
        Execute the `query` provided by including the
        `variables` also given.
        """
        payload = {
            'query': query,
            'variables': variables or {},
        }

        try:
            response = self._session.post(
                self.BASE_URL,
                json = payload,
                timeout = self._timeout,
            )
        except requests.RequestException as exc:
            raise NetworkError(str(exc)) from exc

        if response.status_code in (401, 403):
            raise AuthenticationError('Invalid Buffer API key.')

        response.raise_for_status()

        body = response.json()

        if 'errors' in body:
            raise GraphQLError(body['errors'])

        return body['data']