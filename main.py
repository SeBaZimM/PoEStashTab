import asyncio

from configuration import Client, Init

async def main():
	client = Client.Client('Sanja0408','Synthesis')
	init   = Init.Init(client.account_name, client.league, client.cookie_jar)
	await asyncio.gather(init.update_stashtab(1))

if __name__ == '__main__':
	asyncio.run(main())
