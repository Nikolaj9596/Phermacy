__all__ = ["Doctor"]
from datetime import date, datetime
from typing import Optional

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import Base


class Doctor(Base):
    __tablename__ = "doctor"

    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    middle_name: Mapped[str] = mapped_column(String(50))
    date_start_work: Mapped[date] = mapped_column(Date)
    profession_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("profession.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    appointments: Mapped["DoctorAppointment"] = relationship(back_populates="doctor")
    client_diagnosis: Mapped["ClientDiagnosis"] = relationship(back_populates="doctor")
    profession: Mapped["Profession"] = relationship(back_populates="doctors")


class DoctorAppointment(Base):
    __tablename__ = "make_anappointment"

    start_date_appointment: Mapped[datetime]
    end_date_appointment: Mapped[datetime]
    doctor_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("doctor.id", ondelete="SET NULl"), index=True, nullable=True
    )
    client_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("client.id", ondelete="SET NULl"), index=True, nullable=True
    )
    doctor: Mapped["Doctor"] = relationship(back_populates="appointments")
    client: Mapped["Client"] = relationship(back_populates="appointments")
