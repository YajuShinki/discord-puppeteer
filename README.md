Puppeteer Roleplay Manager
======
## A Discord bot for managing roleplay avatars, known as 'puppets'.

**Users will be able to...**
 * Create, modify, and delete puppets.
 * Post messages as puppets via webhooks, as well as delete one's own puppet messages.
 * Identify the OP of puppet messages.
 * Post as multiple puppets in one message by using multiple triggers.

**Moderators will be able to...**
 * Modify and delete other users' puppets.
 * Restrict puppet usage on a per-room/per-user basis.

## Creating & Using Puppets
To create a puppet, use `rp!new <name> [shortID] <trigger>`. If your puppet's name contains spaces, enclose it with double quotes. Shorthand IDs can be used instead of a puppet's full name in commands. They are optional, but recommened for puppets with difficult-to-type names (such as those with foreign characters). Finally, specify your trigger at the end.

## What's a Trigger?
A **trigger** is a pattern that lets Puppeteer know which messages are in-character. Once Puppeteer detects a message with a trigger, it will delete the original message and send the contents of the message via your avatar.
Triggers are in the format `[prefix]text[suffix]`, that is, all triggers must have the string `text` somewhere. Here are some examples of triggers:

| Trigger      | "Hello, World!" message |
|--------------| ----------------------- |
| `>text`      | `>Hello, World!`        |
| `{text}`     | `{Hello, World!}`       |
| `char1:text` | `char1:Hello, World!`   |

If you ever want to change a puppet's trigger, simply use `rp!trig <puppet> <newtrigger>`.