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

