import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,keyuri,setTTL
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'jateng'
		listkabkot = [
		'%3301%','%3302%','%3303%','%3304%','%3305%','%3306%','%3307%','%3308%','%3309%','%3310%',
		'%3311%','%3312%','%3313%','%3314%','%3315%','%3316%','%3317%','%3318%','%3319%','%3320%',
		'%3321%','%3322%','%3323%','%3324%','%3325%','%3326%','%3327%','%3328%','%3329%',
		'%3371%','%3372%','%3373%','%3374%','%3375%','%3376%','%3388','$3399'
		]
		provloc = '110.159872, -7.138075'
		mapzoom = '9'
		kabkotcord = [
		'108.858048, -7.578583',
		'109.061075, -7.373165',
		'109.397215, -7.241831',
		'109.575888, -7.422398',
		'109.663557, -7.675222',
		'110.022942, -7.70976',
		'109.908374, -7.354766', #RF
		'110.206305, -7.480867',
		'110.59148, -7.523172',
		'110.664080, -7.739502',
		'110.820435, -7.684186',
		'110.925449, -7.790413',
		'110.984578, -7.607561',
		'111.025518, -7.418141',
		'110.838309, -7.069161',
		'111.411095, -6.968463',
		'111.331837, -6.707997',
		'111.028771, -6.742185',
		'110.839126, -6.808539',
		'110.762113, -6.555276',
		'110.636915, -6.892974',
		'110.434981, -7.005688',
		'110.172704, -7.318205',
		'110.200499, -6.931101',
		'109.729064, -6.902824',
		'109.667808, -6.888272',
		'109.392339, -6.923217',
		'109.123720, -6.878921',#uki
		'108.884346, -7.013345',#uki
		'110.223011, -7.481218',#uki
		'110.823955, -7.574859',#uki
		'110.503626, -7.331238',#uki
		'110.429121, -7.001583',#uki
		'109.673467, -6.889120',#uki
		'109.101790, -6.861921'#uki
		'109.485088, -7.560118'#uki
		'110.354836, -7.168365'#uki
		]
		batik.provinsi(provinsi,listkabkot,provloc,mapzoom,kabkotcord)
		cal = calendar.Calendar()
		dt = {}
		for kabkot in listkabkot:
			dt[kabkot]=cal.getYearCountKabKot(str(int(kabkot[1:3])),str(int(kabkot[3:5])),uridt)
		cal.close()
		dt['%WMTS%']=getWMTS()
		dt['%PERIODE%']=uridt
		dt['%LAMAN INDONESIA%']=urlEncode16(keyuri+'%peta%home'+'%'+uridt)
		dt['%TAHUN SEBELUMNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)-1))
		dt['%TAHUN SETELAHNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)+1))
		return dt