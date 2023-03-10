from flask import abort

POSTS = {
    "1": {
        "title": "Atomic habits",
        "author": "James Clear",
        "content": "There is a difference between being in motion and taking action."
    },

    "2": {
        "title": "The Compound Effect",
        "author": "Darren Hardy",
        "content": "Making small and smart consistent to yield large results."
    },

    "3": {
        "title": "Self Improvement 101",
        "author": "John C. Maxwell",
        "content": "Making small and smart consistent to yield large results."
    }
}

PEOPLE = {
    "1": {
        "_id": "1",
        "username": "HardyClub",
        "name": "Darren Hardy",
        "bio": "Raising a purposeful community, join the Hardy Club!"
    },

    "2": {
        "_id": "2",
        "username": "JClear",
        "name": "James Clear",
        "bio": "Unlocking the power of habits."
    },

    "3": {
        "_id": "3",
        "username": "JMax",
        "name": "John C. Maxwell",
        "bio": "You should seek to grow and become a great leader."
    }
}

PLACES = {
    "1": {
        "name": "South Island",
        "Location": "New Zealand"
    },

    "2": {
        "name": "London",
        "Location": "England"
    },

    "3": {
        "name": "Tokyo",
        "Location": "Japan"
    }
}

PHONES = {
    "1": {
        "_id": "1",
        "name": "iPhone X",
        "brand": "Apple",
        "store": "Apple retail"
    },

    "2": {
        "_id": "2",
        "name": "Tecno camon 17s",
        "brand": "Tecno",
        "store": "Tecno store"
    },

    "3": {
        "_id": "3",
        "name": "Samsung Z-fold",
        "brand": "Samsung",
        "store": "Galaxy store"
    }
}

# level one
def get_all_posts():
    return list(POSTS.values())

def add_post(posts):
    title = posts.get("title")
    author = posts.get("author")
    content = posts.get("content")

    if title and title not in POSTS:
        POSTS[title] = {
            "title": title,
            "author": author,
            "content": content
        }
        return POSTS[title], 201
    else:
        abort(
            406, f"Post with {title} already exists."
        )

# level one
def get_all_people():
    return list(PEOPLE.values())

def get_one_person(_id):
    if _id in PEOPLE:
        return PEOPLE[_id]
    else:
        abort(
            404, f'Person with {_id} does not exist.'
        )

# level two
def get_all_places():
    return list(PLACES.values())

# level three
def get_all_phones():
    res = list(PHONES.values())
    res.append({"next": "http://127.0.0.1:9000/api/phones/#"})
    return res

# level three
def get_one_phone(__id):
    if __id in PHONES:
        res = [PHONES[__id]]
        res.append({"return": "http://127.0.0.1:9000/api/phones"})
        return res
    else:
        abort(
            404, f'Person with {__id} does not exist.'
        )