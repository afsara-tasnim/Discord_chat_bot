import requests
import json


def get_qoute():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    print(type(json_data))
    qoute = json_data[0]['q'] + " -" + json_data[0]['a']
    return (qoute)


def get_data():
    response = requests.get("https://dapi.binance.com/dapi/v1/ticker/24hr")
    json_data = json.load(response.text)
    symbol = json_data['symbol']
    return symbol


def get_poem():
    response = requests.get("https://www.poemist.com/api/v1/randompoems")
    json_data = json.loads(response.text)
    poem = json_data[0]["title"] + "\n" + json_data[0]['content'] + "\n" + " -" + "*" + json_data[0]['poet'][
        'name'] + "*"
    return (poem)


def get_jokes():
    response = requests.get("https://some-random-api.ml/joke")
    json_data = json.loads(response.text)
    joke = json_data['joke']
    return (joke)


def get_fact():
    response = requests.get("https://some-random-api.ml/facts/bird")
    json_data = json.loads(response.text)
    return (json_data)


def get_meme():
    response = requests.get("https://some-random-api.ml/meme")
    json_data = json.loads(response.text)
    meme = json_data['image']
    return (meme)


def get_hugs():
    response = requests.get("https://some-random-api.ml/animu/pat")
    json_data = json.loads(response.text)
    hug = json_data['link']
    return (hug)





