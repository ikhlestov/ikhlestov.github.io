# hadoop was setup with this tutorial
# http://thepowerofdata.io/setting-up-a-apache-hadoop-2-7-single-node-on-ubuntu-14-04/
# to start
$ start-dfs.sh
$ start-yarn.sh
# to check all is running
$ jps
# to stop

# do something with the file
$ hadoop fs -ls /
# move file to HDFS
$ hadoop fs -put filename.txt
# remove file
$ hadoop fs -rm filename.txt
# create dir
$ hadoop fs -mkdir /dirname
# copy file to dir
$ hadoop fs -put filename.txt /dirname
# get to the local disk
$ hadoop fs -get out_file local_filename
# remove folder
$ hadoop fs -rmr /dirname

# run the command (output folder should not exist!)
$ hadoop jar /usr/local/lib/hadoop-2.7.0/share/hadoop/tools/lib/hadoop-streaming-2.7.0.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input /myinput -output /joboutput

# generate test file
$ head -50 hadoop_data/purchases.txt > test_file
# testing whole line
$ cat test_file | ./mapper.py | sort | ./reducer.py
