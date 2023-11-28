mkdir $HOME/.my_posts
cp  main.py $HOME/.my_posts/
cp  read.py $HOME/.my_posts/
mkdir $HOME/.my_posts/LOG
touch $HOME/.my_posts/LOG/post.log

alias mypost="python3 ~/.my_posts/read.py"
echo 'python3 ~/.my_posts/main.py' >> $HOME/.zshrc
echo 'alias mypost="python3 ~/.my_posts/read.py"' >> $HOME/.zshrc
echo "**Installed uccessfully**"