MOVIES_DATABASE = {
    "Action": ["Gladiator", "Thor"],
    "Comedy": ["Get Shorty"]
}

MOVIES_DESCRIPTION = {
    "Thor": "The powerful, but arrogant god Thor, is cast out of Asgard to live "
            "amongst humans in Midgard (Earth), where he soon becomes one of their finest defenders.",
    "Gladiator" : "When a Roman General is betrayed, and his family murdered "
                  "by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge."
}

def find_movies_for(user, genres):

    result = []
    for genre in genres:
        result += MOVIES_DATABASE[genre]
    return result


def description_for_movie(movieName):
    return MOVIES_DESCRIPTION[movieName]


