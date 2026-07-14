from tools import RestaurantTool

tool=RestaurantTool()

print(
    tool.search(
        cuisine="Biryani"
    )
)

print()

print(
    tool.search(
        cuisine="Cafe"
    )
)

print()

print(
    tool.search(
        budget=600
    )
)