from .markdown import markdown_content_example

chat_conversation_example = [
    {
        "cid": "c1",
        "title": "Hello World1",
        "date": "2023-01-05",
        "conversation": [
            {
                "role": "user",
                "value": "Hello World"
            },
            {
                "role": "assistant",
                "value": "I'm AtomGPT, Can I help you?"
            },
        ]
    },
    {
        "cid": "c2",
        "title": "Hello World2",
        "date": "2024-01-05",
        "conversation": [
            {
                "role": "user",
                "value": "Hello World"
            },
            {
                "role": "assistant",
                "value": markdown_content_example
            },
        ]
    },
    {
        "cid": "c3",
        "title": "Hello World3",
        "date": "2024-01-04",
        "conversation": [
            {
                "role": "user",
                "value": "Hello World2"
            },
            {
                "role": "assistant",
                "value": "I'm AtomGPT, Can I help you?"
            },
        ]
    },
    {
        "cid": "c3",
        "title": "Hello World3",
        "date": "2024-01-01",
        "conversation": [
            {
                "from": "user",
                "value": "Hello World3"
            },
            {
                "from": "assistant",
                "value": "I'm AtomGPT, Can I help you?"
            },
        ]
    },
]
