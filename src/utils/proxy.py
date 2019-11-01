"""
Various utility functions related to proxying messages.
"""
# Third Party Imports
from discord import TextChannel, Webhook, Guild


async def get_webhook(channel: TextChannel, server: Guild) -> Webhook:
    """Get a webhook for a channel in order to send a proxy."""
    webhooks = await channel.webhooks()
    wh: Webhook
    for webhook in webhooks:
        if webhook.channel in [wh.channel for wh in await server.webhooks()]:
            wh = webhook
            break
    else:
        wh = await channel.create_webhook(name="Puppeteer Proxier!")
    return wh
