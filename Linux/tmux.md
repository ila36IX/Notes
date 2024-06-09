To use `tmux`, you'll need to know some important commands and key bindings. Here are the most useful ones:

**Commands:**

1. `tmux` - Start a new tmux session.
2. `tmux new -s session_name` - Start a new tmux session with a specific name.
3. `tmux ls` - List all active tmux sessions.
4. `tmux attach -t session_name -d "commands"` - Attach to an existing tmux session.
5. `tmux kill-session -t session_name` - Kill a specific tmux session.
6. `tmux kill-server` - Kill the tmux server and all sessions.
7. `tmux a -t session_name' enter the emux sesion
8. `tmux new-session -ssession_name -d "command to run"`

**Key Bindings (Prefix + Key):**

The default prefix key in tmux is `Ctrl+b`. You can press this combination and then press another key to trigger a command.

1. `Prefix + c` - Create a new window (tab).
2. `Prefix + n` - Switch to the next window.
3. `Prefix + p` - Switch to the previous window.
4. `Prefix + 0-9` - Switch to the window with the specified number.
5. `Prefix + %` - Split the current window vertically.
6. `Prefix + "` - Split the current window horizontally.
7. `Prefix + o` - Switch to the next pane.
8. `Prefix + ;` - Toggle between the current and previous pane.
9. `Prefix + x` - Close the current pane.
10. `Prefix + z` - Toggle zoom for the current pane (maximize/restore).
11. `Prefix + d` - Detach from the current session (get back to normal terminal).

**Other Useful Key Bindings:**

1. `Prefix + [` - Enter scroll mode (use arrow keys to scroll, `q` to quit).
2. `Prefix + ?` - Show a list of all key bindings.
3. `Prefix + :` - Enter tmux command mode (type commands and press Enter).

You can also customize tmux by creating a `.tmux.conf` file in your home directory and adding your preferred configurations and key bindings.

Note: The `Prefix` key (`Ctrl+b` by default) can be changed by modifying the `set-option -g prefix` setting in your `.tmux.conf` file.