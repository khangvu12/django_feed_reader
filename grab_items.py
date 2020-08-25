#!/usr/bin/env python3
import argparse
import feedparser

def main():
    description = "Read the feed from urls"

    # Parse the arguments from users
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-u','--urls', nargs='+', required=True)
    args = vars(parser.parse_args())

    # List of urls
    urls = ''.join(args['urls']).split(',')

    for url in urls:
        # Ignore empty url
        if not url:
            continue
        # Parse items from url
        feed = feedparser.parse(url)
        items = feed["items"]

        # Remove published_parsed key which doesn't follow the JSON format
        for item in items:
            item.pop("published_parsed", None)

        print(items)


if __name__ == "__main__":
    main()
