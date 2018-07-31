import webapp2
import jinja2
import os
import random

from google.appengine.ext import ndb
from google.appengine.api import users

class Student(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    birthday = ndb.DateProperty()
    #questions = ndb.StructuredProperty(Question, repeated=True)

class Answer(ndb.Model):
    student_key = ndb.KeyProperty()
    question = ndb.StringProperty()
    answer = ndb.IntegerProperty()

class Quote(ndb.Model):
    content = ndb.StringProperty()
    author = ndb.StringProperty()

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


class MainPage(webapp2.RequestHandler):
    def pickquote(self):
        randquote = Quote.query().get()
        return randquote
        #query looku for quotes in database. use random function
        #to pick random index in list, pick quote to return the quote that
        #was selected
    def get(self):
        login_url = ''
        logout_url = ''
        #current user will be a user object or NONE
        current_user = users.get_current_user()
        #if no one is logged in, show a login prompt
        if not current_user:
            login_url = users.create_login_url('/')
        else:
            logout_url = users.create_logout_url('/')
        # posts = Post.query().fetch()
        # post_query = Post.query()
        # post_query = post_query.order(Post.created_time)
        templateVars = {
            'current_user' : current_user,
            'login_url' : login_url,
            'logout_url' : logout_url,
            'quote' : self.pickquote(),
        }
        template = env.get_template('/templates/home.html')
        self.response.write(template.render(templateVars))

    # def post(self):
    #     message = self.request.get('message')
    #     username = self.request.get('username')
    #     post = Post(message=message, username=username)
    #     post.put()
    #     self.redirect('/')


class QuestionPage(webapp2.RequestHandler):
    def get(self):
        qs = [
            #question 1
            {
                'question' : 'blah blah blah',
                'answers' : ['a1', 'a2', 'a3'],
            },
            #question 2
            {
                'question' : 'blah blah blah',
                'answers' : ['a1', 'a2', 'a3'],
            },
        ]
        print("hi")
        template = env.get_template("/templates/qpg.html")
        self.response.write(template.render(qs=qs))

    #def post(self):


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/qpg', QuestionPage),



], debug=True)
