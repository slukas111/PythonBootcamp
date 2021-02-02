class Car:
    def __init__(self, car_data_list):
        self.car_data_list = car_data_list

    def show_car_detail(self):
        print(
            f"the vehicle on lot {self.car_data_list[2],self.car_data_list[0],self.car_data_list[1]}"
        )

    def insurance_calculation(self):
        year_release = self.car_data_list[0]
        current_price = self.car_data_list[1]
        model = self.car_data_list[2]

        if (year_release >= 2010 and year_release <= 2020) and (
            current_price >= 6000 and current_price <= 17000
        ):
            # if 2020 >= year_release >= 2010 and 6000 <= current_price <= 17000:
            insurance = current_price * 0.05
        else:
            insurance = current_price * 0.07
        print(f"here is the calculated insurance: {round(insurance, 2)}")

    def doors_closed(self):
        doors_status = self.car_data_list[-1]

        if doors_status == True:
            print("the doors are closed ")
        elif doors_status == False:
            print("doors are open ")
        else:
            print("wrong valued entered")


ford_focus_list = [2005, 5000, "ford_focus", True]
ford_focus_instance = Car(ford_focus_list)
ford_focus_instance.show_car_detail()
ford_focus_instance.insurance_calculation()
ford_focus_instance.doors_closed()
print("\n")
audi_a3_list = [2011, 15000, "audi_a3", False]
audi_a3_instance = Car(audi_a3_list)
audi_a3_instance.show_car_detail()
audi_a3_instance.insurance_calculation()
ford_focus_instance.doors_closed()
