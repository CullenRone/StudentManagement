from sqlalchemy import Column, Integer, String, Double, ForeignKey, Enum, Boolean, Date
from datetime import datetime
from sqlalchemy.orm import relationship
from app import db, app
from flask_login import UserMixin
import enum




class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100),
                    default='https://res.cloudinary.com/du5yfxccw/image/upload/v1704394415/m1ctsthqlha7sm6kcatu.png')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
    # receipts = relationship('Receipt', backref='user', lazy=True)
    # comments = relationship('Comment', backref='user', lazy=True)

    def __str__(self):
        return self.name

class Class(db.Model):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    quantity = Column(Integer)
    students = relationship('Student', backref='class', lazy=True)


class Subject(db.Model):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True, autoincrement= False)
    name = Column(String(30), nullable=False, unique=True)
    fifteenTest = Column(Double)
    forty_fiveTest = Column(Double)
    finalTest = Column(Double)
    students = relationship('Student', backref='subject', lazy=True)


class Year(db.Model):
    __tablename__ = 'year'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    students = relationship('Student', backref='year', lazy=True)
    def __str__(self):
        return self.name


class Student(db.Model):
    __tablename__ = 'student'
    MSHS = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=False)
    number = Column(String(30),nullable=False, unique=True)
    birth = Column(Date)
    gender = Column(String(30))
    address = Column(String(200), nullable=False)
    email = Column(String(50))
    image = Column(String(100))
    year_id = Column(Integer, ForeignKey(Year.id), nullable=False)
    class_id = Column(Integer, ForeignKey(Class.id), nullable=False)
    subject_id = Column(Integer, ForeignKey(Subject.id), nullable=False)

    def __str__(self):
        return self.name


# class BaseModel(db.Model):
#     __abstract__ = True
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     active = Column(Boolean, default=True)
#     created_date = Column(DateTime, default=datetime.now())
#
#
# class Receipt(BaseModel):
#     user_id = Column(Integer, ForeignKey(User.id), nullable=True)
#     receipt_details = relationship('ReceiptDetails', backref='receipt', lazy=True)
#
#
# class ReceiptDetails(BaseModel):
#     quantity = Column(Integer, default=0)
#     price = Column(Float, default=0)
#     receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)
#     product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
#
#
# class Interaction(db.Model):
#     __abstract__ = True
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey(User.id), nullable=False)
#     product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
#
#
# class Comment(Interaction):
#     content = Column(String(255), nullable=False)
#     created_date = Column(DateTime, default=datetime.now())


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        #1
        # import hashlib
        # u = User(name='Admin', username='admin',
        #          password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #          user_role=UserRoleEnum.ADMIN)
        # db.session.add(u)
        # db.session.commit()

        # y1 = Year(name='KÌ I--2023-2024')
        # y2 = Year(name='KÌ II--2023-2024')
        #
        # db.session.add(y1)
        # db.session.add(y2)
        # db.session.commit()

        # c1 = Class(name='Khối 10', quantity='5')
        # c2 = Class(name='Khối 11', quantity='6')
        # c3 = Class(name='Khối 12', quantity='7')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)

        # sub1 = Subject(name='Math', fifteenTest=8.0, forty_fiveTest=8.0, finalTest=8.0)
        # sub2 = Subject(name='Literature', fifteenTest=8.0, forty_fiveTest=8.0, finalTest=8.0)
        # sub3 = Subject(name='English', fifteenTest=8.0, forty_fiveTest=8.0, finalTest=8.0)
        #
        # db.session.add(sub1)
        # db.session.add(sub2)
        # db.session.add(sub3)
        #2

        s1 = Student(name='Nguyễn Thị Minh Anh', MSHS=101, number='1122334455', birth='2006-12-12',gender='Female', address='99 Pham Van Dong Street, Go Vap District, Ho Chi Minh City', email='minhanh@gmail.com', year_id=1, class_id= 3, subject_id= 1,
                     image='https://res.cloudinary.com/du5yfxccw/image/upload/v1704394415/m1ctsthqlha7sm6kcatu.png')
        s2 = Student(name='Nguyễn Thị Ngọc Anh', MSHS=201, number='5566778899', birth='2008-12-01', gender='Female', address='100 Pham Van Dong Street, Go Vap District, Ho Chi Minh City', email='ngocanh@gmail.com', year_id=2, class_id= 1, subject_id= 2,
                     image='https://res.cloudinary.com/du5yfxccw/image/upload/v1704394415/m1ctsthqlha7sm6kcatu.png')
        s3 = Student(name='Trần Văn Bình', MSHS=102, number='2233445566', birth='2007-12-25', gender='Male', address='101 Pham Van Dong Street, Go Vap District, Ho Chi Minh City', email='vanbinh@gmail.com', year_id=1, class_id= 2, subject_id= 3,
                     image='https://res.cloudinary.com/du5yfxccw/image/upload/v1704394415/m1ctsthqlha7sm6kcatu.png')
        s4 = Student(name='Trần Văn Tính', MSHS=202, number='6677889911', birth='2008-12-04', gender='Male', address='102 Pham Van Dong Street, Go Vap District, Ho Chi Minh City', email='vantinh@gmail.com', year_id=2, class_id= 1, subject_id= 1,
                     image='https://res.cloudinary.com/du5yfxccw/image/upload/v1704394415/m1ctsthqlha7sm6kcatu.png')
        s5 = Student(name='Đỗ Thị Bình An', MSHS=103, number='3344556677', birth='2008-10-30', gender='Female', address='103 Pham Van Dong Street, Go Vap District, Ho Chi Minh City', email='binhan@gmail.com', year_id=1, class_id= 1, subject_id= 2,
                     image='https://res.cloudinary.com/du5yfxccw/image/upload/v1704394415/m1ctsthqlha7sm6kcatu.png')
        s6 = Student(name='Đỗ Thị Ngọc Bích', MSHS=203, number='7788991122', birth='2007-10-28', gender='Female', address='104 Pham Van Dong Street, Go Vap District, Ho Chi Minh City', email='ngocbich@gmail.com', year_id=2, class_id= 2, subject_id= 3,
                     image='https://res.cloudinary.com/du5yfxccw/image/upload/v1704394415/m1ctsthqlha7sm6kcatu.png')

        db.session.add_all([s1, s2, s3, s4, s5, s6])
        db.session.commit()
