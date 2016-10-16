import csv
import urllib2

finance_url = "http://finance.yahoo.com/d/quotes.csv?s=AAPL+GOOG+MSFT&f=nab"
results = urllib2.urlopen(finance_url)
csv_reader = csv.reader(results)

for row in csv_reader:
    print row
