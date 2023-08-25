from config.database import Base
from sqlalchemy import Column, Integer, String, Time, ForeignKey, BigInteger, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

class Carrer(Base):
    __tablename__ = "carrer"
    id_carrer = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    courses = relationship("Course", back_populates="courses")
    assignments = relationship("Assignment", back_populates="assignments")

class Course(Base): 
    __tablename__ = "course"
    id_course = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    semester = Column(Integer, nullable=False)
    carrer_id = Column(Integer, ForeignKey("carrer.id_carrer"))
    carrers = relationship("Carrer", back_populates="carrers")
    assignments = relationship("Assignment", back_populates="assignments")

class Assignment(Base):
    __tablename__ = "assignment"
    course_id = Column(Integer, ForeignKey("course.id_course"), primary_key=True)
    carrer_id = Column(Integer, ForeignKey("carrer.id_carrer"), primary_key=True)
    year = Column(Integer, primary_key=True)
    semester = Column(Integer, primary_key=True)
    assigned = Column(Integer, nullable=False)
    courses = relationship("Course", back_populates="courses")
    carrers = relationship("Carrer", back_populates="carrers")

    __table_args__ = (
        PrimaryKeyConstraint("course_id", "carrer_id", "year", "semester"),
    )

class Area(Base):
    __tablename__ = "area"
    id_area = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    requirements = relationship("Requeriment", back_populates="requeriments")

class Teacher(Base):
    __tablename__ = "teacher"
    dpi_teacher = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    specialties = relationship("Specialty", back_populates="specialties")

class Classroom(Base):
    __tablename__ = "classroom"
    id_classroom = Column(Integer, primary_key=True)
    capacity = Column(Integer, nullable=False)
    name = Column(String, nullable=False)

class Requirement(Base):
    __tablename__ = "requeriment"
    area_id = Column(Integer, ForeignKey("area.id_area"), primary_key=True)
    course_id = Column(Integer, ForeignKey("course.id_course"), primary_key=True)
    areas = relationship("Area", back_populates="areas")
    courses = relationship("Course", back_populates="courses")

    __table_args__ = (
        PrimaryKeyConstraint("area_id", "course_id"),
    )

class Specialty(Base):
    __tablename__ = "specialty"
    area_id = Column(Integer, ForeignKey("area.id_area"), primary_key=True)
    teacher_dpi = Column(BigInteger, ForeignKey("teacher.dpi_teacher"), primary_key=True)
    areas = relationship("Area", back_populates="areas")
    teachers = relationship("Teacher", back_populates="teachers")

    __table_args__ = (
        PrimaryKeyConstraint("area_id", "teacher_dpi"),
    )

class ScheduleAssignment(Base):
    __tablename__ = "schedule_assignment"
    course_id = Column(Integer, ForeignKey("course.id_course"), primary_key=True)
    classroom_id = Column(Integer, ForeignKey("classroom.id_classroom"), primary_key=True)
    teacher_dpi = Column(BigInteger, ForeignKey("teacher.dpi_teacher"), primary_key=True)
    year = Column(Integer, nullable=False)
    semester = Column(Integer, nullable=False)
    star_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    courses = relationship("Course", back_populates="courses")
    classrooms = relationship("Classroom", back_populates="classrooms")
    teachers = relationship("Teacher", back_populates="teachers")

    __table_args__ = (
        PrimaryKeyConstraint("course_id", "classroom_id", "teacher_dpi"),
    )