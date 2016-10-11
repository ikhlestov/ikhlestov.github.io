git init
# add all files or filename/folder
git add --all
# add updated files only
git add -u
git status
# know the difference with not staged
git diff
# what will be commited
git diff --staged

#use commit message from command line
git commit -m
#change and revrite existing files
git commit -a
#the same and with comment
git commit -am
# change the message if not pushed
git commit --amend -m "New commit message"

# commited messages by one line
git log --oneline

## how to create right commit messages
"
- Separate subject from body with a blank line
- Limit the subject line to 50 characters
- Capitalize the subject line
- Do not end the subject line with a period
- Use the imperative mood in the subject line
- Wrap the body at 72 characters
- Use the body to explain what and why vs. how
"

# list both local and remote branches
git branch -a
# list only remote branches
git branch -r
# update list of local branches
git remote update origin --prune
# delete branch
git branch -d $branch_name
