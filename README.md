# scrape-me

### To download images.

Changes are reflected in books_crawler/items.py, books_crawler/settings.py, and books.py

In items.py

The variable names are very important
If you change it, it wont work

```
    image_urls = scrapy.Field()
    images = scrapy.Field()
```

In settings.py

```
ITEM_PIPELINES = {
   # 'books_crawler.pipelines.BooksCrawlerPipeline': 300,

   # referencing here to default image pipeline offered by scrapy
   'scrapy.pipelines.images.ImagesPipeline': 1,
}
```

It is referencing default image pipeline which is a part of media pipeline.

For more info. Visit: https://doc.scrapy.org/en/latest/topics/media-pipeline.html
