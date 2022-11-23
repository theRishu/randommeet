from sqlalchemy import Column, BigInteger,Integer, String, Boolean

from utils.db_api.base import Base


class User(Base):
    __tablename__ = "user"

    
    user_id = Column(BigInteger, primary_key=True)
    gender = Column(String(2), default='NA')
    partner_gender = Column(String(2), default='NA')
    is_vip = Column(Boolean, unique=False, default=False)
    age = Column(Integer, default=0)
    total_referral = Column(Integer, default=0)
    rating = Column(Integer, default=0)
    country = Column(String(16))
    code = Column(String(16))
    state = Column(String(1), default='A')
    partner_id = Column(BigInteger)
    last_partner_id = Column(BigInteger)
    ro_id  = Column(BigInteger)
    mperm  = Column(Boolean,  default=False)
