


import json
from Config import Config


def read():
    try:
        with open("config.json", encoding="utf-8-sig") as file:
            content:str = file.read()
            as_dict = json.loads(content)
            output:Config = None
            try:
                output = Config(
                    server_uri=as_dict["server_uri"]
                )
            except KeyError as error:
                print(f"the key {error.args[0]} is missing from config.json")
                exit(1)
            return output
    except FileNotFoundError:
        print("config file not found")
        exit(2)
    except json.JSONDecodeError:
        print("could not decode config file")
        exit(3)


if __name__ == "__main__":
    read()