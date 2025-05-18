import asyncio

from mcp_agent.core.fastagent import FastAgent

fast = FastAgent("Demo Agent")


@fast.agent(
    instruction="You are a helpful AI Agent",
    servers=["fetch", "filesystem", "time", "item"],
)
async def main():
    async with fast.run() as agent:
        await agent()


if __name__ == "__main__":
    asyncio.run(main())  # type: ignore
