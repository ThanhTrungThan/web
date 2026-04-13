# web
## project implementation steps
### stages 1-3
1. provide url address of product's opinions webpage
2. send request to provided url address
3. if status code is OK (status code = 200), fetch all opinions from requested webpage
4. for all fetched opinions, parse them to extract relevant data
5. chech if there is a next page
6. for all remaining pages, repeat steps 2-5
7. save obtaind opinions

## project inputs
124893467
106545192
32918774
83177636
91869341
100714868
34935197
174881911
26968156
8679864
### prj codes
### opinion structure
|component|name|selector|
|---------|-----|-------|
|opinion ID|opinion_id|[data-entry-id]|
|opinion’s author|author|span.user-post__author-name|
|author’s recommendation|recommendation|span.user-post__author-recomendation > em|
|score expressed in number of stars|score|span.user-post__score-count|
|opinion’s content|content|div.user-post__text|
|list of product advantages|pros|div.review-feature__title--positives ~ div.review-feature__item|
|list of product disadvantages|cons|div.review-feature__title--negatives ~ div.review-feature__item|
|how many users think that opinion was helpful|like|button.vote-yes > span|
|how many users think that opinion was unhelpful|dislike|button.vote-no > span|
|publishing date|public_date|span.user-post__published > time:nth-child(1)|
|purchase date|purchase_date|span.user-post__published > time:nth-child(2)|