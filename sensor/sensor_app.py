# Runner script for all modules
from load_data import load_sensor_data
from house_info import HouseInfo
from datetime import datetime, date
##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
##############################

# Module 1 code here:
data = load_sensor_data()
print("Loaded records: {}".format(len(data)))
# Module 2 code here:
house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_tata_by_area("id", rec_area = test_area)
print("\nHouse sensor records for area {} = {}".format(test_area, len(recs)))
# Module 3 code here:

# Module 4 code here:

# Module 5 code here: