


import  Src.Utilities.config as config
Icon = config.Icon
Name = config.Name
import re
from fake_headers import Headers
random_headers = Headers()
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
import base64
from bs4 import BeautifulSoup,SoupStrainer
VD_DOMAIN = config.VD_DOMAIN

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:150.0) Gecko/20100101 Firefox/150.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Sec-GPC': '1',
    'Alt-Used': 'v.vidxgo.co',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'DNT': '1',
    'Referer': 'https://altadefinizione.you/',
    'Sec-Fetch-Storage-Access': 'none',
    '-': '-',
    'Priority': 'u=0, i',
}


async def vidxgo(link,client,streams,proxies,ForwardProxy):
    #headers = random_headers.generate()
    response = await client.get(link, allow_redirects=True, headers = headers)
    soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('script'))
    scripts = soup.find_all('script')
    text = scripts[5]
    match = re.search(r"var .+'(.*)',d=atob\('(.*)'",text.text)
    if match:
        key = match.group(1)
        base64_text = match.group(2)
        decoded = base64.b64decode(base64_text)
        u = bytearray(len(decoded))
        for i in range(len(decoded)):
            u[i] = decoded[i] ^ ord(key[i % len(key)])
        decrypted_code = u.decode('utf-8')


    match = re.search(r'currentSrc.+"(https:[^";]+)',decrypted_code)
    if match:
        url = match.group(1).replace("\\","")
        streams['streams'].append({'name': f"{Name}",'title': f'{Icon}Vidxgo\n ▶️ Vidxgo', 'url': url,  'behaviorHints': {'proxyHeaders': {"request": {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',"Accept": "*/*", "Accept-Language":"en-US,en;q=0.9","Referer":VD_DOMAIN+"/","Origin":VD_DOMAIN,"Sec-GPC": "1","Connection": "keep-alive","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"cross-site","DNT": "1","Priority":"u=0"}}, 'notWebReady': True, 'bingeGroup': f'vidxgo'}})
        logger.info(f"Vidxgo found results for the current ID")

    return streams

#Testing
async def test_vidxgo():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await vidsrc("https://v.vidxgo.co/tt34437972/1/1",client,{'streams': []}, "Vidxgo", {})
        print(results)
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_vidxgo()) 




# XOR decryption

