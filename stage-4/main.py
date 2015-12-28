import os
import jinja2
import webapp2
import cgi
import webbrowser

from collections import namedtuple
from datetime import datetime

from google.appengine.api import users
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), "templates")

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

Lesson = namedtuple("Lesson", ["lesson_id", "lesson_number", "lesson_title"])
Concept = namedtuple("Concept", ["concept_id", "concept_title", "concept_description"])

lessons = [
          Lesson(1, "lesson-1", "Lesson 1: Understanding of Servers"),
          Lesson(2, "lesson-2", "Lesson 2: Importance of Validating Input"),
          Lesson(3, "lesson-3", "Lesson 3: HTML Templates and Abstraction")
          ]

concepts = [
            [Concept("lesson-1-1", "yada yada", "yada yada yada"),
            Concept("lesson-1-2", "yada yada", "yada yada yada"),
            Concept("lesson-1-3", "yada yada", "yada yada yada")],
            
            [Concept("lesson-2-1", "hada hada", "hada hada hada"),
            Concept("lesson-2-2", "hada hada", "hada hada hada"),
            Concept("lesson-2-3", "hada hada", "hada hada hada")],
            
            [Concept("lesson-3-1", "mada mada", "mada yada yada"),
            Concept("lesson-3-2", "mada mada", "mada yada yada"),
            Concept("lesson-3-3", "mada mada", "<span>mada yada yada</span>")]
            ]

DEFAULT_COMMENTS = "Comments"

def comments_key(comments_name=DEFAULT_COMMENTS):
  """Constructs a Datastore key for a comment entity.

  We use comments_name as the key.
  """
  return ndb.Key("Comments", comments_name)

class Author(ndb.Model):
  """Sub model for representing an author."""
  identity = ndb.StringProperty(indexed=True)
  name = ndb.StringProperty(indexed=False)
  email = ndb.StringProperty(indexed=False)

class Comment(ndb.Model):
  """A main model for representing an individual comment."""
  author = ndb.StructuredProperty(Author)
  content = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)

class Handler(webapp2.RequestHandler):
  def write(self, *a, **kw):
      self.response.out.write(*a, **kw)

  def render_str(self, template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

  def render(self, template, **kw):
    self.write(self.render_str(template, **kw))

class MainPage(Handler):
  def get(self):
    comments_name = DEFAULT_COMMENTS

    # [START query]
    comments_query = Comment.query(ancestor = comments_key(comments_name)).order(-Comment.date)
    comments = comments_query.fetch()
    # [END query]

    # If a person is logged into Google's Services
    user = users.get_current_user()
    if user:
      url = users.create_logout_url(self.request.uri)
      url_linktext = "Logout"
      user_name = user.nickname()
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = "Login"
      user_name = "Anonymous"

    self.render("notes.html", lessons = lessons, concepts = concepts, user_name = user_name,
                url = url, url_linktext = url_linktext, comments = comments)

class CommentPage(webapp2.RequestHandler):
  def post(self):
    comments_name = DEFAULT_COMMENTS
    comment = Comment(parent=comments_key(comments_name))

    # When the person is making the post, check to see whether the person is logged into Google
    if users.get_current_user():
      comment.author = Author(identity=users.get_current_user().user_id(),
                           name=users.get_current_user().nickname(),
                           email=users.get_current_user().email())
    else:
      comment.author = Author(name="anonymous@anonymous.com",
                           email="anonymous@anonymous.com")

    # Get the content from our request parameters, in this case, the message
    # is in the parameter "content"
    comment.content = self.request.get("content")

    if not comment.content:
      webbrowser.open("http://www.youtube.com/watch?v=e-ORhEE9VVg&feature=youtu.be&t=1m23s")
      self.redirect("/?" + comments_name + "#comment-section")
    else:
      # Write to the Google Database
      comment.put()
      webbrowser.open('http://www.google.com')
      # Redirect to the comments section after posting a comment
      self.redirect("/?" + comments_name + "#comment-section")

app = webapp2.WSGIApplication([("/", MainPage),
                               ("/post-comment", CommentPage)],
                               debug=True)
