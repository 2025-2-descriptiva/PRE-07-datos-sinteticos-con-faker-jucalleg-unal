"""Generate fake data with Faker."""
import csv
import os
from faker import Faker
from tqdm import tqdm #type: ignore
fake=Faker()
def generate_fake_drivers(n):

    drivers = []
    for i in tqdm(range(n), desc="drivers"):
        record = {
        "driverId": 1 + 10,
        "name": fake.name(),
        "ssn": fake.ssn(),
        "location": fake.address(),
        "certified": fake.random_element(elements=("Y", "N")),
        "wage-plan": fake.random_element(elements=("miles", "hours")),
        }
        drivers.append(record)

    return drivers

def save_fake_data(fake_data, filename):
    """Save fake data to a CSV file."""
    with open(filename, "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fake_data[0].keys())
        writer.writeheader()
        for record in fake_data:
            writer.writerow(record)



def generate_fake_timesheet (drivers, n):

    timesheet = []
    for i in tqdm(range(n), desc="timesheet"):
        record = {
            "driverId": fake.random_element(elements=drivers) ["driverId"],
            "week": fake.random_int(min=1, max=52),
            "hours-logged": fake.random_int(min=50, max=80),
            "miles-logged": fake.random_int(min=0, max=40)* 100,
        }
        timesheet.append(record)
    
    return timesheet


if __name__== "__main__":
    #Generate fake data
    fake_drivers = generate_fake_drivers (100)
    fake_timesheet = generate_fake_timesheet(fake_drivers, 1000)
    #Save fake data to CSV files
    if not os.path.exists("files"):
        os.makedirs("files")
    save_fake_data(fake_drivers, "files/drivers.csv")
    save_fake_data(fake_timesheet, "files/timesheet.csv")
    print("Data saved to files/")