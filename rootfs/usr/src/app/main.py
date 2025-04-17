import os
import json
from aiohttp import web, ClientSession
from aiohttp.web import middleware
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def load_config():
    with open('/data/options.json') as f:
        return json.load(f)

@middleware
async def error_middleware(request, handler):
    try:
        return await handler(request)
    except Exception as e:
        logger.error(f"Error handling request: {e}")
        return web.Response(text=str(e), status=500)

async def proxy_handler(request):
    config = await load_config()
    path = request.match_info['path']
    page_name = request.match_info['page']
    
    # 查找对应的页面配置
    page_config = None
    for page in config['pages']:
        if page['name'] == page_name:
            page_config = page
            break
    
    if not page_config:
        return web.Response(text="Page not found", status=404)
    
    target_url = f"{page_config['url']}/{path}"
    
    async with ClientSession() as session:
        try:
            async with session.request(
                method=request.method,
                url=target_url,
                headers={k: v for k, v in request.headers.items() if k.lower() not in ['host']},
                data=await request.read()
            ) as response:
                headers = {k: v for k, v in response.headers.items()
                         if k.lower() not in ['transfer-encoding']}
                return web.Response(
                    body=await response.read(),
                    status=response.status,
                    headers=headers
                )
        except Exception as e:
            logger.error(f"Error proxying request to {target_url}: {e}")
            return web.Response(text=str(e), status=502)

async def index_handler(request):
    config = await load_config()
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Internal Web Pages</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .page-list { list-style: none; padding: 0; }
            .page-item { 
                margin: 10px 0;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            .page-link {
                text-decoration: none;
                color: #0066cc;
            }
        </style>
    </head>
    <body>
        <h1>可用页面</h1>
        <ul class="page-list">
    """
    
    for page in config['pages']:
        html += f"""
            <li class="page-item">
                <a href="/proxy/{page['name']}/" class="page-link">
                    {page['name']}
                </a>
            </li>
        """
    
    html += """
        </ul>
    </body>
    </html>
    """
    return web.Response(text=html, content_type='text/html')

app = web.Application(middlewares=[error_middleware])
app.router.add_get('/', index_handler)
app.router.add_route('*', r'/proxy/{page}/{path:.*}', proxy_handler)

if __name__ == '__main__':
    web.run_app(app, port=8099) 