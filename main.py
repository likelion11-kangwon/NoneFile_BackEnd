import asyncio

from Router.router import root


async def main():
    print("Run main")
    await root()

asyncio.run(main())
