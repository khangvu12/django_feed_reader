#!/usr/bin/env python3
import argparse
import feedparser
import datetime
import json


def write_log(path, item):
    try:
        content = json.dumps(item)
        # Append new items to the file
        with open(path, "a") as log_file:
            log_file.write(content)
            log_file.write("\n\n")

    except Exception as e:
        print("Make sure to use absolute path AND the file can be overwritten")


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
    # Parse the arguments from users
    description = "Read the feed from urls"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-u','--urls', nargs='+', required=True)
    parser.add_argument('-p','--path', required=True)
    args = vars(parser.parse_args())

    # List of urls
    urls = ''.join(args['urls']).split(',')

    items = get_items(urls)
    print(items)
    write_log(args['path'], items)

if __name__ == "__main__":
    main()
