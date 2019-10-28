### MISCELANEOUS COMMANDS
- rp!about: Show bot info
- rp!help [command]: Generate help message

### GENERAL MANAGEMENT COMMANDS
- rp!list [user] [-g|-G] [group(s)]: 
    - List all puppets. If a user is specified, lists that user's puppets. If groups are specified, list puppets only from (-g) or excluding (-G) those groups.
- rp!listg [user]: 
    - List all groups.
- rp!new <name> [shortID] <trigger> [local|global]: Create new puppet with specified shortID
- rp!rm <puppet>: Delete puppet
- rp!newgroup <groupName>: Create group
- rp!delgroup <groupName>: Delete group
- rp!groupadd <puppet> <group>: Assign puppet to group
- rp!grouprm <puppet> <group>: Remove puppet from group
- rp!empty <group(s)>: Empty a group without removing it
- rp!find <query>: Search for puppets/groups

### CONTROL COMMANDS
- rp!toggle [puppet]: 
    - If a puppet is specified, proxies all of the user's messages using the puppet's profile in the current channel. If no puppet is specified, resets behavior so that only messages with triggers will be proxied.
- rp!reset: Clear all puppet toggles.

### PUPPET MODIFICATION COMMANDS
- rp!trig <puppet> <newTrigger>: Change trigger
- rp!name <puppet> <newname>: Change puppet name
- rp!id <puppet> [newID]: Change/set/view puppet shortID
- rp!pic <puppet> [image/url]: Change/view puppet profile picture
- rp!desc <puppet> [description]: Change/view puppet description

### MODERATOR COMMANDS
- rp!setprefix <newPrefix> : Change the bot's command prefix
- rp!setlog [channel] : 
    -Have Puppeteer output a log to the specified channel. If none is specified, defaults to the channel the command was issued in.
- rp!nolog : Stop logging events.
- rp!roomtype [flags] [channel(s)] : 
    - Apply the room flags to the channels specified. If no room flags are specified, shows status of the channel specified (current channel if none is specified).
- rp!ban <user> [time] : 
    - Prevents the specified user from making use of Puppeteer for a specified amount of time (or indefinitely, if no time was specified.)
- rp!unban <user> : No explanation necessary.
- rp!block <user:puppet> [channel(s)|*]: 
    - Prevents a specific puppet from being used in specified channels. Defaults to current channel. Asterisk = all channels.
- rp!unblock <user:puppet> [channel(s)|*] Unblocks a specific puppet from specified channels. Defaults to current channel. Asterisk = all channels.

#### Room flags:
- -i = In-character room. Only proxied messages will be allowed.
- -o = OOC room. No messages will be proxied.
- -n = Neutral room. Both IC and OOC messages will be allowed.

*(i,o, and n flags are mutually exclusive.)*

- -e = Commands are enabled in these channels.
- -d = Commands are disabled in these channels and will be ignored.

*(e and d flags are mutually exclusive.)*