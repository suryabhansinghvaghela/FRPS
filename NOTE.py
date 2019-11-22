#import requests 
#url = "https://rzp_test_Ymrxr3dAmuXw7x:ZMfg3cO6wj9oW2zsTGJQ2FrC@api.razorpay.com/v1/payments"


import urllib.request,json

url = "http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false"

response = urllib.request.urlopen(url)

data = json.loads(response.read())

print(data)





#KID - rzp_test_uxn2fKkLYq4J29
#SK - dLB9zcMUvz6sOp2bErjYEU8C

https://rzp_test_uxn2fKkLYq4J29:dLB9zcMUvz6sOp2bErjYEU8C@api.razorpay.com/v1/payments \
data = {'type':'link', \
		 'currency':'INR', \ 
		 'description':'TRY 1', \ 
		 'amount':'1500', \
		 'customer[name]':'Dharmit Saradva', \
		 'customer[email]':'dsaradva@gmail.com', \
		 'customer[contact]':'9409678919' \
		 } 


https://rzp_test_uxn2fKkLYq4J29:dLB9zcMUvz6sOp2bErjYEU8C@api.razorpay.com/v1/payments ^
data = {'type':'link','currency':'INR','description':'TRY 1','amount':'1500','customer[name]':'Dharmit Saradva','customer[email]':'dsaradva@gmail.com','customer[contact]':'9409678919'} 