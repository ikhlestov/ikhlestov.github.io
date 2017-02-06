# get the location of the executable link
$ readlink -f /usr/bin/java
/usr/lib/jvm/java-8-oracle/jre/bin/java

# display part of the file
$ cat filename | less
$ tail -200 filename
$ head -200 filename
$ head -n 1000 filename | tail
# display to stdout
$ echo SOMETHING

# get list of all listened ports
$ sudo netstat -peanut

# check free disk space
$ df -h

# check memory every 1 second
$ watch -n 1 free -m

# search recursive by folders
$ grep -r "/api/Profile/active_home_devices" static/

# search by file content
$ grep -R 'GCModel' SemanticProcessor/

# find by filename
$ find ~ -name readme.txt 

# get folder size
$ du -hs

# get folders size inside another one
$ du -h --max-depth=1 some_folder

# sizes of files
$ ls -lah

# as per tutorial: http://manpages.ubuntu.com/manpages/trusty/man1/enca.1.html
# get coding of document
$ enca filename
# change encoding of doc
$ enconv filename

# merge all files in folder to one
$ cat folder_path/* > new_file

# copy content of some text file(ssh for example)
$ cat ~/.ssh/id_rsa.pub | xclip -sel clip

# get source code of some package
http://askubuntu.com/questions/167468/where-can-i-find-the-source-code-of-ubuntu

# get dependencies
$ readelf -d some_exe

# find location of installed files
$ dpkg --listfiles libqt4-dev

# remove range of folders starts with numbers
$ rm -r output/logs/{17..26}*

# unzip tar.gz file
$ tar -xvzf filename.tar.gz

