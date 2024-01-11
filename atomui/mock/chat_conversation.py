from datetime import datetime, timedelta
from .markdown import markdown_content_example

chat_conversations_example = [
    {
        "user": "draven",
        "cid": "c1",
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
        "cid": "c2",
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
        "cid": "c3",
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
        "cid": "c4",
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

