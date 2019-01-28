.. title: Bash scripting
.. slug: bash-scripting
.. date: 2019-01-07 20:53:13 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

- assign variable ``var_name=value``
- refer a variable ``$var_name``
- ``$0`` - The name of the script.
- ``$1`` - ``$9`` - Any command line arguments given to the script. $1 is the first argument, $2 the second and so on.
- ``$#`` - How many command line arguments were given to the script.
- ``$*`` - All command line arguments.

**if** statements:

.. code-block:: bash

  if [ <some test> ]
  then
    <commands>
  else
    <another>
  fi

**while** loop:

.. code-block:: bash

  while [ <some test> ]
  do
    <commands>
  done

**for** loops:

.. code-block:: bash

  # for value in {1..5}
  for var in <list>
  do
    <commands>
  done

