from bufferpy.graphql.types import _GraphQLInput
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Union

import json


# TODO: What is this name (?)
class GraphQLEnum(
    str,
    Enum
):
    """
    A GraphQL as an Enum, serialized without
    quote marks.
    """


def graphql_value(
    value: Any
) -> str:
    if isinstance(value, _GraphQLInput):
        return graphql_object(
            value.to_graphql()
        )

    if value is None:
        return 'null'

    if isinstance(value, GraphQLEnum):
        return value.value

    if isinstance(value, bool):
        return (
            'true'
            if value else
            'false'
        )

    if isinstance(value, (int, float)):
        return str(value)

    if isinstance(value, datetime):
        return graphql_datetime(value)
        # return json.dumps(value.isoformat())

    if isinstance(value, str):
        return json.dumps(value)

    if isinstance(value, list):
        return '[' + ', '.join(
            graphql_value(item)
            for item in value
        ) + ']'

    if isinstance(value, dict):
        return graphql_object(value)

    # TODO: debug, so remove it soon
    print(value)
    raise TypeError(
        f'Unsupported GraphQL value: {type(value).__name__}'
    )


def graphql_object(
    values: Union[dict[str, Any], _GraphQLInput],
) -> str:
    if isinstance(values, _GraphQLInput):
        values = values.to_graphql()

    fields = []

    for key, value in values.items():
        if value is None:
            continue

        fields.append(
            f'{key}: {graphql_value(value)}'
        )

    return '{\n' + ',\n'.join(fields) + '\n}'

def graphql_datetime(
    value: datetime
) -> str:
    if value.tzinfo is None:
        value = value.astimezone()

    value = value.astimezone(timezone.utc)

    return json.dumps(
        value.isoformat(
            timespec = 'milliseconds'
        ).replace('+00:00', 'Z')
    )