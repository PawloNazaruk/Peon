import json
import keyboard
from pprint import pprint


def get_tag_template(path = "template\\tags.json"):
    with open(path, "r") as file_ref:
        raw_data = json.load(file_ref)
        return raw_data

def set_tag_template(tags, path = "template\\tags.json"):
    with open(path, "r+") as file_ref:
        file_ref.seek(0)
        json.dump(dict(tags=tags), file_ref, indent=4, sort_keys=True)
        file_ref.truncate()

def tag_key_exist(tags, dict):
    for tag in tags:
        if dict['name'] == tag['name']:
            return 'exist'
    return None

def tag_exist(tags, dict):
    for tag in tags:
        if dict == tag:
            return 'exist'
    return None

def create_tag(tags, dict):
    if tag_key_exist(tags, dict) == None:
        tags.append(dict)
        keyboard.add_abbreviation(dict["name"], dict["switch_to"])
        print("Tag created.")
        set_tag_template(tags)
    else:
        print("Tag couldn't be created, as is already existing.")

def update_tag(tags, dict, new_dict):
    if tag_exist(tags, dict) != None:
        tags.pop(tags.index(dict))
        if tag_key_exist(tags, new_dict) == None:
            tags.append(new_dict)
            keyboard.add_abbreviation(dict['name'], "Tag will be cleared with the new start of the program.")
            keyboard.add_abbreviation(dict['name'], dict['switch_to'])
            print("Tag was updated.")
            set_tag_template(tags)
        else:
            print("The name of the tag is already used.")
    else:
        print("Tag couldn't be found.")

def delete_tag(tags, dict):
    if tag_exist(tags, dict) != None:
        tags.pop(tags.index(dict))
        keyboard.add_abbreviation(dict['name'], "Tag will be cleared with the new start of a program.")
        print("Tag was deleted.")
        set_tag_template(tags)
    else:
        print("Tag to delete doesn't exist.")

def create_abbreviation_from_file(tags, vars):
    for dict in tags:
        for var in vars:
            for key, val in var.items():
                dict['switch_to'] = dict['switch_to'].replace(key, val)
                keyboard.add_abbreviation(dict['name'], dict['switch_to'])


def main():
    tags = get_tag_template()['tags']
    vars = get_tag_template("template\\vars.json")['vars']
    create_abbreviation_from_file(tags, vars)


    while True:
        continue






if __name__ == "__main__":
    main()