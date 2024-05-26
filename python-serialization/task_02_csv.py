#!/usr/bin/python3
"""json convert csv to json"""
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = []
            for row in csv_reader:
                data.append(row)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
