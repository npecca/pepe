import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    chat_url = 'https://web.telegram.org/a/#7631205793'
    
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(headless=False, user_data_dir='./userdata')
        page = await browser.new_page()
        await page.goto(chat_url)
        
        
        playbtn = page.locator('//*[@id="MiddleColumn"]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div/button[1]')
        await expect(playbtn).to_be_visible()
        await playbtn.click()
        
        # Wait for the iframe to be available
        await page.wait_for_selector('iframe')
        gframe = page.frame_locator('iframe')
        
        # Locate buttons inside the frame
        getbutn = gframe.locator('//*[@id="ui-bottom"]/a[2]')
        exitbtn = page.locator('//*[@id="portals"]/div[1]/div/div/div[2]/div[1]/div/button[1]')
        await expect(getbutn).to_be_visible()
        await getbutn.click()
        await exitbtn.click()
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())