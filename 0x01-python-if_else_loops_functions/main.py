#!/usr/bin/python3
islower = __import__('7-islower').islower

print("'4' => {}".format("lower" if islower("4") else "upper"))
