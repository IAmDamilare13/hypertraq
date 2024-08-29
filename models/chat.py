from .model import *


class Chat(Model):
    def __init__(
        self,
        models: "Chats",
        *,
        patient_id: str,
        professional_id: str,
        sender: str,
        message: str,
        **kwargs,
    ) -> None:
        super().__init__(models, **kwargs)

        self.patient_id = patient_id
        self.professional_id = professional_id
        self.sender = sender
        self.message = message


class Chats(Models):
    model_class = Chat


Chats = Chats()
