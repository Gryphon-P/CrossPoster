import pytumblr


def makeTumblrPost(
        _customer_key,
        _consumer_secret,
        _oauth_token,
        _oauth_secret,
        _blog_url,
        _tags: list[str],
        _tweet: str,
        _image_directory
        ):

    # Creates a tumblr client in order to make posts
    tumblr_client = pytumblr.TumblrRestClient(
        '<consumer_key>',
        '<consumer_secret>',
        '<oauth_token>',
        '<oauth_secret>',
    )

    # Pulls info about the user
    client_info = tumblr_client.info()

    # Creates a post
    tumblr_client.create_photo(
        blogname=_blog_url,
        state="published",
        tweet=_tweet,
        source=_image_directory
    )








