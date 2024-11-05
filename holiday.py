# holiday.py

# Define the hotel_cost function
def hotel_cost(num_nights):
    price_per_night = 100  # hotel charges $100 per night
    return num_nights * price_per_night

# Define the plane_cost function
def plane_cost(city_flight):
    # Set flight costs for different cities
    if city_flight.lower() == "paris":
        return 300
    elif city_flight.lower() == "new york":
        return 500
    elif city_flight.lower() == "tokyo":
        return 700
    elif city_flight.lower() == "sydney":
        return 800
    else:
        print("Unknown city. Setting flight cost to $0.")
        return 0

# Define the car_rental function
def car_rental(rental_days):
    daily_rental_cost = 40  # Car rental is $40 per day
    return rental_days * daily_rental_cost

# Define the holiday_cost function
def holiday_cost(num_nights, city_flight, rental_days):
    # Calculate each part of the holiday cost
    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days)
    
    # Calculate total holiday cost
    total_cost = total_hotel_cost + total_plane_cost + total_car_rental_cost
    return total_cost

if __name__ == "__main__":
    # Get user inputs
    city_flight = input("Enter the city you will be flying to (e.g., Paris, New York, Tokyo, Sydney): ")
    num_nights = int(input("Enter the number of nights you will be staying at the hotel: "))
    rental_days = int(input("Enter the number of days you will be hiring a car: "))
    
    # Calculate the total holiday cost
    total_cost = holiday_cost(num_nights, city_flight, rental_days)
    
    # Print a breakdown of the holiday cost
    print("\n---- Holiday Cost Summary ----")
    print(f"Destination city: {city_flight.capitalize()}")
    print(f"Number of nights at hotel: {num_nights}")
    print(f"Hotel cost: ${hotel_cost(num_nights)}")
    print(f"Flight cost to {city_flight.capitalize()}: ${plane_cost(city_flight)}")
    print(f"Car rental for {rental_days} days: ${car_rental(rental_days)}")
    print(f"\nTotal holiday cost: ${total_cost}")
