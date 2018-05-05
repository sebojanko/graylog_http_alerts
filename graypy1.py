import logging
import graypy
import time

my_logger = logging.getLogger('test_logger')
my_logger.setLevel(logging.DEBUG)

handler = graypy.GELFHandler('192.168.0.25', 12201)
my_logger.addHandler(handler)

while True:
	my_logger.debug('Danger, Will Robinson, Danger!')
	time.sleep(1)