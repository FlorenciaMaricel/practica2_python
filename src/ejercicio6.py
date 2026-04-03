def analisis_hashtag(posts):
    hashtags = {}

    for post in posts:
        palabras = post.split()
        for palabra in palabras:
            if palabra.startswith("#"):
                if palabra in hashtags:
                    hashtags[palabra] += 1
                else:
                    hashtags[palabra] = 1

    trending = {}
    for h, c in hashtags.items():
        if c > 1:
            trending[h] = c

    total_unicos = len(hashtags)

    return trending, total_unicos
