from pydantic import BaseModel
from typing import List, Optional

class CreditRiskInput(BaseModel):
    age: int
    income: float
    loan_amount: float
    credit_score: Optional[int] = None
    employment_status: str

class CreditRiskOutput(BaseModel):
    risk_level: str
    probability: float

class BatchCreditRiskInput(BaseModel):
    inputs: List[CreditRiskInput]