from dataclasses import dataclass, fields


@dataclass
class WorkerData:
    id: int
    email: str
    name: str
    department: str
    hours_worked: int
    hourly_rate: int | None = None
    rate: int | None = None
    salary: int | None = None

    @property
    def hourly_salary(self):
        result = (
            self.hourly_rate
            if self.hourly_rate
            else self.rate if self.rate else self.salary
        )
        if result:
            return result
        raise TypeError("You must provide a hourly_rate or rate or salary")

    @property
    def result_salary(self):
        return int(self.hourly_salary) * int(self.hours_worked)

    def validate(self):
        is_ok = True
        for _, field in self.__dataclass_fields__.items():
            actual_type = getattr(self, field.name)
            if not isinstance(actual_type, field.type):
                raise TypeError(f"{field.name} - expected {field.type} but got {type(actual_type)}")
        return is_ok

    def __post_init__(self):
        self.validate()