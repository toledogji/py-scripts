import os
import json

dir_content = os.listdir('.')
json_files = [doc for doc in dir_content if doc.endswith("json")]
processed = 0

data_file = open("./summary.csv", "w")
data_file.write("username, posts, follows, followers\n")

for doc in json_files:

    with open(doc, "r") as json_file:
        try:
            content = json.loads(json_file.read())
            user_content = content["graphql"]["user"]
            username = user_content["username"]
            posts = user_content["edge_owner_to_timeline_media"]["count"]
            follows = user_content["edge_follow"]["count"]
            followers = user_content["edge_followed_by"]["count"]
            data_file.write(f"{username}, {posts}, {follows}, {followers}")
            processed += 1
            print(f"User {username}: {posts}, {follows}, {followers}\n")
        except json.decoder.JSONDecodeError as err:
            print(f"Could not load json from {doc}... {err}")

print(f"Processed {processed} of {len(json_files)}")