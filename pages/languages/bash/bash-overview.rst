.. title: Bash overview
.. slug: bash-overview
.. date: 2019-01-07 20:52:22 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

.. contents:: Contents


Wildcards
=========

- **\*** - represents zero or more characters
- **?** - represents a single character
- **[]** - represents a range of characters

  - ``ls [sv]*`` - looking for a files begins with s or v
  - ``ls *[0-9]*`` - set by using a hyphen
  - ``ls [^a-z]*`` - caret means *not*

Permissions
===========

For files:
- **r** read - you may view the contents of the file.
- **w** write - you may change the contents of the file.
- **x** execute - you may execute or run the file if it is a program or script.

For directories:
- **r** - you have the ability to read the contents of the directory (ie do an ls)
- **w** - you have the ability to write into the directory (ie create files and directories)
- **x** - you have the ability to enter that directory (ie cd)

Set for:

- **u** user
- **g** group
- **o** other
- **a** all

In case octal mask using, each number represent [ugo].

grep/egrep
==========

- **.** (dot) - a single character.
- **?** - the preceding character matches 0 or 1 times only.
- **\*** - the preceding character matches 0 or more times.
- **+** - the preceding character matches 1 or more times.
- **{n}** - the preceding character matches exactly n times.
- **{n,m}** - the preceding character matches at least n times and not more than m times.
- **[agd]** - the character is one of those included within the square brackets.
- **[^agd]** - the character is not one of those included within the square brackets.
- **[c-f]** - the dash within the square brackets operates as a range. In this case it means either the letters c, d, e or f.
- **()** - allows us to group several characters to behave as one.
- **|** (pipe symbol) - the logical OR operation.
- **^** - matches the beginning of the line.
- **$** - matches the end of the line.

flags:

- ``-n`` - display line number as well at the output
- ``-c`` - display quantity of matched lines

Piping and redirection
======================

- ``>`` - STDOUT to a file. ``cat filename > out``
- ``<`` - STDIN from a file. ``wc -l < filename``
- STDIN and STDOUT. ``wc -l < barry.txt > myoutput``
- ``2>`` - redirect STDERR
- ``ls -l > out 2>&1`` redirect STDERR to STDOUT and STDOUT to a file
- ``|`` - pipe. Output of program to the next one. Ex: ``ls | head -3 | tail -1``
- save the output from the command to the variable - ``lines=\`cat $1 | wc -l\```

Foreground and Background Jobs
==============================

- ``program_name &`` - run program in background
- ``ctrl+z`` - pause the current foreground process and move it into the background
- ``jobs`` - show background jobs
- ``fg <job number>`` - return job to foreground

bash[rc, _profile] explanation
==============================

TODO

Commands descriptions
=====================

- **``ls [options] [path]``** - list directory contents
 
  - ``ls -lahF`` - long format, all files, human readable format, files indicators

- **``file [path]``** - determine file type

- **``man <command name>``** - access to manual pages
  
  - ``man -k <search term>`` - find required search term in man pages
  - press ``/`` to start search inside man page and ``n`` to search next result

-   Files manipulations
    
    - **``mkdir [options] <directory>``** - make directories
      
      - ``mkdir -p`` - create parent directories
      - ``mkdir -v`` - verbose output

    - **``rmdir [options] <directory>``** - remove empty directories. Flags similar to ``mkdir`` 

    - **``touch [options] <filename>``** - change file timestamp. Can be used to create blank file

    - **``cp [options] <source> <destination>``** - copy file or directory

      - ``cp -r <source> <destination>`` - copy some folder
      - ``cp -n ...`` - do not overwrite existing file

    - **``mv [options] <source> <destination>``** - move a file or directory

    - **``rm [options] <file>``** - remove vile or directory

      - ``rm -r <directory>`` - remove non empty directory
      - ``rm -i <file>`` - interactive mode
      - ``rm -d <path>`` - remove empty directories

- **``cat [files]``** - concatenate and print files

  - ``cat file1 file2 > out_file`` - concatenate two files

- **``less <file>``** - display file with navigation. ``space`` - next page, ``b`` - previous page

- **``chmod [permissions] [path]``** -- change file modes or Access Control Lists

  - ``chmod g+x`` - add execute permissions to the group
  - ``chmod u-w`` - revoke read permissions for the user
  - ``chmod ug+rx`` - add read and execute permissions to the user and group
  - ``chmod 755`` - all rights for user, read and execute only for group and other
  - ``chmod 644`` - read/write for user, read only for group and other

- Filters

  - **``head [-number of lines to print] [path]``** - display first lines of a file
  - **``tail [-number of lines to print] [path]``** - display the last part of a file
  - **``sort [-options] [path]``** - sort lines of text files
  - **``nl [-options] [path]``** - line numbering filter
    
    - ``nl -s '. ' -w 10`` - add some formating
  
  - **``wc [-options] [path]``** - word, line, character, and byte count
  - **``cut [-options] [path]``** - cut out selected portions of each line of a file
    
    - ``cut -f 1 -d ' '`` - get first column from the file, if columns separated by spaces.
    - ``cut -f 1,2 -d ' '`` - get first and second columns
  
  - **``sed <expression> [path]``** - stream editor. basic expression - ``s/search/replace/g``

    - ``sed 's/oranges/bananas/g' mysampledata.txt`` - replace oranges with bananas
  
  - **uniq [options] [path]** - report or filter out repeated lines in a file
  - **tac [path]** - concatenate and print files in reverse (reversed ``cat``).

- **diff [options] <files>** - compare two files
- **top** - display and update sorted information about processes
- **ps** - process status
- **date** - display current date.

  - ``date +%F`` - display in format year-month-day

- **xargs** - construct argument list(s) and execute utility
- **find** - walk a file hierarchy
  
  - ``find . -type f`` - find all files
  - ``find . -type d`` - find all directories
  - ``find . -size +200M -exec ls -sh {} \`` - find and display all files more than 200M
  - ``find . -mtime -1`` - find all recently changed files

- **tar** - manipulate tape archives

  - ``tar -zcvf mytar.tar.gz *`` - add all files in folder to the archive
  - ``tar -zxvf mytar.tar.gz`` - extract files from archive

- **awk 'pattern { action }'** - pattern-directed scanning and processing language


References
==========

- `The Art of Command Line <https://github.com/jlevy/the-art-of-command-line/blob/master/README.md>`__
- `Bash command explanation(explain shell) <https://explainshell.com/>`__
