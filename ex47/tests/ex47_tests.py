from nose.tools import *
import ex47

def setup():
	print("SETUP!")

def teardown():
	print("TEARDOWN!")

def test_basic():
	print("I RAN!", end='')
	