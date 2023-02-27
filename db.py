POSTS = {
    1: {
        "title": "Atomic habits",
        "author": "James Clear",
        "content": "There is a difference between being in motion and taking action."
    },

    2: {
        "title": "The Compound Effect",
        "author": "Darren Hardy",
        "content": "Making small and smart consistent to yield large results."
    },

    3: {
        "title": "Self Improvement 101",
        "author": "John C. Maxwell",
        "content": "Making small and smart consistent to yield large results."
    }
}

PEOPLE = {
    1: {
        "username": "HardyClub",
        "name": "Darren Hardy",
        "bio": "Raising a purposeful community, join the Hardy Club!"
    },

    2: {
        "username": "JClear",
        "name": "James Clear",
        "bio": "Unlocking the power of habits."
    },

    3: {
        "username": "JMax",
        "name": "John C. Maxwell",
        "bio": "You should seek to grow and become a great leader."
    }
}

PLACES = {
    1: {
        "name": "South Island",
        "Location": "New Zealand"
    },

    2: {
        "name": "London",
        "Location": "England"
    },

    3: {
        "name": "Tokyo",
        "Location": "Japan"
    }
}

def get_all_posts():
    return list(POSTS.values())