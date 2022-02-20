import requests
import json


def get_json_from_site(url):
    """Get dict from site."""
    response = requests.get(url)
    return response.json()


def write_json_data_in_file(file_name, json_data):
    """Write json data in file."""
    with open(file_name, 'w') as f:
        json.dump(json_data, f)


def read_json_data_in_file(file_name):
    """Read json data from file."""
    with open(file_name, 'r') as f:
        return json.load(f)


def main():
    """The main function."""
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    action = input('Where should i get data? (0-from file, 1-from internet)>>>')
    if action == "1":
        """
        If user choose action for getting data from internet. 
        Here, i add data from inet in data_json.json file.
        """
        json_data = get_json_from_site(url)
        write_json_data_in_file('data_json.json', json_data)

        print(f'File was created/updated! Run and choose from file.')
        return

    elif action == "0":
        """If user choose action for getting data from file. Just get data from file, l-logic."""
        json_data = read_json_data_in_file('data_json.json')

        print(json_data)
        return

    else:
        print('You chose a wrong action.')
        return


if __name__ == "__main__":
    """Точка входа нашей программы."""
    main()


