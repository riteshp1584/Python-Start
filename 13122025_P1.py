def get_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

stats = get_stats([10, 20, 30, 40, 50])
print(stats)
ttl, avg = stats
print(f"Total is {ttl}")
print(f"Average is {avg}")

data = {'NVDA': 120.5, 'TSMC': 95.2, 'INTC': 22.1}
print(data['NVDA'])
print(data.keys())
print(data.values())
for k, v in data.items():
    print(k, v)
