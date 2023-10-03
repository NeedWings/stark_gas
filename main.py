from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import MAINNET
 
client = GatewayClient(MAINNET)
async def main():
    while True:
        print((await client.get_block()).gas_price/1e9)
        await asyncio.sleep(1)

asyncio.run(main())
