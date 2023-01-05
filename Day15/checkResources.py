from constants import resources


def check_resources(requested):
    if resources["water"] >= requested["water"] and resources["coffee"] >= requested["coffee"]:
        resources["water"] = resources["water"] - requested["water"]
        resources["coffee"] = resources["coffee"] - requested["coffee"]
        return True
    else:
        print("Resources is not enough for new coffee ")