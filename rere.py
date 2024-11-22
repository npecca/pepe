import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    chat_url = 'https://web.telegram.org/a/#7631205793'
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state="state.json")
        page = await context.new_page()
        await page.goto(chat_url)
        
        # 
        playbtn = page.locator('//*[@id="MiddleColumn"]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div/button[1]')
        await asyncio.sleep(10)
        await expect(playbtn).to_be_visible()
        await playbtn.click()
        confirm = page.locator('//*[@id="portals"]/div[2]/div/div/div[2]/div[2]/div/button[1]')
        await expect(confirm).to_be_visible()
        await confirm.click()
        # Wait for the iframe to be available
        await page.wait_for_selector('iframe')
        gframe = page.frame_locator('iframe')
        
        # Locate buttons inside the frame
        getbutn = gframe.locator('//*[@id="ui-bottom"]/a[2]')
        # exitbtn = page.locator('//*[@id="portals"]/div[1]/div/div/div[2]/div[1]/div/button[1]')
        await expect(getbutn).to_be_visible()
        await getbutn.click()
        # await exitbtn.click()
        await browser.close()
        

if __name__ == '__main__':
    asyncio.run(main())