class Employee:

    def __init__(
        self,
        employee_id,
        first_name,
        last_name,
        gender,
        date_of_birth
    ):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.date_of_birth = date_of_birth

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "date_of_birth": self.date_of_birth
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            employee_id=data.get("employee_id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            gender=data.get("gender"),
            date_of_birth=data.get("date_of_birth")
        )