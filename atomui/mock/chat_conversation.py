from .markdown import markdown_content_example

chat_conversations_example = [
    {
        "user": "draven",
        "cid": "c1",
        "title": "Today Chat",
        "date": "2023-01-08",
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
        "user": "draven",
        "cid": "c2",
        "title": "Markdown Display",
        "date": "2024-01-07",
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
        "user": "draven",
        "cid": "c3",
        "title": "Recent 30 Days",
        "date": "2023-12-20",
        "conversation": [
            {
                "role": "user",
                "value": "Hello Atom, what day is it today?"
            },
            {
                "role": "assistant",
                "value": "Today is 2023-12-20"
            },
        ]
    },
    {
        "user": "draven",
        "cid": "c4",
        "title": "Previous 31+ Days",
        "date": "2023-01-01",
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
]

