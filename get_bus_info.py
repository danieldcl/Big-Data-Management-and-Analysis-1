import sys
import urllib2
import json
import csv

if __name__=='__main__':
    mta_key = sys.argv[1]
    bus_num = sys.argv[2]
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'%(mta_key, bus_num)
    request = urllib2.urlopen(url)
    bus_data = json.load(request)
    active_bus = bus_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    num_bus = len(active_bus)
    with open(sys.argv[3], 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])
        for s in range(num_bus):
            latitude = active_bus[s]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            longitude = active_bus[s]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            stop_name = "N/A"
            stop_status = "N/A"
            if active_bus[s]['MonitoredVehicleJourney']['OnwardCalls'] != "":
                stop_name = active_bus[s]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                stop_status = active_bus[s]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            row = [latitude, longitude, stop_name, stop_status]
            writer.writerow(row)
