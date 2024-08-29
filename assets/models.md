# Models

- User

  - firstname `str`
  - lastname `str`
  - email `str`
  - password `str`
  - phone_number `str`
  - role `str` `nr`

  - org_name `str`
  - org_location `str`
  - org_phone_number `str`

  - professional_id `str`

- MedicalData

  - uid `str`
  - age `int`
  - gender `str`
  - systolic_bp `float`
  - diastolic_bp `float`
  - height `float`
  - weight `float`
  - bmi `float`
  - timestamp `str`
  - diagnosis `str`

- Chat

  - patient_id `str`
  - professional_id `str`
  - sender `str`
  - message `str`
