class TestHelper():
    
    @staticmethod
    def replace_fields_for_creating_order_test(source, destination, user_data):
        source["order"]["_id"] = destination.json()["order"]["_id"]
        source["order"]["owner"]["name"] = user_data["name"]
        source["order"]["owner"]["email"] = user_data["email"]
        source["order"]["owner"]["createdAt"] = destination.json()["order"]["owner"]["createdAt"]
        source["order"]["owner"]["updatedAt"] = destination.json()["order"]["owner"]["createdAt"]
        source["order"]["createdAt"] = destination.json()["order"]["createdAt"]
        source["order"]["updatedAt"] = destination.json()["order"]["updatedAt"]
        source["order"]["number"] = destination.json()["order"]["number"]
        source["order"]["price"] = destination.json()["order"]["price"]
        return source