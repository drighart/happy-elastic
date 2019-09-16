import random
from datetime import datetime
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text, connections, GeoPoint

# Define a default Elasticsearch client
connections.create_connection(hosts=['elasticsearch-master'])

class Article(Document):
    title = Text(analyzer='snowball', fields={'raw': Keyword()})
    body = Text(analyzer='snowball')
    tags = Keyword()
    published_from = Date()
    lines = Integer()
    loc = GeoPoint()

    class Index:
        name = 'blog'
        settings = {
          "number_of_shards": 2,
        }

    def save(self, ** kwargs):
        # self.lines = len(self.body.split())
        return super(Article, self).save(** kwargs)

    def is_published(self):
        return datetime.now() > self.published_from

# create the mappings in elasticsearch
Article.init()

# create and save and article
# article = Article(meta={'id': 42}, title='Hello world!', tags=['test'])
# article.body = ''' looong text '''
# article.published_from = datetime.now()
# article.save()

# article = Article.get(id=42)
# print(article.is_published())

for i in range(100):
    article = Article(meta={'id': i}, title='Hello world nr ' + str(i), tags=['test'])
    article.body = ''' looong text '''
    article.published_from = datetime.now()
    article.lines = random.randint(1,501)
    article.loc = dict(lat=51.9838608 + (random.randint(1,101) * 0.01), lon=5.8755333 + (random.randint(1,101) * 0.01))
    article.save()
