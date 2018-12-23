import base64
import json

def g(c):
    if c.lower() == "u05d0":
        return 1
    elif c.lower() == "u05d1":
        return 2
    elif c.lower() == "u05d2":
        return 3
    elif c.lower() == "u05d3":
        return 4
    elif c.lower() == "u05d4":
        return 5
    elif c.lower() == "u05d5":
        return 6
    elif c.lower() == "u05d6":
        return 7
    elif c.lower() == "u05d7":
        return 8
    elif c.lower() == "u05d8":
        return 9
    elif c.lower() == "u05d9":
        return 10
    elif c.lower() == "u05db":
        return 20
    elif c.lower() == "u05dc":
        return 30
    elif c.lower() == "u05de":
        return 40
    elif c.lower() == "u05e0":
        return 50
    elif c.lower() == "u05e1":
        return 60
    elif c.lower() == "u05e2":
        return 70
    elif c.lower() == "u05e4":
        return 80
    elif c.lower() == "u05e6":
        return 90
    elif c.lower() == "u05e7":
        return 100
    elif c.lower() == "u05e8":
        return 200
    elif c.lower() == "u05e9":
        return 300
    elif c.lower() == "u05ea":
        return 400
    else :
        return 0

def c(x):
     return 'u05'+x[:2]

def findUnicodesAndCalcSum(mystring):
    uss = mystring.split("u05")
    uss.pop(0)
    us = filter(lambda x: len(x) > 4, map(c,uss))
    sum = 0
    for y in us:
        sum = sum + g(y)
    return sum




def median(lst):
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0

def calc():
	with open('data.json') as fjson:
		data = json.load(fjson)
		ndata = []
		for item in data:
			ndata.extend(data[item])
		
		tsum1 = 0
		valsarr = []
		for item in ndata:
			val = 0
			text = ''
			for key in item:
				if key == "value":
					if(item[key] == "?" ):
						val = -1
					else: 
						val = item[key]
				else:
					text = item[key]
			calc = findUnicodesAndCalcSum(text)
			valsarr.append(calc)

		valsarr.sort()
		# m = median(valsarr)
		for v in range(0,len(valsarr)/2):
			tsum1 = tsum1 + valsarr[v]

		encoded = base64.b64encode(str(tsum1))
		print encoded

calc()