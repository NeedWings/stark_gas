from starknet_py.net.full_node_client import FullNodeClient

 
client = FullNodeClient("https://starknet-mainnet.public.blastapi.io")
async def main():
    while True:
        print((await client.get_block()).gas_price/1e9)
        await asyncio.sleep(1)

asyncio.run(main())
