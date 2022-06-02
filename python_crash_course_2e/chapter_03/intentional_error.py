# intentional_error.py

# cars.py

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw','audi','toyota','subaru']

print("\nHere is the original list:")
print(cars)


print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse sorted list:")
print(sorted(cars,reverse=True))

print("\nHere is the original list again:")
print(cars)

cars = ['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)

cars = ['bmw','audi','toyota','subaru']
print(cars[4])