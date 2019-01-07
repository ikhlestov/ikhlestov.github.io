.. title: Makefile
.. slug: makefile
.. date: 2018-08-27 19:33:42 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

You can read a lot about makefiles at the `wiki <https://en.wikipedia.org/wiki/Make_(software)#Makefile>`__.

You can dynamically create makefiles with `autoconf <https://en.wikipedia.org/wiki/Autoconf>`__ or `CMake <https://en.wikipedia.org/wiki/CMake>`__.

Defining the variables(macros). Note: path should be provided without quotes.

.. code-block:: make

    MACRO = definition
    MAIN_DIR := training
    TRAIN_DIR := $(MAIN_DIR)/train/$(PROJECT_NAME)_$(RUN)

You can overwrite macros providing it's value to a make call

.. code-block:: bash

    make MACRO="some_new_value"


``ifdef`` and ``ifndef``

.. code-block:: make

    ifdef ENV_VAR
        LOCAL_VAR = $(ENV_VAR)
    else
        LOCAL_VAR = $(shell $(SOME_SHELL_COMMAND))
    endif

execute shell command

.. code-block:: make

    # simple command
    RESULT = `some_command`

    # complex command
    SOME_SHELL_COMMAND = find $(TRAIN_DIR) -name 'model*' | awk -F '.' '{print $$2}' | awk -F '-' '{print $$2}' | sort -g | tail -n 1
    LOCAL_VAR = $(shell $(SOME_SHELL_COMMAND))

define and call commands

.. code-block:: make

    merged_command: command_1 command_2

    command_1:
        rm -rf $(TRAIN_DIR)/*

    command_2:
        rm -rf $(EVAL_DIR)/*

set environment variables

.. code-block:: make

    CUDA_VISIBLE_DEVICES=$(TRAIN_CUDA) python train.py

update one file after another modification

.. code-block:: make

    dependent_file.txt: required.html
        lynx -dump required.html > dependent_file.txt
