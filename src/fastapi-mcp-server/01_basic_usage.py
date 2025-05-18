from fastapi_mcp import FastApiMCP
from shared.apps.items import app
from shared.setup import setup_logging

setup_logging()

mcp = FastApiMCP(app)

mcp.mount()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
