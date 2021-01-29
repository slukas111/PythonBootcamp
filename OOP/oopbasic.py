class Building:
    def __init__(self, season_in_year, apartment_number, apartment_size):
        self.season_in_year = season_in_year
        self.apartment_number = apartment_number
        self.apartment_size = apartment_size

    def show_apartment_details(self):
        print(
            f"season || {self.season_in_year}, apartment # || {self.apartment_number}, apartment size || {self.apartment_size}"
        )

    def rent_calculation(self):

        base_price_per_month = 2000
        season_price_buffer = 0

        if self.season_in_year == "Summer":
            season_price_buffer = 1.5

        elif self.season_in_year == "Winter":
            season_price_buffer = 1.1

        elif self.season_in_year == "Spring":
            season_price_buffer = 1.4

        elif self.season_in_year == "Fall":
            season_price_buffer = 1.3

        else:
            season_price_buffer = None

        if self.apartment_size > 130:
            season_price_buffer += 0.1

        total_rent_price = base_price_per_month * season_price_buffer
        print(f"the buffer is: {season_price_buffer}")
        print(f"the total price is: {total_rent_price}")

        return total_rent_price

    def monthly_maintenance_pay(self, rent_price):
        maintenance = 0

        if rent_price > 3000:
            maintenance = 100
        else:
            maintenance = 50

        print(f"the maintenance fee is: {maintenance}")


# instances
lease_contract_1 = Building("Summer", 4, 135)
# lease_contract_1.show_apartment_details()
rent_price_1 = lease_contract_1.rent_calculation()
lease_contract_1.monthly_maintenance_pay(rent_price_1)
print("\n")
lease_contract_2 = Building("Spring", 17, 100)
lease_contract_2.show_apartment_details()
rent_price_2 = lease_contract_2.rent_calculation()
lease_contract_2.monthly_maintenance_pay(rent_price_2)
print("\n")
lease_contract_3 = Building("Fall", 3, 125)
lease_contract_3.show_apartment_details()
rent_price_3 = lease_contract_3.rent_calculation()
lease_contract_3.monthly_maintenance_pay(rent_price_3)
