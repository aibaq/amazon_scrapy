### Installation
```
git clone https://aibaq/amazon_scrapy.git
create an environment
pip install -r requirements.txt
```

### Run
```
scrapy crawl main
```
#### In order to prevent ban from Amazon, the following middlewares were added

### User agents middleware (settings.py)
```
'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
```

### Proxy middleware (settings.py)
Add your own proxies to proxy_list.txt
```
'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
```

### List of free proxies
https://free-proxy-list.net/

