from configuration import Client, Init

def main():

	client = Client.Client('Sanja0408', 'Synthesis')
	init = Init.Init(client)

	init.setup()
	#ui = test_start.Ui_Form()
	#ui.start()


if __name__ == '__main__':
	main()
