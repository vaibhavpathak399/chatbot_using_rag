def is_general_chat(query):

    query = query.lower()

    general_patterns = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening",
        "good night",

        "what is your name",
        "who are you",
        "your name",

        "thank you",
        "thanks",

        "how are you",

        "my name is",
        "call me",
        "your name is",

        "okay",
        "ok"
    ]

    return any(
        pattern in query
        for pattern in general_patterns
    )