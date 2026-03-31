import json
import sys
from urllib.request import urlopen

ALLOWLIST = ['names_of_bots_allowed_in_stream']


# Press the green button in the gutter to run the script.
def main():
    username = sys.argv[1:]
    bot_list = get_bot_list()
    value = check_bot_list(username[0], bot_list)
    return print(value)


def get_bot_list():
    # Use a breakpoint in the code line below to debug your script.
    response = urlopen("https://api.twitchinsights.net/v1/bots/all")
    data_json = json.loads(response.read())['bots']
    # Write bot list to file for debugging purposes
    with open(r'path_to_save_json_file', 'w', encoding='utf-8') as f:
        json.dump(data_json, f, ensure_ascii=False)
    return data_json


def check_bot_list(name, bots):
    for cleared in ALLOWLIST:
        if cleared[0].lower() == name.lower():
            return 0

    for entry in bots:
        if entry[0].lower() == name.lower():
            return 1
    return 0


if __name__ == '__main__':
    main()
