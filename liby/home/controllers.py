from home.models import *

def deletaConta(request):
	try:
		request.user.delete()
		return True
	except:
		return False