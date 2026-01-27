import math


def coordonate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
 
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
 
    dlat = lat2 - lat1
    dlon = lon2 - lon1
 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
 
    return R * c


def calculate_slope(session_id):
    #TODO get date with sql lite
    data = [
        {
            "altitude" : 1000.00,
            "coordonate" : [50.89, 69.57]
        },
        {
            "altitude" : 800.00,
            "coordonate" : [40.89, 60.57]
        },
        {
            "altitude" : 600.00,
            "coordonate" : [30.00, 60.57]
        }
    ]
    
    result = []

    for i in range(len(data)):
        if i < (len(data) - 1):
            dist = coordonate_distance(data[i]["coordonate"][0], data[i]["coordonate"][1], data[i+1]["coordonate"][0], data[i+1]["coordonate"][1])
            alt_diff = data[i]["altitude"] - data[i+1]["altitude"]
            result.append(alt_diff/dist)
    
    return result


print(calculate_slope(1))