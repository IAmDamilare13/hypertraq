from .model import *


class User(Model):
    def __init__(
        self,
        models: "Users",
        *,
        firstname: str,
        lastname: str,
        email: str,
        password: str,
        phone_number: str,
        role: str = "",
        org_name: str = "",
        org_location: str = "",
        org_phone_number: str = "",
        professional_id: str = "",
        **kwargs,
    ) -> None:
        super().__init__(models, **kwargs)

        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.role = role
        self.org_name = org_name
        self.org_location = org_location
        self.org_phone_number = org_phone_number
        self.professional_id = professional_id


class Users(Models):
    model_class = User


Users = Users()
