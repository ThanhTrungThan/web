import os
import json
import requests
from bs4 import BeautifulSoup

product_code = input("Provide product code: ")
page = 1
next = True

headers = {
    "Host": "www.ceneo.pl",
    "Cookie": "sv3=1.0_ed234801-3ccc-11f1-8ec8-3829d94f2bb6; urdsc=1; userCeneo=ID=dcb65990-aec1-43c2-b2f4-27be211a6efa",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0"
}

all_opinions = []

while next:
    url = f"https://www.ceneo.pl/{product_code}/opinie-{page}"
    print(url)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        page_dom = BeautifulSoup(response.text, "html.parser")
        opinions = page_dom.select("div.js_product-review:not(.user-post--highlight)")

        for opinion in opinions:

            def get_text(selector):
                element = opinion.select_one(selector)
                return element.text.strip() if element else None

            def get_list(selector):
                elements = opinion.select(selector)
                return [e.text.strip() for e in elements] if elements else []

            single_opinion = {
                "opinion_id": opinion.get("data-entry-id"),
                "author": get_text("span.user-post__author-name"),
                "recommendation": get_text("span.user-post__author-recomendation > em"),
                "stars": get_text("span.user-post__score-count"),
                "content": get_text("div.user-post__text"),
                "pros": get_list("div.review-feature__title--positives ~ div.review-feature__item"),
                "cons": get_list("div.review-feature__title--negatives ~ div.review-feature__item"),
                "useful": get_text("button.vote-yes > span"),
                "useless": get_text("button.vote-no > span"),
                "publish_date": get_text("span.user-post__published > time:nth-child(1)"),
                "purchase_date": get_text("span.user-post__published > time:nth-child(2)")
            }
            all_opinions.append(single_opinion)

        next = True if page_dom.select_one("a.pagination__next-arrow") else False
        page += 1
    else:
        print(f"Error: status code {response.status_code}")
        break

print(f"Successfully extracted {len(all_opinions)} opinions.")

if not os.path.exists("./opinions"):
    os.mkdir("./opinions")

with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)

print(f"Opinions saved to ./opinions/{product_code}.json")