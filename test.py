import sys
import urllib2
import json
import csv

if __name__=='__main__':
    with open(sys.argv[1], 'r') as jfile:
        bus_data = json.load(jfile)
        active_bus = bus_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
        num_bus = len(active_bus)
        with open(sys.argv[2], 'wb') as csvfile:
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
