import asyncio
from pyppeteer import launch
import os
import json
from monitoring import monitoring


async def simple_uptime_check():
    browser = await launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
    browser_ws_endpoint = browser.wsEndpoint

    with open(os.path.join(os.getcwd(), 'site-config.json')) as config_file:
        config = json.load(config_file)

    for site_data in config:
        site = site_data['site']
        selector = site_data['selector']
        try:
            await monitoring(site, selector, browser_ws_endpoint)
        except Exception as e:
            print(str(e))

    await browser.close()

asyncio.run(simple_uptime_check())
