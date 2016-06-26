Content
=======
* `Main Commands`_
* `Breakpoints`_
* `Jumps`_
* `Aliases`_

Main Commands
=============

Based on this tutorial: https://pymotw.com/2/pdb/

**enter** - repeat last command

**where(w)** - find out exactly what line is being executed and where on the call stack you are.

**list(l)** - add more context around the current location
**list(l) 5** - display context around required line of code
**list(l) 3, 10** - display from first(3) to last(10) line

**up(u)/down(d)** - move between frames

**args(a)** - print all arguments to the function active in the current frame
**p** - evaluates(print) an expression given as argument and prints the result

.. code-block::

  p output

**pp** - pretty print

.. code-block::

    (Pdb) pp lines
    ['Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec\n',
     'egestas, enim et consectetuer ullamcorper, lectus ligula rutrum leo, a\n',
     'elementum elit tortor eu quam.\n']


**!** - passes to Python interepter to be evaluated.

.. code-block::

    (Pdb) !output='changed value'

    (Pdb) continue
    changed value


**step** - debug step by step

.. code-block::

    (Pdb) step
    --Call--
    > .../pdb_step.py(9)f()
    -> def f(n):


**next** -  command is like step, but does not enter functions called from the statement being executed. 

**until** -  command is like **next**, except it explicitly continues until execution reaches a line in the same function with a line number higher than the current value

**return** -  is another short-cut for bypassing parts of a function. It continues executing until the function is about to execute a return statement, and then it pauses. This gives you time to look at the return value before the function returns.


Breakpoints
===========
**break lineno** - execute untill line number

.. code-block::

    $ python -m pdb pdb_break.py
    > .../pdb_break.py(7)<module>()
    -> def calc(i, n):
    (Pdb) break 11
    Breakpoint 1 at .../pdb_break.py:11

    (Pdb) continue
    i = 0
    j = 0
    i = 1
    j = 5
    > .../pdb_break.py(11)calc()
    -> print 'Positive!'

.. code-block:: 

    (Pdb) break calc  # specify the name of the function as a brackpoint
    (Pdb) break pdb_break.py:11  # remote filename breakpoint


**continue** -  tells the debugger to keep running your program until the next breakpoint

**break** - list of all breakpoints

**disable/enable breakpoint_id** - disable or enable some breakpoint
**clear breakpoint_id** - delete breakpoint entirely

**tbreak** - temporary breakpoint

.. code-block::

    (Pdb) break 9, j>0  # conditional breakpoint
    (Pdb) condition 1 j>0  # add condition to existing breakpoint by id
    (Pdb) ignore 1 2  # Will ignore next 2 crossings of breakpoint 1.
    (Pdb) ignore 1 0  # Will stop next time breakpoint 1 is reached.


**commands** - you can define a series of interpreter commands, including Python statements

.. code-block::

    (Pdb) break 9
    Breakpoint 1 at .../pdb_break.py:9

    (Pdb) commands 1
    (com) print 'debug i =', i
    (com) print 'debug j =', j
    (com) print 'debug n =', n
    (com) end

Jumps
=====
**jump line_no** - jump ahead to line number without incrementing

**run shlex_args** - restart the command 

.. code-block::

    (Pdb) run one two three

Aliases
=======

.. code-block::

    $ python -m pdb pdb_function_arguments.py
    > .../pdb_function_arguments.py(7)<module>()
    -> import pdb
    (Pdb) break 10
    Breakpoint 1 at .../pdb_function_arguments.py:10

    (Pdb) continue
    > .../pdb_function_arguments.py(10)recursive_function()
    -> if n > 0:

    (Pdb) pp locals().keys()
    ['output', 'n']

    (Pdb) alias pl pp locals().keys()

    (Pdb) pl
    ['output', 'n']



**alias** - return list of all aliases

.. code-block::

    (Pdb) alias ph !help(%1)  # alias with ars

    (Pdb) ph locals
    Help on built-in function locals in module __builtin__:
