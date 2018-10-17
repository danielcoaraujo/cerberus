import os
import requests
import json
import tarfile
import shutil
from listRequests import *
from time import gmtime, strftime

currentPath = os.path.dirname(os.path.abspath(__file__))

date = strftime("%d-%m-%Y", gmtime())
time = strftime("%H:%M:%S", gmtime())

header = {'Content-Type':'application/json'}
domain = 'https://...'

try:
	msisdns = open('msisdns.txt', 'r').read().splitlines()
except (IOError, TypeError) as error:
	print 'Error: ' + str(error)

def writeResponseFile(request, response, pathFile, path):
	if not os.path.exists(path):
				os.makedirs(path)
	f = open(pathFile, 'a+')
	f.write('REQUEST:\n\n')
	f.write(request)
	f.write('\n\n---------------------------------\n\n')
	f.write('RESPONSE:\n\n')
	f.write(response)
	f.write('\n\n')
	f.close()

def writeErrorFile(url, e, pathFile, errorPath):
	if not os.path.exists(errorPath):
				os.makedirs(errorPath)
	f = open(pathFile, 'a+')
	f.write('ENDPOINT:' + url + '\n\n')
	f.write('Unexpected error: ' + str(e))
	f.write('\n\n---------------------------------\n\n')
	f.close()

# def make_tarfile(output_filename):
# 	currentPath = os.path.dirname(os.path.abspath(__file__))
# 	with tarfile.open(output_filename+'.tar.gz', "w:gz") as tar:
# 	    tar.add(output_filename, arcname=os.path.basename(output_filename))

for msisdn in msisdns:
	print '\n----------------------------------\n'
	print 'MSISDN:', msisdn, '\n'
	tests = getNames(msisdn)
	for name, payLoad in tests.items():
		url = domain + name.strip()
		try:
			print 'Requesting.... ', url
			request = json.dumps(payLoad)
			response = requests.post(url, data=request, headers=header, timeout=30)
			response = response.text
			path = 'results/' + date + "/" + time + '/' + msisdn + '/'
			pathFile = path + name + '.txt'
			writeResponseFile(request, response, pathFile, path)
		except Exception as e:
			print 'Unexpected error: ', e
			errorPath = 'results/' + date + '/' + time + '/' + '/errors/'
			pathFile = errorPath + msisdn + '.txt'
			writeErrorFile(url, e, pathFile, errorPath)

try:
	print '\n'
	print 'Compressing results...'
	# make_tarfile('results')
	shutil.make_archive('results', 'zip', currentPath+'/results')
	print 'Archive compressed'
except (IOError, TypeError) as error:
	print 'Error: ' + str(error)