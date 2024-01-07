from app.stu import Year,Class,Subject, Student, User
from app import app, db
import hashlib
from flask_login import current_user
from sqlalchemy import func
import cloudinary.uploader


def load_years():
    return Year.query.all()
    # return [{
    #     'id': 1,
    #     'name': 'Kì I - Năm học:2023-2024'
    # }, {
    #     'id': 2,
    #     'name': 'Kì II - Năm học:2023-2024'
    # }]

def load_classes():
    # return Class.query.all()
    return [{
        'id':1,
        'name':' Khối 10',
        'quantity':5
    }, {
        'id': 2,
        'name': ' Khối 11',
        'quantity':6
    }, {
        'id': 3,
        'name': ' Khối 12',
        'quantity': 7
    }]

def load_subjects():
     # return Subject.query.all()
    return [{
        'id': 1,
        'name': 'Math',
        'fifteenTest': 8.0,
        'forty_fiveTest': 8.0,
        'finalTest': 8.0
    }, {
        'id': 2,
        'name': 'Literature',
        'fifteenTest': 8.0,
        'forty_fiveTest': 8.0,
        'finalTest': 8.0
    }, {
        'id': 3,
        'name': 'English',
        'fifteenTest': 8.0,
        'forty_fiveTest': 8.0,
        'finalTest': 8.0
    }]

def load_students(kw=None, year_id=None, page=None):
    # students = Student.query
    students = [{
        'MSHS': 101,
        'name': 'Nguyễn Thị Minh Anh',
        'number':'1122334455',
        'birth': '2006-12-12',
        'gender': 'Female',
        'address': '99 Pham Van Dong Street, Go Vap District, Ho Chi Minh City',
        'email': 'minhanh@gmail.com',
        'image': 'https://res.cloudinary.com/du5yfxccw/image/upload/v1704394415/m1ctsthqlha7sm6kcatu.png'
    }, {
        'MSHS': 201,
        'name': 'Nguyễn Thị Ngọc Anh',
        'number': '5566778899',
        'birth': '2008-12-01',
        'gender': 'Female',
        'address': '100 Pham Van Dong Street, Go Vap District, Ho Chi Minh City',
        'email': 'ngocanh@gmail.com',
        'image': 'https://res.cloudinary.com/du5yfxccw/image/upload/v1704394415/m1ctsthqlha7sm6kcatu.png'
    }, {
        'MSHS': 102,
        'name': 'Trần Văn Bình',
        'number':'2233445566',
        'birth': '2007-12-25',
        'gender': 'Male',
        'address': '101 Pham Van Dong Street, Go Vap District, Ho Chi Minh City',
        'email': 'vanbin@gmail.com',
        'image': 'https://res.cloudinary.com/du5yfxccw/image/upload/v1704394415/m1ctsthqlha7sm6kcatu.png'
    }, {
        'MSHS': 202,
        'name': 'Trần Văn Tính',
        'number':'6677889911',
        'birth': '2008-12-04',
        'gender': 'Male',
        'address': '102 Pham Van Dong Street, Go Vap District, Ho Chi Minh City',
        'email': 'vantinh@gmail.com',
        'image': 'https://res.cloudinary.com/du5yfxccw/image/upload/v1704394415/m1ctsthqlha7sm6kcatu.png'
    }, {
        'MSHS': 103,
        'name': 'Đỗ Thị Bình An',
        'number':'3344556677',
        'birth': '2008-10-30',
        'gender': 'Female',
        'address': '103 Pham Van Dong Street, Go Vap District, Ho Chi Minh City',
        'email': 'binhan@gmail.com',
        'image': 'https://res.cloudinary.com/du5yfxccw/image/upload/v1704394415/m1ctsthqlha7sm6kcatu.png'
    }, {
        'MSHS': 203,
        'name': 'Đỗ Thị Ngọc Bích',
        'number':'7788991122',
        'birth': '2007-10-28',
        'gender': 'Female',
        'address': '104 Pham Van Dong Street, Go Vap District, Ho Chi Minh City',
        'email': 'ngocbich@gmail.com',
        'image': 'https://res.cloudinary.com/du5yfxccw/image/upload/v1704394415/m1ctsthqlha7sm6kcatu.png'
    }]

    if kw:
        students = [s for s in students if s['name'].find(kw) >= 0]

    if year_id:
        students = students.filter(Student.year_id.__eq__(year_id))

    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1) * page_size

        return students.slice(start, start + page_size)

    # return students.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)


#
#
# def count_product():
#     return Product.query.count()
#
#
def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()


# def add_receipt(cart):
#     if cart:
#         receipt = Receipt(user=current_user)
#         db.session.add(receipt)
#
#         for c in cart.values():
#             d = ReceiptDetails(quantity=c['quantity'], price=c['price'], product_id=c['id'], receipt=receipt)
#             db.session.add(d)
#
#         db.session.commit()
#
#
# def add_user(name, username, password, avatar):
#     password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
#     u = User(name=name, username=username, password=password)
#
#     if avatar:
#         res = cloudinary.uploader.upload(avatar)
#         print(res)
#         u.avatar = res['secure_url']
#
#     db.session.add(u)
#     db.session.commit()
#
#
def count_students():
    return db.session.query(Student).count()

#
# def revenue_stats(kw=None):
#     query = db.session.query(Product.id, Product.name, func.sum(ReceiptDetails.quantity*ReceiptDetails.price))\
#                       .join(ReceiptDetails, ReceiptDetails.product_id==Product.id)
#
#     if kw:
#         query = query.filter(Product.name.contains(kw))
#
#     return query.group_by(Product.id).all()
#
#
# def revenue_mon_stats(year=2024):
#     query = db.session.query(func.extract('month', Receipt.created_date),
#                              func.sum(ReceiptDetails.quantity*ReceiptDetails.price))\
#                       .join(ReceiptDetails, ReceiptDetails.receipt_id.__eq__(Receipt.id))\
#                       .filter(func.extract('year', Receipt.created_date).__eq__(year))\
#                       .group_by(func.extract('month', Receipt.created_date))
#     return query.all()
#
#
# def get_product_by_id(id):
#     return Product.query.get(id)
#
#
# def get_comments_by_product(product_id):
#     return Comment.query.filter(Comment.product_id.__eq__(product_id)).all()
#
#
# def add_comment(product_id, content):
#     c = Comment(product_id=product_id, content=content, user=current_user)
#     db.session.add(c)
#     db.session.commit()
#
#     return c


if __name__ == '__main__':
    with app.app_context():
        print(count_students())
