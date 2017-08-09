# add all files or filename/folder
git add --all
# add updated files only
git add -u

### SHOW THE DIFF
# know the difference with not staged
git diff
# what will be committed
git diff --staged

### CREATE COMMIT
# use commit message from command line
git commit -m
# change and rewrite existing files
git commit -a
#the same and with comment
git commit -am
# change the message if not pushed
git commit --amend -m "New commit message"
# how to create right commit messages
"
- Separate subject from body with a blank line
- Limit the subject line to 50 characters
- Capitalize the subject line
- Do not end the subject line with a period
- Use the imperative mood in the subject line
- Wrap the body at 72 characters
- Use the body to explain what and why vs. how
"

### WORK WITH BRANCHES
# list both local and remote branches
git branch -a
# list only remote branches
git branch -r
# update list of local branches
git remote update origin --prune
# delete branch
git branch -d $branch_name

### UNDO SOME THINGS
# local update
git add some/changed/file.ext
git commit --amend -m "commit message"
## Undoing local changes
# reset one file to the last committed version
git checkout HEAD file/to/restore.ext
# reset all files
git reset --hard HEAD
## Undoing Committed Changes
# revert commit == reapply some commit one more time, history will be saved
git revert 2b504be
# reset commit == all next commits will be erased, last history will be destroyed
git reset --hard 2be18d9

# if you want use some tool to display diff(meld, for example)
git difftool -y -t meld some_filename
# committed messages by one line
git log --oneline
