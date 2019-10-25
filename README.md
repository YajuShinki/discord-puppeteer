Puppeteer Roleplay Manager
======
## A Discord bot for managing roleplay avatars, known as 'puppets'.

**Users will be able to...**
 * Create, list, modify, and delete puppets and groups of puppets.
 * Search for puppets by name and description.
 * Assign optional profile pictures and descriptions to puppets.
   * Change/assign the following puppet attributes: Name, profile picture, description.
 * Post messages as puppets via webhooks, as well as delete one's own puppet messages.
 * Identify the OP of puppet messages.
 * Post as multiple puppets in one message by using multiple triggers.
 * 'Toggle' between characters to continuously post in-character without having to retype triggers.

**Moderators will be able to...**
 * Change Puppeteer's command prefix.
 * Modify and delete other users' puppets.
 * Delete others' puppet messages.
 * Restrict puppet usage on a per-room/per-user basis.
   * Ban users from using puppets permanently, or for a set amount of time.
   * Ban certain puppets from posting in certain rooms.
   * Set rooms as IC-only/OOC-only, and enable/disable commands in specific channels.
 * Have Puppeteer output a log to a channel.

## Creating & Using Puppets
To create a puppet, use `rp!new <name> [shortID] <trigger>`. If your puppet's name contains spaces, enclose it with double quotes. Shorthand IDs can be used instead of a puppet's full name in commands. They are optional, but recommened for puppets with difficult-to-type names (such as those with foreign characters). Finally, specify your trigger at the end.

### What's a Trigger?
A **trigger** is a pattern that lets Puppeteer know which messages are in-character. Each puppet must have a unique trigger. Once Puppeteer detects a message with a trigger, it will delete the original message and proxy it using the profile of the puppet the trigger belongs to.
Triggers are in the format `[prefix]text[suffix]`, that is, all triggers must have the string `text` somewhere, which will be substituted with the actual message text. Here are some examples of triggers in action:

| Trigger      | "Hello, World!" message |
|--------------| ----------------------- |
| `>text`      | `>Hello, World!`        |
| `{text}`     | `{Hello, World!}`       |
| `char1:text` | `char1:Hello, World!`   |

If you ever want to change a puppet's trigger, simply use `rp!trig <puppet> <newtrigger>`.

## Managing Your Puppets
