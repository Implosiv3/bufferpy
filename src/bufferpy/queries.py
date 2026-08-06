from bufferpy.graphql.builder import graphql_object
from bufferpy.inputs import CreatePostInput


def get_account_query(
) -> str:
    return """
query GetAccount {
  account {
    id
    name
    email

    organizations {
      id
      name
      ownerEmail
    }
  }
}
"""


def get_channels_query(
    organization_id: str,
) -> str:
    return f"""
query GetChannels {{
  channels(
    input: {{
      organizationId: "{organization_id}"
    }}
  ) {{
    id
    name
    displayName
    service
    avatar
    isQueuePaused
  }}
}}
"""


def create_post_mutation(
    input_data: CreatePostInput,
) -> str:
    return f"""
mutation CreatePost {{
  createPost(
    input: {graphql_object(input_data)}
  ) {{

    __typename

    ... on MutationError {{
      message
    }}

    ... on PostActionSuccess {{
      post {{
        id
        text
        status
        dueAt

        channel {{
          id
          name
          service
        }}

        assets {{
          id
          type
          source
          mimeType
        }}
      }}
    }}
  }}
}}
"""