from config.database import Base
from sqlalchemy import Column, Integer, String, Time, ForeignKey, Boolean, BigInteger, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.orm import relationship

class Carrer(Base):
    __tablename__ = "carrer"
    id_carrer = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    courses = relationship("Course", back_populates="carrer")
    assignments = relationship("Assignment", back_populates="carrer")

class Course(Base): 
    __tablename__ = "course"
    id_course = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    semester = Column(Integer, nullable=False)
    carrer_id = Column(Integer, ForeignKey("carrer.id_carrer"))
    carrer = relationship("Carrer", back_populates="courses") 
    assignments = relationship("Assignment", back_populates="course")
    qualifications = relationship("Qualification", back_populates="course")
    schedule_assignments = relationship("ScheduleAssignment", back_populates="course") 

class Assignment(Base):
    __tablename__ = "assignment"
    id_assignment = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("course.id_course"), nullable=False)
    carrer_id = Column(Integer, ForeignKey("carrer.id_carrer"), nullable=False)
    year = Column(Integer, nullable=False)
    semester = Column(Integer, nullable=False)
    section = Column(String, nullable=False)
    assigned = Column(Integer, nullable=False)
    course = relationship("Course", back_populates="assignments")
    carrer = relationship("Carrer", back_populates="assignments")

    __table_args__ = (
        UniqueConstraint('course_id', 'carrer_id', 'year', 'semester', 'section', name='uq_assignment_fields'),
    )

class Teacher(Base):
    __tablename__ = "teacher"
    dpi_teacher = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    start_conntracting_hour = Column(Time, nullable=False)
    end_conntracting_hour = Column(Time, nullable=False)
    qualifications = relationship("Qualification", back_populates="teacher")
    schedule_assignments = relationship("ScheduleAssignment", back_populates="teacher") 

class Classroom(Base):
    __tablename__ = "classroom"
    id_classroom = Column(Integer, primary_key=True)
    capacity = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    schedule_assignments = relationship("ScheduleAssignment", back_populates="classroom") 

class Qualification(Base):
    __tablename__ = "qualification"
    id_qualification = Column(Integer, primary_key=True, autoincrement=True)
    teacher_dpi = Column(BigInteger, ForeignKey("teacher.dpi_teacher"))
    course_id = Column(Integer, ForeignKey("course.id_course"))
    is_owner = Column(Boolean, default=False)
    teacher = relationship("Teacher", back_populates="qualifications")
    course = relationship("Course", back_populates="qualifications")

    __table_args__ = (
        UniqueConstraint('teacher_dpi', 'course_id', name='uq_qualification_fields'),
    )

class ScheduleAssignment(Base):
    __tablename__ = "schedule_assignment"
    course_id = Column(Integer, ForeignKey("course.id_course"), primary_key=True)
    classroom_id = Column(Integer, ForeignKey("classroom.id_classroom"), primary_key=True)
    teacher_dpi = Column(BigInteger, ForeignKey("teacher.dpi_teacher"), primary_key=True)
    criterion_id = Column(Integer, ForeignKey("criterion.id_criterion"))
    section = Column(String, primary_key=True)
    year = Column(Integer, nullable=False, unique=True)
    semester = Column(Integer, nullable=False, unique=True)
    star_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    warnings = Column(String)
    course = relationship("Course", back_populates="schedule_assignments")
    classroom = relationship("Classroom", back_populates="schedule_assignments")
    teacher = relationship("Teacher", back_populates="schedule_assignments")
    criteria = relationship("Criterion", back_populates="schedule_assignments")

    __table_args__ = (
        PrimaryKeyConstraint("course_id", "classroom_id", "teacher_dpi", "section"),
    )

class Criterion(Base):
    __tablename__ = "criterion"
    id_criterion = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    schedule_assignments = relationship("ScheduleAssignment", back_populates="criteria") 
