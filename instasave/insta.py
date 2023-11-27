import requests
import json


def instagram_download(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
    querystring = {"url": link}
    headers = {
        "X-RapidAPI-Key": "ae4b2aa11emsh2a4092f4bcc150fp169b97jsn8be86c35222c",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    result = json.loads(response.text)
    # print(result)
    dict = {}
    if result["Type"] == "Post-Image":
        dict["type"] = "image"
        dict["media"] = result["media"]
        return dict
    elif result["Type"] == "Post-Video":
        dict["type"] = "video"
        dict["media"] = result["media"]
        return dict
    elif result["Type"] == "Carousel":
        dict["type"] = "carousel"
        dict["media"] = result["media"]
        return dict
    else:
        return "error"
