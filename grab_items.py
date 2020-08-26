#!/usr/bin/env python3
import argparse
import feedparser
import datetime
import json
import os

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from dotenv import load_dotenv


def add_to_database(items):
    try:
        connection = mysql.connector.connect(host=os.getenv("HOST"),
                                             database=os.getenv("DATABASE"),
                                             user='root',
                                             password=os.getenv("PASSWORD"),
                                             port=os.getenv("PORT"))
        cursor = connection.cursor()

        query = ""

        cursor.execute(query)

        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))

    finally:
        if (connection.is_connected()):
            connection.close()


def write_log(path, items):
    # Remove the key 'published_parsed' which doesn't follow the JSON format
    for url in items['feeds']:
        for item in items['feeds'][url]:
            item.pop("published_parsed", None)

    try:
        content = json.dumps(items)
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

        # Store the result
        result["feeds"] = {url : items}

    return result


def main():
    # Load environment vars from the .env file
    load_dotenv()
    # Parse the arguments from users
    description = "Read the feed from urls"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-u','--urls', nargs='+', required=True)
    parser.add_argument('-p','--path', required=True)
    args = vars(parser.parse_args())

    # List of urls
    urls = ''.join(args['urls']).split(',')

    items = get_items(urls)
    add_to_database(items)

    write_log(args['path'], items)


if __name__ == "__main__":
    main()
