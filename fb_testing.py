import facebook
import json


ACCESS_TOKEN = 'CAADGZBDQaJpYBAFV0HYjWayAwOen4C8ZChjNThknKAiy48KfceJNn3dgY1eYrmlmr0S1atOl5jGSIFacO8m02yHosvPv5PhqaBdZBjMZBTa2zTSI80LwBb1odGUCU6QZCrOlQu3WVjPztZAzpfUaohYIPexsS7ZATrZAQx0gAffXIZArpYesbyHYUxpc3tNOxdBzeNrNQRC2hJwh86n3DWqiO'

base_url = 'https://graph.facebok.com/clay.davis.146'

def pp(o): 
    print json.dumps(o, indent=1)

def int_format(n): return "{:,}".format(n)
    
g = facebook.GraphAPI(ACCESS_TOKEN)

pepsi_id = '56381779049'
kobe_id = 'kobe'
coke_id = 'cocacola'

print "Facebook users who like Coca Cola:", int_format(g.get_object(coke_id)['likes'])
print "Facebook users who like Kobe Bryant:", int_format(g.get_object(kobe_id)['likes'])
