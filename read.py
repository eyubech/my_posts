import os

log_file_name = os.path.join(os.path.expanduser("~"), ".my_posts/LOG/post.log")

with open(log_file_name, "r") as log_file:
    lines = log_file.readlines()

print(f"\033[1;35;40mYou have logged in the past 2 days in the posts:")
for line in lines:
    hostname_output = line.split('<')[0].strip()
    print(f"\033[1;32;40m{hostname_output}")
