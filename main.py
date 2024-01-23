from starknet_py.net.full_node_client import FullNodeClient
import asyncio
 
client = FullNodeClient("https://starknet-mainnet.public.blastapi.io")
async def main():
    while True:
        print((await client.get_block("latest")).l1_gas_price.price_in_wei/1e9)
        await asyncio.sleep(1)

asyncio.run(main())
