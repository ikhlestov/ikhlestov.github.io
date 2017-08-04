.. title: MakeFiles
.. slug: makefiles
.. date: 2017-08-04 14:56:23 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

Defining the variables. Note: pathes should be provided without quotes!

.. code-block:: make

    MAIN_DIR := training
    TRAIN_DIR := $(MAIN_DIR)/train/$(PROJECT_NAME)_$(RUN)

    ifdef HANDLED_CHECKPOINT
        LATEST_CHECKPOINT = $(HANDLED_CHECKPOINT)
    else
        LATEST_CHECKPOINT = $(shell $(GET_LATEST_CHECKPOINT))
    endif

execute shell command

.. code-block:: make

    GET_LATEST_CHECKPOINT = find $(TRAIN_DIR) -name 'model*' | awk -F '.' '{print $$2}' | awk -F '-' '{print $$2}' | sort -g | tail -n 1
    LATEST_CHECKPOINT = $(shell $(GET_LATEST_CHECKPOINT))

define some commands

.. code-block:: make

    # merge command together
    clean-all: clean-train clean-val

    clean-train:
        rm -rf $(TRAIN_DIR)/*

    clean-val:
        rm -rf $(EVAL_DIR)/*

set environment variables

.. code-block:: make

    CUDA_VISIBLE_DEVICES=$(TRAIN_CUDA) python train.py
