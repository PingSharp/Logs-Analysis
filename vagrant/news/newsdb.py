#!/usr/bin/python

import psycopg2 as psy


def connect_db():
    databaseName = 'news'
    connectObj = psy.connect(database=databaseName)
    return connectObj


def find_most_popular_articles():
    connectdb = connect_db()
    cursor = connectdb.cursor()
    query = '''select articles.title,count(*) as num from articles left
                   join log on log.path = ('/article/' || articles.slug)
                    group by articles.title order by num desc limit 3;'''
    cursor.execute(query)
    toparticles = cursor.fetchall()
    print("What are the most popular three articles of all time?")
    for article in toparticles:
        print('article:'+article[0])
        print(str(article[1])+" views")
    connectdb.close()


def find_most_popular_article_authors():
    connectdb = connect_db()
    cursor = connectdb.cursor()
    query = '''select authors.name, sub.num from authors,
                    (select articles.author,count(*) as num from articles
                   left join log on log.path =
                    ('/article/' || articles.slug)
                    group by articles.author order by num desc)
                   as sub where sub.author=authors.id;'''
    cursor.execute(query)
    topauthors = cursor.fetchall()
    print("Who are the most popular article authors of all time?")
    for author in topauthors:
        print('author:'+author[0])
        print(str(author[1])+" views")
    connectdb.close()


def find_error_day():
    connectdb = connect_db()
    cursor = connectdb.cursor()
    query = '''select subqr.ntime,subqr.result from (select sub.ntime, (sub.
                    num/subq.sum*100) as result from
                     (select log.time::DATE as ntime, cast(count(*) as float)
                    as num from log where not log.status = '200 OK'
                    group by ntime order by ntime) as sub inner join
                    ( select log.time::DATE as ntime, cast(count(*) as float)
                   as sum from log group by ntime order by ntime )
                    as subq on (sub.ntime=subq.ntime) order by result desc) as
                     subqr where subqr.result>1;'''
    cursor.execute(query)
    errordays = cursor.fetchall()
    print("On which days did more than 1% of requests lead to errors?")
    for day in errordays:
        print(day[0])
        print(':'+str(day[1])[:3]+"%")


if __name__ == '__main__':
    find_most_popular_articles()
    find_most_popular_article_authors()
    find_error_day()
