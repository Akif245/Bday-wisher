import requests

import json

import sys
sys.stdout.reconfigure(encoding='utf-8')


stock_name = "TSLA"
company_name="TESLA_LTD"

stock_end_point="https://www.alphavantage.co/query"
news_end_point="https://newsapi.org/v2/top-headlines"

stock_apikey="BQN7I1SS9QCM4QCF"
news_api_key="9bfd8a3052c442c0afd881487ca0059d"

news_param={
    "apiKey":news_api_key,
    "qInTitle":company_name,
    "language": "en",
    
}




parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol": stock_name,
    "apikey":stock_apikey,
            }


response=requests.get(stock_end_point,params=parameters)
# print(response.json())
data=response.json()["Time Series (Daily)"]
# print(data)
data_list=[value for (key,value) in data.items()]
# print(data_list)
yesterday_data=data_list[0]
# print(yesterday_data)
yes_closing_price=yesterday_data["4. close"]
print(yes_closing_price)
day_before_yesterday_data=data_list[1]
# print(day_before_yesterday_data)
day_before_yesterday_closing=day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing)

difference=abs(float(yes_closing_price)-float(day_before_yesterday_closing))#abs is predifined fun to give positive value
print(difference)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
     up_down = "🔻"

# to get percentage of yes and day before yes

dife_perc=(difference/float(yes_closing_price))*100
print(f"the difference in percentage is {dife_perc} %")


if dife_perc>2:
    news_response=requests.get(news_end_point,params=news_param)
    articles =news_response.json()["articles"]
    print(articles)





# for only 3 articles
# news_list=[value for (key,value) in articles]
news_list = [
    {"title": article["title"], "description": article["description"]}
    for article in articles[:3]
]
# print(news_list[:3])
# news_list = articles[:3]
formatted_articles = [
    f"{stock_name}: {up_down}{dife_perc}%\nHeadline: {article['title']}.\nBrief: {article['description']}"
    for article in news_list
]





clean_text = json.dumps(articles, ensure_ascii=False)  # Convert to readable JSON with Unicode preserved
print(clean_text.encode('ascii', 'ignore').decode())