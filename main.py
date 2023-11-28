import os
from datetime import datetime, timedelta


post_name = os.popen("hostname -fs").read().strip()

log_file_name = os.path.join(os.path.expanduser("~"), ".my_posts/LOG/post.log")

with open(log_file_name, "r") as log_file:
    existing_lines = log_file.readlines()

two_days_ago = datetime.now() - timedelta(days=2)
filtered_lines = [line for line in existing_lines if datetime.strptime(line.split('<')[1].split('>')[0], '%Y-%m-%d %H:%M:%S') >= two_days_ago]

with open(log_file_name, "w") as log_file:
    log_file.writelines(filtered_lines)

if post_name not in ''.join(filtered_lines):
    with open(log_file_name, "a") as log_file:
        log_file.write(post_name + " <" + datetime.today().strftime('%Y-%m-%d %H:%M:%S') + ">" + "\n")
