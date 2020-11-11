import asyncio
from pyppeteer import launch



# # 异步基础
# async def count():
#     print('one')
#     await asyncio.sleep(1)
#     print('two')
#
# # 异步先全部运行await之前的
# async def main():
#     await asyncio.gather(count(), count(), count())
#
# asyncio.run(main())

# 百度截屏
async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://www.baidu.com')
    await page.screenshot({'path': 'baidu.png'})
    dimensions = await page.evaluate('''() => {
            return {
                width: document.documentElement.clientWidth,
                height: document.documentElement.clientHeight,
                deviceScaleFactor: window.devicePixelRatio,
            }
        }''')
    print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

