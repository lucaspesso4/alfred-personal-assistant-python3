import wolframalpha
import wikipedia

while True:
	question = input('Ask me something: ')
	try:
		# wolframalpha
		apikey = 'XxXxXx-xXxXxXxXxX'
		client = wolframalpha.Client(apikey)
		res = client.query(question)
		answer = next(res.results).text
		print(answer)
	except:
		# wikipedia
		wikipedia.set_lang('us')
		print(wikipedia.summary(question, sentenses = 2))