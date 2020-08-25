#!/usr/bin/env python3
import argparse
import feedparser
import datetime

def get_items(urls):
    result = {}
    # Add the timestamp
    result["date"] = str(datetime.datetime.utcnow())
    result["feeds"] = {}

    for url in urls:
        # Ignore empty urls
        if not url:
            continue
        # Parse items from the url
        feed = feedparser.parse(url)
        items = feed["items"]

        # Remove the key 'published_parsed' which doesn't follow the JSON format
        for item in items:
            item.pop("published_parsed", None)

        # Store the result
        result["feeds"] = {url : items}

    return result


def main():
    description = "Read the feed from urls"

    # Parse the arguments from users
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-u','--urls', nargs='+', required=True)
    args = vars(parser.parse_args())

    # List of urls
    urls = ''.join(args['urls']).split(',')

    items = get_items(urls)
    print(items)


if __name__ == "__main__":
    main()
