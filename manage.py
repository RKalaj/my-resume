from flask_script import Manager
from myresume import app, db, Courses, Prof

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    harry = Prof(name='Harry Wang', department='MIS')
    junbo = Prof(name='Junbo Son', department='MIS')
    jillian = Prof(name='Jillian Pratt', department='ACCT')
    susan = Prof(name='Susan Murphy', department='OM')
    misy350 = Courses(number='MISY350', title='Business Application Development II', desc='Covers concepts related to client side development, including cascading style sheets and JavaScript.', prof=harry)
    buad345 = Courses(number='BUAD345', title='Decision Analytics and Visualization', desc='Analytics leverages both the proliferation of data and the advancement of computational tools to bring a new level of sophistication to business decision making. As part of developing an analytic mind and skillset, this course teaches students to properly frame decision problems, represent and understand how to manage uncertainty inherent in those problems, manipulate large data sets using modern software to prescribe recommended actions, and to then compel organizational change through data visualizations.', prof=junbo)
    acct352 = Courses(number='ACCT352', title='Law and Social Issues in Business', desc='Focuses on the legal environment of business, including objectives of the law, sources of the law, regulatory and judicial process, and effect of government and society on the formation and evolution of the law.', prof=junbo)
    buad306 = Courses(number='BUAD306', title='Service and Operations Management', desc='Analysis of major problems faced by operations managers at different levels of management. Topics include scheduling, forecasting, process design, inventory management and quality management.', prof=junbo)
    db.session.add(misy350)
    db.session.add(buad345)
    db.session.add(acct352)
    db.session.add(buad306)
    db.session.add(harry)
    db.session.add(junbo)
    db.session.add(jillian)
    db.session.add(susan)
    db.session.commit()


if __name__=='__main__':
    manager.run()
