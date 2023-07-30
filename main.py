import json
import difflib


def get_followers():
    with open("src/raw_data/followers_1.json") as file:
        data = json.loads(file.read())

    list_followers = open("src/final_data/followers.txt", "w")

    for v in data:
        for j in v["string_list_data"]:
            list_followers.write(j["value"])
            list_followers.write("\n")


def get_following():
    with open("src/raw_data/following.json") as file:
        data = json.loads(file.read())

    list_following = open("src/final_data/following.txt", "w")

    for v in data.values():
        for j in v:
            list_following.write(j["string_list_data"][0]["value"])
            list_following.write("\n")


def who_unfollowed():
    with (
        open("src/final_data/followers.txt") as f1,
        open("src/final_data/following.txt") as f2,
    ):
        a = sorted(f1.readlines())
        b = sorted(f2.readlines())

    unfollowers = open("src/final_data/unfollowers.txt", "w")

    diff = difflib.unified_diff(a, b, fromfile="f1.txt", tofile="f2.txt", lineterm="")

    for line in diff:
        if line[0] == "+":
            unfollowers.write(line)
            unfollowers.write("\n")


def run():
    get_followers()
    get_following()
    who_unfollowed()

    with open("src/final_data/unfollowers.txt") as f:
        data = f.read()

    print(data)


if __name__ == "__main__":
    print(run())
