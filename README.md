# scrape-me

### Scrapy Settings

Get your USER-AGENT from here: https://www.whoishostingthis.com/tools/user-agent/

Set `ROBOTSTXT_OBEY = False`

Set `DOWNLOAD_DELAY = 3`, to get more friendlier with the site.

Set `CONCURRENT_REQUESTS = 4`, same for getting familiar with the site.

Enable HTTP Caching, uncomment the code

```
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
```

### Scrapy Advanced Settings

For some sites which don't enable scraping like https://amazon.com
Pass in `USER_AGENT` in settings.

```
scrapy shell "https://www.amazon.com/" -s USER_AGENT="<YOUR-USER-AGENT>"
```

After that view whether the site has been opened or not.

```
view(response)
```

