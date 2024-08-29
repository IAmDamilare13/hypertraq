from .model import *


class MedicalData(Model):
    def __init__(
        self,
        models: "MedicalDatas",
        *,
        uid: str,
        age: int,
        gender: str,
        systolic_bp: float,
        diastolic_bp: float,
        height: float,
        weight: float,
        bmi: float,
        timestamp: str,
        diagnosis: str,
        **kwargs,
    ) -> None:
        super().__init__(models, **kwargs)

        self.uid = uid
        self.age = age
        self.gender = gender
        self.systolic_bp = systolic_bp
        self.diastolic_bp = diastolic_bp
        self.height = height
        self.weight = weight
        self.bmi = bmi
        self.timestamp = timestamp
        self.diagnosis = diagnosis


class MedicalDatas(Models):
    model_class = MedicalData


MedicalDatas = MedicalDatas()
