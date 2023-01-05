from constants import resources


def check_resources(requested):
    if "milk" not in requested:
        if resources["water"] >= requested["water"] and resources["coffee"] >= requested["coffee"]:
            resources["water"] = resources["water"] - requested["water"]
            resources["coffee"] = resources["coffee"] - requested["coffee"]
            return True
    else:
        if resources["water"] >= requested["water"] and resources["coffee"] >= requested["coffee"] and \
                resources["milk"] >= requested["milk"]:
            resources["water"] = resources["water"] - requested["water"]
            resources["coffee"] = resources["coffee"] - requested["coffee"]
            resources["milk"] = resources["milk"] - requested["milk"]
            return True

