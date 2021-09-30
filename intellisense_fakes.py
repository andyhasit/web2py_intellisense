#!/usr/bin/python
#-*- coding: utf-8 -*-
#  This file defines a number of fake global variables commonly used in web2py,
#  simply to provide auto-completion support in an IDE.
#  For the "db" oject it provides fakes all the way down to table's field's attributes:
#  db.my_table.my_field.represent
#  For other objects like "response" and "request" you get what you get.
#  It is rebuilt from a running copy of db by the function generate_auto_completion_file()
#  which is most likely in the auto_completion_support.py file in modules.
#
from gluon import *
from gluon.globals import *



class Auth_user:
    def  __init__(self):
        self.id = Field("dummy")
        self.first_name = Field("dummy")
        self.last_name = Field("dummy")
        self.email = Field("dummy")
        self.password = Field("dummy")
        self.registration_key = Field("dummy")
        self.reset_password_key = Field("dummy")
        self.registration_id = Field("dummy")

    def insert(self, id=None, first_name=None, last_name=None, email=None, password=None, registration_key=None, reset_password_key=None, registration_id=None):
        pass


class Auth_group:
    def  __init__(self):
        self.id = Field("dummy")
        self.role = Field("dummy")
        self.description = Field("dummy")

    def insert(self, id=None, role=None, description=None):
        pass


class Auth_membership:
    def  __init__(self):
        self.id = Field("dummy")
        self.user_id = Field("dummy")
        self.group_id = Field("dummy")

    def insert(self, id=None, user_id=None, group_id=None):
        pass


class Auth_permission:
    def  __init__(self):
        self.id = Field("dummy")
        self.group_id = Field("dummy")
        self.name = Field("dummy")
        self.table_name = Field("dummy")
        self.record_id = Field("dummy")

    def insert(self, id=None, group_id=None, name=None, table_name=None, record_id=None):
        pass


class Auth_event:
    def  __init__(self):
        self.id = Field("dummy")
        self.time_stamp = Field("dummy")
        self.client_ip = Field("dummy")
        self.user_id = Field("dummy")
        self.origin = Field("dummy")
        self.description = Field("dummy")

    def insert(self, id=None, time_stamp=None, client_ip=None, user_id=None, origin=None, description=None):
        pass


class Auth_cas:
    def  __init__(self):
        self.id = Field("dummy")
        self.user_id = Field("dummy")
        self.created_on = Field("dummy")
        self.service = Field("dummy")
        self.ticket = Field("dummy")
        self.renew = Field("dummy")

    def insert(self, id=None, user_id=None, created_on=None, service=None, ticket=None, renew=None):
        pass


class Course:
    def  __init__(self):
        self.id = Field("dummy")
        self.title = Field("dummy")

    def insert(self, id=None, title=None):
        pass


class Course_section:
    def  __init__(self):
        self.id = Field("dummy")
        self.title = Field("dummy")

    def insert(self, id=None, title=None):
        pass


class Course_lesson:
    def  __init__(self):
        self.id = Field("dummy")
        self.title = Field("dummy")
        self.lesson_path = Field("dummy")

    def insert(self, id=None, title=None, lesson_path=None):
        pass


class Course_section_in_course:
    def  __init__(self):
        self.id = Field("dummy")
        self.course_section = Field("dummy")
        self.course = Field("dummy")
        self.position_in_list = Field("dummy")

    def insert(self, id=None, course_section=None, course=None, position_in_list=None):
        pass


class Course_lesson_in_section:
    def  __init__(self):
        self.id = Field("dummy")
        self.course_lesson = Field("dummy")
        self.course_section = Field("dummy")
        self.position_in_list = Field("dummy")

    def insert(self, id=None, course_lesson=None, course_section=None, position_in_list=None):
        pass


class Course_session:
    def  __init__(self):
        self.id = Field("dummy")
        self.course = Field("dummy")
        self.start_date = Field("dummy")
        self.end_date = Field("dummy")
        self.venue = Field("dummy")

    def insert(self, id=None, course=None, start_date=None, end_date=None, venue=None):
        pass


class User_in_course:
    def  __init__(self):
        self.id = Field("dummy")
        self.course = Field("dummy")
        self.auth_user = Field("dummy")
        self.date_enrolled = Field("dummy")

    def insert(self, id=None, course=None, auth_user=None, date_enrolled=None):
        pass


class User_in_course_session:
    def  __init__(self):
        self.id = Field("dummy")
        self.course = Field("dummy")
        self.auth_user = Field("dummy")
        self.course_session = Field("dummy")

    def insert(self, id=None, course=None, auth_user=None, course_session=None):
        pass


class User_lesson_status:
    def  __init__(self):
        self.id = Field("dummy")
        self.course_lesson = Field("dummy")
        self.auth_user = Field("dummy")
        self.status = Field("dummy")
        self.answer = Field("dummy")
        self.notes = Field("dummy")

    def insert(self, id=None, course_lesson=None, auth_user=None, status=None, answer=None, notes=None):
        pass


class FakeDAL(DAL):
    def  __init__(self):
        self.auth_user = Auth_user()
        self.auth_group = Auth_group()
        self.auth_membership = Auth_membership()
        self.auth_permission = Auth_permission()
        self.auth_event = Auth_event()
        self.auth_cas = Auth_cas()
        self.course = Course()
        self.course_section = Course_section()
        self.course_lesson = Course_lesson()
        self.course_section_in_course = Course_section_in_course()
        self.course_lesson_in_section = Course_lesson_in_section()
        self.course_session = Course_session()
        self.user_in_course = User_in_course()
        self.user_in_course_session = User_in_course_session()
        self.user_lesson_status = User_lesson_status()


class FakeSession(Session):
    def  __init__(self):
        pass
session = FakeSession()

class FakeResponse(Response):
    def  __init__(self):
        pass
response = FakeResponse()

class FakeRequest(Request):
    def  __init__(self):
        pass
request = FakeRequest()

class FakeAuth(Auth):
    def  __init__(self):
        pass
auth = FakeAuth()

db = FakeDAL()

__all__ = ['db', 'session', 'response', 'request', 'auth',]
