class Employee:

    def __intit__(self, years_of_experience, position_name, name_of_employee):
        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.name_of_employee = name_of_employee

        def calculate_salary(self):

            base_salary = 25000
            calculated_salary = None

            if 0 < self.years_of_experience and 2 >= self.years_of_experience:
                calculated_salary = base_salary + 15000

            elif 2 < self.years_of_experience and 5 >= self.years_of_experience:
                calculated_salary = base_salary + 25000

            elif self.years_of_expereince > 5:
                calculated_salary = base_salary + 3500

            else:
                print("wrong value entered")
                return calculated_salary

    def candidate_for_bonus(self, salary):

        salary_with_bonus = None

        if "front_end" in self.position_name:
            salary_with_bonus = salary * 1.1
        
        if self.years_of_experience > 2:
            salary_with_bonus = salary * 1.2

        print(f"the bonus for this position: {self.position_name} is: {salary_with_bonus}")


