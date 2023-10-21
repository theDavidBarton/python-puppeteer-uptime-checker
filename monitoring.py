import asyncio
from pyppeteer import connect

async def monitoring(url, selector, browser_ws_endpoint):
    max_retry = 3
    failed = False
    cause = 'unknown error'
    response_code = 'unknown status'

    try:
        browser = await connect(browserWSEndpoint=browser_ws_endpoint)
        page = await browser.newPage()
        await page.setUserAgent('python-puppeteer-uptime-checker')

        for retry in range(1, max_retry + 1):
            try:
                response = await page.goto(url)
                response_code = response.status
                failed = False
                cause = 'unknown error'
                break
            except Exception as e:
                failed = True
                cause = type(e).__name__
                print(f"- {url} retries after {retry} unsuccessful attempt(s)")

        if response_code == 200:
            await page.waitForSelector(selector)
    except Exception as e:
        failed = True
        cause = type(e).__name__

    if failed or response_code != 200:
        failed_message = f"HEALTH CHECK FAILED on {url} with HTTP {response_code} ({cause})"
        print(failed_message)
    else:
        passed_message = f"HEALTH CHECK PASSED on {url} with HTTP {response_code}"
        print(passed_message)

    await page.goto('about:blank')
    await page.close()
    await browser.disconnect()
