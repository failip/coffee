import yaml

with open("prices.yaml", "r") as f:
    try:
        prices = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        print(exc)

print(prices)


class user:
    """Userinfo"""
    pass