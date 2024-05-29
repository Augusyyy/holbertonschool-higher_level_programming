#!/usr/bin/python3
"""
Write a basc Python menthod to fetch posts from
https://jsonplaceholder.typicode.com/posts using requests.get().
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Print the status code of the response i.e. Status Code: 200
    Iterate through the parsed JSON data and print out the titles
    of all the posts.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print("Status Code: ", response.status_code)
    if response.status_code == 200:
        list_data = response.json()
        for post in list_data:
            print(post['title'])


def fetch_and_save_posts():
    """
    Print the status code of the response i.e. Status Code:
    :return:
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print("Status Code: ", response.status_code)
    if response.status_code == 200:
        with open("posts.csv", "w") as f:
            titles = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=titles)
            list_data = response.json()
            writer.writeheader()
            for post in list_data:
                writer.writerow({'id':post['id'], 'title': post['title'], 'body': post['body']})
