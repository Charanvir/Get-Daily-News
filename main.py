import requests
from send_email import send_email
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
url_US_NEWS = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}&language=en"
url_CAN_NEWS = f"https://newsapi.org/v2/top-headlines?country=ca&category=business&apiKey={api_key}&language=en"
urls = [url_US_NEWS, url_CAN_NEWS]

for url in urls:
    request = requests.get(url)
    content = request.json()

    content_type = url.split("country=")
    content_type = content_type[1].split("&")[0]

    message = f"Subject: Today's news {content_type.upper()}" + "\n"

    for article in content["articles"][:20]:
        single_article = f"""

Title: {article["title"]}
Description: {article["description"]}
Source: {article["url"]}
        """
        if article["title"] is not None:
            message = message + single_article

    message = message.encode("utf-8")
    send_email(message)
