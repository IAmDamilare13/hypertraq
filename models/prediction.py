from .model import *


class Prediction(Model):
    def __init__(
        self,
        models: "Predictions",
        *,
        uid: str,
        result: str,
        **kwargs,
    ) -> None:
        super().__init__(models, **kwargs)

        self.uid = uid
        self.result = result


class Predictions(Models):
    model_class = Prediction


Predictions = Predictions()
