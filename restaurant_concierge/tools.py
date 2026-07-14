import json

class RestaurantTool:
    def __init__(self):
        with open(
            "restaurant_concierge/data/restaurants.json",
            "r",
            encoding="utf-8"
        ) as file:
            self.restaurants=json.load(file)
    
    def search(
            self,
            cuisine=None,
            budget=None,
            area=None
    ):
        
        results=[]
        for restaurant in self.restaurants:
        
            if cuisine:
                if cuisine.lower()!=restaurant["cuisine"].lower():
                    continue
            if area:
                if area.lower()!=restaurant["area"].lower():
                    continue
            if budget:
                if restaurant["budget"]>budget:
                    continue
            results.append(restaurant)
        return {
    "success": len(results) > 0,
    "count": len(results),
    "restaurants": results
}
    

