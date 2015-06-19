#!/usr/local/bin/python3
import sys
import math, re
import sh
from blessings import Terminal

MAX = 2500
term = Terminal()
TERM_SIZE = term.width
LINES = term.height - 7

integer = re.compile(r'^[0123456789]+$')

timequeue = []

usage = '''usage: %s [<url to ping>] [<max lines to display>]''' % sys.argv[0]

timeouts = 0
count = 0
average = 0

url = 'google.com'

# args!
if len(sys.argv) == 2:
	if integer.match(sys.argv[1]):
		LINES = int(sys.argv[1])
	else:
		url = sys.argv[1]
elif len(sys.argv) == 3:
	url = sys.argv[1]
	LINES = int(sys.argv[2])
elif len(sys.argv) > 3:
	print('Too many arguments supplied')
	print(usage)
	sys.exit()

ip = sh.dig('+short', url).strip()

print('Pinging %s (%s)' % (url, ip))

try:
	for line in sh.ping(url, _iter=True): # I love you, sh.py
		line = line.split()

		# find the time of the ping
		time = None
		for word in line:
			if 'timeout' in word:
				time = 'TIMEOUT'
			elif 'time' in word:
				time = str(int(round(float(word.split('=')[1])))) + ' ms'

		if time is not None:
			count += 1
			term_size = TERM_SIZE - (len(time)+1)

			if time == 'TIMEOUT':
				timeouts += 1
				timestring = '█' * term_size
			else:
				timeint = float(time[:-3])
				success_count = count - timeouts
				average = ((average*(success_count-1)) + timeint) / success_count

				factor = MAX / (TERM_SIZE - 8) # the smallest 'unit', so MAX ping fills the screen
				timestring = '█' * int(min(math.ceil(timeint/factor), term_size))

			timestring = timestring + ' ' + time

			if len(timequeue) >= LINES:
				timequeue.pop(0)
			timequeue.append(timestring)

			# if term.location() 
			if count < LINES:
				print(timestring)
			else:
				# with term.location(0, term.height - len(timequeue)):
				with term.location():
					print(term.move_x(0) + (term.move_up * len(timequeue)))
					print(term.clear_eos + '\n'.join(timequeue), end='')

except KeyboardInterrupt:
	# print stats, and exit gracefully
	print()
	print('sent', count, 'packets')
	print('%.2f%% packet loss' % (100*timeouts/count))
	print('%.2f' % average, 'ms average ping')
