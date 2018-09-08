import csv

with open('artikel.csv', encoding="utf-8") as csvfile:
    rawArticles = csv.reader(csvfile, delimiter=',')
    articles = []
    for row in rawArticles:
        articles.append(row[2])

print(articles)