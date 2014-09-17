import facebook
graph = facebook.GraphAPI()
print "Mashable has %s fans" % graph.get_object('/mashable')['fan_count']
