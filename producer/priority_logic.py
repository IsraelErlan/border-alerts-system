

def get_priority_level(alert: dict):
    if (alert["weapons_count"] > 0 or 
        alert["distance_from_fence_m"] <= 50 or 
        alert["people_count"] >= 8 or 
        alert["vehicle_type"] == "truck") or(
        alert["distance_from_fence_m"] <= 150 and
          alert["people_count"] >= 4) or (
          alert["vehicle_type"] == "jeep" and 
          alert["people_count"] >= 3):
        return 'URGENT'
    else: 
        return 'NORMAL'

        
    



