import datetime
import argparse
from yahoo_earnings_calendar import YahooEarningsCalendar

def parse_arguments():
    parser = argparse.ArgumentParser(description='Earnings Calendar')

    parser.add_argument('tickers_file', help='file contains a list of tickers on each line')
    #parser.add_argument('from_date', help='From date (default: today)')
    #parser.add_argument('duration', help='duration (default: 2weeks)')

    return parser.parse_args()

def read_tickers(tickers_filename):
    tickers = set()
    with open(tickers_filename) as f:
        while True:
            line = f.readline()
            if line == '':
                break
            tickers.add(line.strip())
    return tickers

def main(args):
    tickers = read_tickers(args.tickers_file)

    date_from = datetime.datetime.now()
    date_to = date_from + datetime.timedelta(days=3)
    yec = YahooEarningsCalendar()
    earnings = yec.earnings_between(date_from, date_to)

    for earning in earnings:
        if earning["ticker"] in tickers:
            print("{ticker}\t\t{date}\t\t{timetype}".format(ticker=earning["ticker"], date=earning["startdatetime"], timetype=earning["startdatetimetype"]))


if __name__ == '__main__':
    args = parse_arguments()
    main(args)