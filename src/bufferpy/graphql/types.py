from abc import ABC
from dataclasses import fields
from typing import Any


class _GraphQLInput(
    ABC
):
    """
    *For internal use only*
    
    GraphQL input base class.
    """

    __graphql_field_map__: dict[str, str] = {}
    """
    A dictionary to map our variables to the
    actual name that the GraphQL API requires.
    """

    def to_graphql(
        self
    ) -> dict[str, Any]:
        """
        Transform the input into a dict for the
        GraphQL query.
        """
        result = {}

        for field in fields(self):
            value = getattr(self, field.name)

            if value is None:
                continue

            graphql_name = self.__graphql_field_map__.get(
                field.name,
                field.name,
            )

            result[graphql_name] = value

        return result