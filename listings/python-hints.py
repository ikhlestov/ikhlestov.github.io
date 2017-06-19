# ==========================================
# add zeros at the start of string
'22'.zfill(10)
# out: '0000000022'

# ==========================================
# make iterable slice
from itertools import islice
islice(iterable, stop)
islice(iterable, start, stop)
islice(iterable, start, stop, step)

# ==========================================
# write directly to the file
with open('/tmp/filename', 'w') as f:
    # python2
    print >> f, 'some_text'
    # python3
    print("some_text", file=f)

# ==========================================
# try statement
try:
    # something
except:
    # if exception was raised
else:
    # if try was successfully
finally:
    # do this stuff in any case

# ==========================================
# lambda function
f = lambda x: x**2
lambda x: x if (x < 3) else None

# ==========================================
# get input from shell
for line in sys.stdin:
    print("You entered: ", line)
# and after entering required data to the shell press ctrl+D

# ==========================================
# get first and last line of the file
with open("using_python_to_profit") as f:
    first, *_, last = f.readlines()
