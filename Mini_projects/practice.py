bus_stops_and_routes = {
  "X60": ["sandnes", "stavanger", "sola", "haugesund", "bryne", "sandnes"],
  "X61": ["sandnes", "stavanger", "sola", "haugesund", "bryne", "sandnes"],
  "N2": ["bergen", "oslo", "bergen"]}


def get_route_stops(route):
  for value in bus_stops_and_routes.values():
    if route in value:
      print("your bus stops are: ", value)


get_route_stops("X60")
