.. title: Git
.. slug: git
.. date: 2018-08-26 14:33:28 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

Resources:

- `Git cheat sheet <http://files.zeroturnaround.com/pdf/zt_git_cheat_sheet.pdf>`__
- `Another cheat sheet <https://gist.github.com/eashish93/3eca6a90fef1ea6e586b7ec211ff72a5>`__
- `Undoing things <https://www.git-tower.com/learn/git/ebook/en/command-line/advanced-topics/undoing-things>`__

**Installing git repo with pip**

.. code-block::

    pip install -e \
    git+ssh://git@github.com/username/repository@[branch|tag|commit]#egg=common[&subdirectory=dir_name]


**Remove file from git but not from local machine**

.. code-block:: bash

    # for a single file
    git rm --cached file_name

    # for a single directory
    git rm --cached -r directory_name

**Add files to git**

.. code-block:: bash
    
    # add all files or filename/folder
    git add --all
    
    # add updated files only
    git add -u

**Show the diff**

.. code-block:: bash

    # know the difference with not staged
    git diff
    
    # what will be committed
    git diff --staged

**Create a commit**

.. code-block:: bash

    # use commit message from command line
    git commit -m
    
    # change and rewrite existing files
    git commit -a
    
    # the same but with a comment
    git commit -am
    
    # change only the message if commit was not pushed
    git commit --amend -m "New commit message"

**Make right commit messages**

- Separate subject from body with a blank line
- Limit the subject line to 50 characters
- Capitalize the subject line
- Do not end the subject line with a period
- Use the imperative mood in the subject line
- Wrap the body at 72 characters
- Use the body to explain what and why vs. how

**Work with branches**

.. code-block:: bash

    # list both local and remote branches
    git branch -a
    
    # list only remote branches
    git branch -r
    
    # update list of local branches
    git remote update origin --prune
    
    # delete branch
    git branch -d $branch_name

**Revert some things**

.. code-block:: bash

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

**Additional topics**

.. code-block:: bash
    
    # if you want use some tool to display diff(meld, for example)
    git difftool -y -t meld some_filename
    
    # committed messages by one line
    git log --oneline

