from flask_script import Manager
from resume import app, db, Professor, Course


manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    wang = Professor(name='Jiannan Wang', department='Accounting & MIS')
    dragone = Professor(name='Debra Sue Gassner Dragone', department='Accounting & MIS')
    lynch = Professor(name='Christopher Michael Lynch', department='Finance')
    serva = Professor(name='Mark A. Serva', department='Accounting & MIS')
    course1 = Course(course_number='MISY 350', title='Web Application Development', description='Covers concepts related to client side development, including cascading style sheets and JavaScript.')
    course2 = Course(course_number= 'ACCT 208', title='Accounting II', description=' Introduction to managerial accounting.')
    course3 = Course(course_number='FINC 311', title='Principles of Finance', description='Introduces fundamental techniques and concepts related to the financial management of business firms.')
    course4 = Course(course_number='MISY 330', title='Database Design & Implementation', description='Covers the design and implementation of enterprise databases in the business environment.')
    db.session.add(wang)
    db.session.add(dragone)
    db.session.add(lynch)
    db.session.add(serva)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
