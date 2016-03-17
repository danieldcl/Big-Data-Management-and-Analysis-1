import sys
import urllib2
import json

if __name__=='__main__':
    mta_key = sys.argv[1]
    bus_num = sys.argv[2]
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'%(mta_key, bus_num)
    request = urllib2.urlopen(url)
    bus_data = json.load(request)
    active_bus = bus_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    num_bus = len(active_bus)
    print 'Bus Line : %s' %(bus_num)
    print 'Number of Active Buses : %s' % str(num_bus)
    for i in range(num_bus):
        latitude = active_bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        longitude = active_bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print 'Bus %i is at latitude %s and longitude %s' %(i, latitude, longitude)
