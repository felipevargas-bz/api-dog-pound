import requests


def get_picture():
    """
    get a picture url from the api
    """
    api_url: str = 'https://dog.ceo/api/breeds/image/random'
    res = requests.get(api_url).json()
    picture: str = res["message"]

    return picture
