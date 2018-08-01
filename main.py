import webapp2
import jinja2
import os
import random

from google.appengine.ext import ndb
from google.appengine.api import users

class Student(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    #birthday = ndb.DateProperty()
    #questions = ndb.StructuredProperty(Question, repeated=True)

class Answer(ndb.Model):
    student_key = ndb.KeyProperty()
    question = ndb.StringProperty()
    answer = ndb.IntegerProperty()

class Quote(ndb.Model):
    content = ndb.StringProperty()
    author = ndb.StringProperty()
    # TODO(yojairo): Set an index on the quote and look up a random
    # quote by the index. Increment this index each time we add a quote
    # index = ndb.IntegerProperty()

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


class MainPage(webapp2.RequestHandler):
    #def pickquote(self):
        # TODO(yojairo): This is slow when we have a lot of quotes. Instead,
        # select a random index and get the Quote for that index.
        # randquotes = Quote.query().fetch()
        # randquote = random.choice(randquotes)
        # return randquote.content
        # return randquote.author
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
            #'quote' : self.pickquote(),
        }
        template = env.get_template('/templates/home.html')
        self.response.write(template.render(templateVars))

    def post(self):
        name = self.request.get('name') #<-- name is the name from the form
        email = users.get_current_user().email()
        student = Student(name=name, email=email)
        student.put()
        self.redirect('/')


class RedirectPage(webapp2.RequestHandler):
    def get (self):
        template = env.get_template("/templates/main.html")
        self.response.write(template.render())


class QuestionPage(webapp2.RequestHandler):
    def get(self):
        # qs = [
        #     #question 1
        #     {
        #         'question' : 'What is your name?',
        #         'answers' : ['a1', 'a2', 'a3'],
        #     },
        #     #question 2
        #     {
        #         'question' : 'blah blah blah',
        #         'answers' : ['a1', 'a2', 'a3'],
        #     },
        # ]
        template = env.get_template("/templates/qpg.html")
        self.response.write(template.render())

    def post(self):
        stage = self.request.get('stage')
        #intro
        if stage == 'intro':
            year = self.request.get('grade')
            if year == 'underclassman':
                template = env.get_template("templates/lowerq1.html")
                self.response.write(template.render())
            else:
                template = env.get_template("templates/upperq1.html")
                self.response.write(template.render())
        #study habits - lower
        elif stage == 'study':
            studyhabits = self.request.get('studyh')
            if  studyhabits == 'whenever' or studyhabits == 'not':
                template = env.get_template("templates/lowerresource1.html")
                self.response.write(template.render())
            else:
                template = env.get_template("templates/lowerq2.html")
                self.response.write(template.render())
        #extracurriculars - lower
        elif stage == 'extracurriculars':
            excs = self.request.get('ecs')
            if  excs == 'no':
                template = env.get_template("templates/lowerresource2.html")
                self.response.write(template.render())
            else:
                template = env.get_template("templates/lowerq3.html")
                self.response.write(template.render())
        #classes - lower
        elif stage == 'classes':
            classes = self.request.get('classes')
            if  classes == 'not':
                template = env.get_template("templates/lowerresource3.html")
                self.response.write(template.render())
            else:
                template = env.get_template("templates/lowerq4.html")
                self.response.write(template.render())
        #psat - lower
        elif stage == 'psat':
            psat = self.request.get('psat')
            if  psat == 'no':
                template = env.get_template("templates/lowerresource4.html")
                self.response.write(template.render())
            else:
                template = env.get_template("templates/lowerq5.html")
                self.response.write(template.render())
        #careers - lower
        elif stage == 'careers':
            career = self.request.get('career')
            if  career == 'no':
                template = env.get_template("templates/lowerresource5.html")
                self.response.write(template.render())
            else:
                template = env.get_template("templates/lowerq6.html")
                self.response.write(template.render())
#######upper######
        #applying - upper
        elif stage == 'applying':
                apply = self.request.get('apply')
                if  apply == 'notstarted':
                    template = env.get_template("templates/lowerresource1.html")
                    self.response.write(template.render())
                else:
                    template = env.get_template("templates/upperq2.html")
                    self.response.write(template.render())
        #scholarships - upper
        elif stage == 'scholarships':
                funds = self.request.get('funds')
                if  funds == 'havenot':
                    template = env.get_template("templates/lowerresource2.html")
                    self.response.write(template.render())
                else:
                    template = env.get_template("templates/upperq3.html")
                    self.response.write(template.render())
            #SAT - upper
        elif stage == 'SAT':
                testing = self.request.get('testing')
                if  testing == 'no':
                    template = env.get_template("templates/lowerresource3.html")
                    self.response.write(template.render())
                else:
                    template = env.get_template("templates/upperq4.html")
                    self.response.write(template.render())
            #campus - upper
        elif stage == 'campus':
                place = self.request.get('place')
                if  place == 'no':
                    template = env.get_template("templates/lowerresource4.html")
                    self.response.write(template.render())
                else:
                    template = env.get_template("templates/upperq5.html")
                    self.response.write(template.render())
            #essays - upper
        elif stage == 'essays':
                essay = self.request.get('essay')
                if  essay == 'havenot':
                    template = env.get_template("templates/lowerresource5.html")
                    self.response.write(template.render())
                else:
                    template = env.get_template("templates/upperq6.html")
                    self.response.write(template.render())
            #FAFSA - upper
        elif stage == 'FAFSA':
                finaid = self.request.get('finaid')
                if  finaid == 'notstarted':
                    template = env.get_template("templates/lowerresource5.html")
                    self.response.write(template.render())
                else:
                    template = env.get_template("templates/lowerq6.html")
                    self.response.write(template.render())



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/qpg', QuestionPage),
    ('/redirect', RedirectPage),



], debug=True)
