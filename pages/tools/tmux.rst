.. title: Tmux
.. slug: tmux
.. date: 2018-08-26 14:30:16 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Illarion Khlestov

When you close ssh session, scripts that were called from ssh user may be closed. To handle this situation you may run scripts under the sudo. Or use tmux. What we should do:

- Connect to VPN, required server ``ssh username@host_ip``
- Install tmux - ``sudo apt-get install tmux``
- Open new tmux session ``tmux new -s session_name``
- Run desired script.
- Detach session with hotkey ``ctrl+b ++ d`` (Means press ``ctrl + b`` first and after the ``d``)
- You may reconnect at this point to the server
- List all tmux session ``tmux ls``
- Connect to chosen session with ``tmux a -t session_name``
- Kill session from itself if not required any more ``ctrl+b ++ x``

Additional notes:

- In case of mouse scrolling not works - inside tmux type ``tmux set-option -g mouse on``
- If you want to be sure that tmux session will not be stopped - you may open new window under the sudo ``sudo tmux new -s window_name`` and after inside change the user ``su - username``
- Here exist quite full `cheat sheet for tmux <https://gist.github.com/MohamedAlaa/2961058>`__
- Copy from tmux screen can be some way inconvinient - so it's better to store output in some file: ``./script_name | tee -a logs.txt``
- In case you want to copy something - you may just highlight by mouse required region, and to past press ``ctrl+b ++ ]``

Tmux is very powerful tool with many other capabilities. For example you may work in one session with your team.
