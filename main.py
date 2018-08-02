import webapp2
import jinja2
import os
import random
import logging

from google.appengine.ext import ndb
from google.appengine.api import users

class Student(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    #birthday = ndb.DateProperty()
    #questions = ndb.StructuredProperty(Question, repeated=True)

# class Answer(ndb.Model):
#     student_key = ndb.KeyProperty()
#     question = ndb.StringProperty()
#     answer = ndb.IntegerProperty()

class Quote(ndb.Model):
    content = ndb.StringProperty()
    author = ndb.StringProperty()
    # TODO(yojairo): Set an index on the quote and look up a random
    # quote by the index. Increment this index each time we add a quote
    # index = ndb.IntegerProperty()
class Resource(ndb.Model):
    student_key = ndb.KeyProperty()
    #name = ndb.StringProperty()
    description = ndb.StringProperty()
    url = ndb.StringProperty()

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

    # def post(self):
    #     name = self.request.get('name') #<-- name is the name from the form
    #     email = users.get_current_user().email()
    #     logging.info('I am here')
    #     #logging.info(Student.query().filter(Student.email == email).get())
    #     #if not Student.query().filter(Student.email == email).get():
    #     student = Student(name=name, email=email)
    #     student.put()
    #     self.redirect('/')


class ChecklistPage(webapp2.RequestHandler):
    def get (self):
        email = users.get_current_user().email()
        current_student_key = Student.query().filter(Student.email == email).get().key
        resource_list = Resource.query().filter(Resource.student_key == current_student_key).fetch()

        templateVars = {
            'resource_list' : resource_list,

        }
        template = env.get_template("/templates/checklist.html")
        self.response.write(template.render(templateVars))

class ResourceHandler(webapp2.RequestHandler):
    def post(self):
        resource_name = self.request.body
        logging.info(resource_name)
        email = users.get_current_user().email()
        current_student = Student.query().filter(Student.email == email).get()
        if current_student and resource_name == 'study tips':
            Resource(student_key=current_student.key, description='Study Tips', url='https://blog.prepscholar.com/how-to-study-better-in-high-school').put()

class QuestionPage(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("/templates/qpg.html")
        self.response.write(template.render())

    def post(self):
        stage = self.request.get('stage')
        email = users.get_current_user().email()
        current_student = Student.query().filter(Student.email == email).get()
        #intro
        if stage == 'intro':
            name = self.request.get('name') #<-- name is the name from the form

            #logging.info('I am here')
            if not current_student:
                student = Student(name=name, email=email)
                student.put()

            year = self.request.get('grade')
            if year == 'underclassman':
                template = env.get_template("templates/lowerq1.html")
                self.response.write(template.render())
            else:
                template = env.get_template("templates/upperq1.html")
                self.response.write(template.render())
        #study habits - lower
        elif stage == 'study':
            logging.info('working')
            studyhabits = self.request.get('studyh')
            tips = 'Study Tips'
            resource_check = Resource.query().filter(Resource.student_key == current_student.key).filter(Resource.description == tips).get()

            if studyhabits == 'whenever' or studyhabits == 'not':
                if not resource_check:
                    Resource(student_key=current_student.key, description=tips, url='https://blog.prepscholar.com/how-to-study-better-in-high-school').put()
                template = env.get_template("templates/lowerresource1.html")
                self.response.write(template.render())
            else:
                template = env.get_template("templates/lowerq2.html")
                self.response.write(template.render())
        #extracurriculars - lower
        elif stage == 'extracurriculars':
            excs = self.request.get('ecs')
            ecs = 'Extracurriculars'
            resource_check = Resource.query().filter(Resource.student_key == current_student.key).filter(Resource.description == ecs).get()

            if excs == 'no':
                if not resource_check:
                    Resource(student_key=current_student.key, description=ecs, url='https://www.fastweb.com/student-life/articles/impressive-extracurriculars').put()
                template = env.get_template("templates/lowerresource2.html")
                self.response.write(template.render())
            else:
                template = env.get_template("templates/lowerq3.html")
                self.response.write(template.render())
        #classes - lower
        elif stage == 'classes':
            classes = self.request.get('classes')
            classdescription = 'Classes'
            resource_check = Resource.query().filter(Resource.student_key == current_student.key).filter(Resource.description == classdescription).get()

            if classes == 'not':
                if not resource_check:
                    Resource(student_key=current_student.key, description=classdescription, url='https://apstudent.collegeboard.org/apcourse').put()
                template = env.get_template("templates/lowerresource3.html")
                self.response.write(template.render())
            else:
                template = env.get_template("templates/lowerq4.html")
                self.response.write(template.render())
        #psat - lower
        elif stage == 'psat':
            psat = self.request.get('psat')
            psatdescription = 'PSAT'
            resource_check = Resource.query().filter(Resource.student_key == current_student.key).filter(Resource.description == psatdescription).get()
            if  psat == 'no':
                if not resource_check:
                    Resource(student_key=current_student.key, description=psatdescription, url='https://collegereadiness.collegeboard.org/psat-nmsqt-psat-10/inside-the-test').put()
                template = env.get_template("templates/lowerq5.html")
                self.response.write(template.render())
            else:
                template = env.get_template("templates/lowerq5.html")
                self.response.write(template.render())
        #careers - lower
        elif stage == 'careers':
            career = self.request.get('career')
            careerdescription = 'Career Quiz'
            resource_check = Resource.query().filter(Resource.student_key == current_student.key).filter(Resource.description == careerdescription).get()
            if  career == 'no':
                if not resource_check:
                    Resource(student_key=current_student.key, description=careerdescription, url='https://www.princetonreview.com/quiz/career-quiz').put()
                template = env.get_template("templates/lowerresource5.html")
                self.response.write(template.render())
            else:
                template = env.get_template("templates/lowerq6.html")
                self.response.write(template.render())
#######upper######
        #applying - upper
        elif stage == 'applying':
                apply = self.request.get('apply')
                applicationdescription = 'Application Resources'
                resource_check = Resource.query().filter(Resource.student_key == current_student.key).filter(Resource.description == applicationdescription).get()
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
    #('/redirect', RedirectPage),
    ('/resource', ResourceHandler),
    ('/checklist', ChecklistPage),



], debug=True)
