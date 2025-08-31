from sqlalchemy import Column, Integer, Text
from .database import Base

class Job(Base):
    __tablename__ = "myjob"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    salary = Column(Text)
    date_posted = Column(Text)
    location = Column(Text)
    closing_date = Column(Text)
    link = Column(Text)  # ✅ New field added
