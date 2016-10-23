import csv
import urllib2

def read_stocks():
    finance_url = "http://finance.yahoo.com/d/quotes.csv?s=NFLX+AAPL+GOOG+AMZN+MSFT&f=nabc1p2"
    results = urllib2.urlopen(finance_url)
    csv_reader = csv.reader(results)
    return csv_reader
