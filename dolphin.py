#!/usr/bin/env python
import hashlib
import sys
import os

this = os.path.basename(__file__)
def process(hash,salt,dic):
  for line in open(dic):
		line = line.replace("\n","")
		md5 = hashlib.md5(line).hexdigest()
		spass = hashlib.sha1(md5+salt).hexdigest()
		if spass==hash:
			print("Collision: "+hash+" == "+line)
			sys.exit()

def main():
	if len(sys.argv) == 4:
		process(sys.argv[1],sys.argv[2],sys.argv[3])
	else:
		print("Usage: python "+this+" <hash> <salt> <dictionary>")
		sys.exit(0)

if __name__=="__main__":
	main()
