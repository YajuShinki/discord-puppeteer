This is a list of all the commands available in Puppeteer, along with detailed descriptions of what they do. The default prefix for commands is `!rp`, so to use a command `cmd`, one would type `rp!cmd`. For the sake of brevity, and due to the fact that this prefix can be changed, prefixes are omitted on this page.

# BASIC COMMANDS
## find
Usage: `find <query>`

Get a list of puppets whose description or name match the given query.

Aliases: `search`
## info 
Usage: `info <puppet>`

Show detailed info about the puppet specified.
## list
Usage: `list [user] [-Gg] [group(s)]`

Get a list of all of the puppets the specified user (default: you) has. If the `-g` flag is enabled, shows only puppets in the specified group(s). If the `-G` flag is enabled, shows all puppets except those in the specified group(s).

Aliases: `ls`
## new 
Usage: `new <username> [shortID] <trigger>`

Create a new puppet with the specified username and trigger pattern. If a shortID is specified, assign it to the new puppet.

Aliases: `create`, `register`, `init`
## remove
Usage: `remove <puppet(s)|*>`

Deletes the specified puppet(s). `remove *` deletes all puppets after confirmation.

Aliases: `delete`, `del`, `rm`
# CONTROL COMMANDS
## msgrm (Later version)
Usage: `msgrm [-f] [messageID(s)|range(s)]`

Deletes specified puppet message(s) (default: last sent). If the user is a moderator, asks for confirmation on every message sent by others before deleting, unless the `-f` flag is enabled.

Aliases: `msgdel`, `delmsg`
## toggle (Later version)
Usage: `toggle [-a] [puppet]`

If a puppet is specified, proxies all of the user's messages using the specified puppet's profile in the current channel, or all channels if the `-a` flag is enabled. If no puppet is specified, resets behavior so that only messages with triggers will be proxied.
## whois (Later version)
Usage: `whois [messageID]`

Identify who posted the specified puppet message. (default: last posted)
# PUPPET MANAGEMENT COMMANDS
## desc
Usage: `desc <puppet> [description]`

View or change a puppet's description.

Aliases: `describe`
## id
Usage: `id <puppet> [shortID]`

View or change a puppet's shortID.
## name
Usage: `name <puppet> <newName>`

Change a puppet's name.
## pic
Usage: `pic <puppet> [image/url]`

View or change a puppet's avatar. NOTE: You can also upload an image with the command `pic <puppet>` as a caption.
## trig
Usage: `trig <puppet> [newTrigger]`

View or change a puppet's trigger pattern.

Aliases: `trigger`
# GROUP MANAGEMENT COMMANDS
## groupadd (Later version)
Usage: `groupadd <puppet(s)>,<group>`

Add puppet(s) to the specified group.
## grouprm (Later version)
Usage: `grouprm <puppet(s)|*>,<group|*>`

Remove puppet(s) from the specified group. `grouprm * group` empties a group. `grouprm puppet(s) *` removes puppet(s) from all groups. `grouprm * *` empties all groups. All 3 cases prompt for confirmation.

## newgroup (Later version)
Usage: `newgroup <groupName(s)>`

Create new group(s) with the specified name(s).

Aliases: `mkgroup`, `mkdir`
## rmgroup (Later version)
Usage: `rmgroup <groupName(s)|*>`

Delete group(s) with the specified name(s). Asterisk `rmgroup *` deletes  all groups after confirmation.

Aliases: `delgroup`, `rmdir`
# MODERATOR COMMANDS
## allow (Later version)
Usage: `allow [-t <time>] <user(s)>`

On whitelist servers, grant the specified user(s) permission to use puppets, optionally for only a set amount of time.

Time is formatted using single-letter time units, using `y` for years, `w` for weeks, `d` for days, `h` for hours, and `m` for minutes. Examples: 1 day = `1d` or `24h`, 2weeks = `2w` or `14d`, 36 hours = `36h` or `1d12h`.
## block (Later version)
Usage: `block [-t <time>] <user>`

Prevent specific user(s) from using puppets, optionally for a certain amount of time.
## disallow (Later version)
Usage: `disallow <user(s)>`

On whitelist servers, remove specified user(s) from whitelist.
## log (Later version)
Usage: `log [-n|channelID]`

Assign the specified channel (default: current channel) as the log dump. If flag `-n` is enabled, disables server log output.
## unblock (Later version)
Usage: `unblock <user(s)>`

Removes specified user(s) from the blacklist.
## roomtype (Later version)
Usage: `roomtype [-cCinox] [channelID(s)]`

Change the room type of specific channel(s). If no flags are specified, displays the room type of the specified channel. (default: current channel)

| FLAG | MEANING |
| ---- | --- | 
| `-c` | Listen to commands in this channel. |
| `-C` | Ignore non-moderator commands in this channel. |
| `-i` | Allow only in-character posts. Commands excluded. |
| `-n` | Allow both in-character and out-of-character posts. |
| `-o` | Do not parse any puppet triggers. |
| `-x` | Delete posts with puppet triggers. |

`c/C` and `i/n/o/x` flags are mutually exclusive.

Examples: `roomtype -Ci` prevents commands and only allows in-character posts. `roomtype -c` allows commands. `roomtype -x` disallows messages with triggers.