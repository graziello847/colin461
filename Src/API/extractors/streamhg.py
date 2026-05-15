import  Src.Utilities.config as config
from Src.Utilities.eval import eval_solver
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
Icon = config.Icon
Name = config.Name




async def streamhg(link,client,streams, site_name, proxies,ForwardProxy):
    link = 'https://audinifer.com/e/' + link.split('/e/')[1]
    url = await eval_solver(link,proxies, ForwardProxy, client,r'"hls2":"([^"]+)"')
    if url:
        streams['streams'].append({'name': f"{Name}",'title': f'{Icon}{site_name}\n▶️ StreamHG', 'url': url, 'behaviorHints': {'bingeGroup': f'{site_name.lower()}'}})
        logger.info(f"{site_name} on StreamHG found results for the current ID")
        status = True
    else:
        status = False
    return streams,status




async def test_streamhg():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await streamhg("https://dhcplay.com/e/zctlgpn3zoll",client,{'streams': []}, "StreamHG", {},"")
        print(results)
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_streamhg()) 

