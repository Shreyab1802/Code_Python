# Question : https://thejoboverflow.com/problem/170/
# Leetcode : https://leetcode.com/discuss/interview-question/570407/salesforce-oa-hackerrank

def find_price(n, m, instances, prices):
    # Filter out invalid prices
    valid_data = [(instances[i], prices[i]) for i in range(m) if prices[i] > 0]
    if not valid_data:
        return 0.0  # if all prices are invalid, return 0.0

    # Sort data by instances
    valid_data.sort()

    # Check for exact match
    for instance, price in valid_data:
        if instance == n:
            return price

    # Interpolate or extrapolate
    smaller = None
    larger = None

    for instance, price in valid_data:
        if instance < n:
            smaller = (instance, price)
        if instance > n and larger is None:
            larger = (instance, price)

    if smaller and larger:
        # Linear interpolation
        x1, y1 = smaller
        x2, y2 = larger
        price = y1 + (y2 - y1) * (n - x1) / (x2 - x1)
        return price
    elif smaller:
        # Linear extrapolation using the last two smaller points
        (x1, y1), (x2, y2) = valid_data[-2], valid_data[-1]
        price = y1 + (y2 - y1) * (n - x1) / (x2 - x1)
        return price
    else:
        # Linear extrapolation using the first two larger points
        (x1, y1), (x2, y2) = valid_data[0], valid_data[1]
        price = y1 + (y2 - y1) * (n - x1) / (x2 - x1)
        return price


# Input data
n = 75
m = 3
instances = [25, 50, 100]
prices = [5.0, 4.0, 3.0]

# Compute and output the price
price = find_price(n, m, instances, prices)
print(f"{price:.6f}")


########## 2nd solution ####################

def find_price(n, m, instances, prices):
    # Filter out invalid prices
    valid_data = [(instances[i], prices[i]) for i in range(m) if prices[i] > 0]
    if not valid_data:
        return 0.0  # if all prices are invalid, return 0.0

    # Sort data by instances
    valid_data.sort()

    # Check for exact match
    for instance, price in valid_data:
        if instance == n:
            return price

    # Interpolate or extrapolate
    smaller = None
    larger = None

    for instance, price in valid_data:
        if instance < n:
            smaller = (instance, price)
        if instance > n and larger is None:
            larger = (instance, price)

    if smaller and larger:
        # Linear interpolation
        x1, y1 = smaller
        x2, y2 = larger
        price = y1 + (y2 - y1) * (n - x1) / (x2 - x1)
        return price
    elif smaller:
        # Linear extrapolation using the last two smaller points
        (x1, y1), (x2, y2) = valid_data[-2], valid_data[-1]
        price = y1 + (y2 - y1) * (n - x1) / (x2 - x1)
        return price
    else:
        # Linear extrapolation using the first two larger points
        (x1, y1), (x2, y2) = valid_data[0], valid_data[1]
        price = y1 + (y2 - y1) * (n - x1) / (x2 - x1)
        return price


# Input data
n = 25
m = 5
instances = [10, 25, 50, 100, 500]
prices = [2.46, 2.58, 2.0, 2.25, 3.0]

# Compute and output the price
price = find_price(n, m, instances, prices)
print(f"{price:.6f}")
