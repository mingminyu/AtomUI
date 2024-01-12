from datetime import datetime, timedelta
from .markdown import markdown_content_example

chat_conversations_example = [
    {
        "user": "draven",
        "cid": "164334f0-bc9f-4e4a-9b12-038a201f7387",
        "title": "Greet",
        "date": f"{datetime.now():%Y-%m-%d}",
        "conversation": [
            {
                "role": "user",
                "content": "Hello, Atom"
            },
            {
                "role": "assistant",
                "content": "I'm AtomGPT, Can I help you?"
            },
        ]
    },
    {
        "user": "draven",
        "cid": "b4cba9bc-e26b-4d28-b206-4c26aee5e64f",
        "title": "Chat Markdown",
        "date": f"{datetime.now() + timedelta(days=-1):%Y-%m-%d}",
        "conversation": [
            {
                "role": "user",
                "content": "Hello World"
            },
            {
                "role": "assistant",
                "think": True,
                "content": markdown_content_example
            },
        ]
    },
    {
        "user": "draven",
        "cid": "ab132efb-fac4-46d9-82ec-ae4c283f180b",
        "title": "Chat Pyecharts",
        "date": f"{datetime.now() + timedelta(days=-1):%Y-%m-%d}",
        "conversation": [
            {
                "role": "user",
                "content": "Plotting a graph for atom documents."
            },
            {
                "role": "assistant",
                "think": True,
                "content": ""
            },
        ]
    },
    {
        "user": "draven",
        "cid": "6b101588-755f-48ec-bd40-25e1fa3abf1c",
        "title": "Recent 30 Days",
        "date": f"{datetime.now() + timedelta(days=-20):%Y-%m-%d}",
        "conversation": [
            {
                "role": "user",
                "content": "Hello Atom, what day is it today?"
            },
            {
                "role": "assistant",
                "content": "Today is 2023-12-20"
            },
        ]
    },
]

