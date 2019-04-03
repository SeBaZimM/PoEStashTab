import asyncio

from configuration import Client, Setup

async def main():
	client = Client.Client('Sanja0408','Synthesis')
	setup  = Setup.Setup(client.account_name, client.league, client.cookie_jar)
	await asyncio.gather(setup.setup())

if __name__ == '__main__':
	asyncio.run(main())
