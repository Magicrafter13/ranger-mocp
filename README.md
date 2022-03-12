# ranger-mocp

A plugin for the [ranger](https://ranger.github.io) file manager, that lets you interact with the [MoC](https://moc.daper.net/) audio player.

The plugin adds these commands:
- `:mocp_server`: Start the moc server daemon.
- `:mocp_enqueue`: Add the given file(s) to the queue.
- `:mocp_clear`: Clear the playlist (and exit).
- `:mocp_play`: Start playing from the first item on the playlist.
- `:mocp_playit`: Play the given file(s) without modifying the playlist.
- `:mocp_stop`: Stop playing.
- `:mocp_next`: Play the next song.
- `:mocp_previous`: Play the previous song.
- `:mocp_exit`: Shutdown the moc server daemon.
- `:mocp_pause`: Pause.
- `:mocp_unpause`: Unpause.
- `:mocp_toggle_pause`: Toggle between playing and paused.

## Installation

Clone this repo into the ranger plugins folder.

```bash
cd ~/.config/ranger/plugins/
git clone https://github.com/Magicrafter13/ranger-mocp.git
```

## Usage

Some commands are standalone, while others will use any files you have marked (selected) - for example, `:mocp_playit` or `:mocp_enqueue`.

You can add simple keybinds to `~/.config/ranger/rc.conf` for a quick and easy way to use the commands. Example below:

```
map eq mocp_enqueue
map ec mocp_clear
map ep mocp_play
map el mocp_playit

map es mocp_stop
map ef mocp_next
map er mocp_previous

map eP mocp_pause
map eU mocp_unpause
map eG mocp_toggle_pause
```
