import webapp2
import jinja2
import os

from google.appengine.ext import ndb

class Post(ndb.Model):
    message = ndb.StringProperty()
    username = ndb.StringProperty()
    created_time = ndb.DateTimeProperty(auto_now_add=True)

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


class MainPage(webapp2.RequestHandler):
    def get(self):
        posts = Post.query().fetch()
        post_query = Post.query()
        post_query = post_query.order(Post.created_time)
        templateVars = {
            'posts' : posts,
        }
        template = env.get_template('/templates/cssiwall.html')
        self.response.write(template.render(templateVars))

    def post(self):
        message = self.request.get('message')
        username = self.request.get('username')
        post = Post(message=message, username=username)
        post.put()
        self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', MainPage),


], debug=True)
