import os
import jinja2
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from content import stages

template_dir = os.path.join(os.path.dirname(__file__), "templates")

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))


def comments_key(comments_name):
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
        """Creates a Jinja template and stores it in 't'."""
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    """Displays the home page using a get request."""
    def get(self):
        self.render("main_page.html", stages=stages)


class StageNotes(Handler):
    """Displays a stage notes page using a get request."""
    def get(self):
        # Set comments name key to the stage number of the current page
        current_path = self.request.path
        current_stage_number = current_path[7]
        comments_name = "stage-" + current_stage_number + "-comments"

        # [START query]
        comments_query = Comment.query(ancestor=comments_key(comments_name)).order(-Comment.date)
        comments = comments_query.fetch()
        # [END query]

        # Set login/logout display information by checking the user's present
        # state in Google's Services
        user = users.get_current_user()
        if user:
            user_url = users.create_logout_url(self.request.uri)
            user_url_linktext = "Logout"
            user_name = user.nickname()
        else:
            user_url = users.create_login_url(self.request.uri)
            user_url_linktext = "Login"
            user_name = "Anonymous"

        # Initialize the error variable if its query parameter is present
        error = self.request.get("error")

        self.render("comments.html", current_path=current_path,
                    comments=comments, user=user, user_url=user_url,
                    user_url_linktext=user_url_linktext, user_name=user_name,
                    error=error, stages=stages)

    def post(self):
        """Posts a comment on the notes page using a post request."""
        # Set comments name key to the stage number of the current page
        current_path = self.request.path
        current_stage_number = current_path[7]
        comments_name = "stage-" + current_stage_number + "-comments"

        comment = Comment(parent=comments_key(comments_name))

        # When the person is making the post, check to see whether the person
        # is logged into Google
        if users.get_current_user():
            comment.author = Author(identity=users.get_current_user().user_id(),
                                    name=users.get_current_user().nickname(),
                                    email=users.get_current_user().email())
        else:
            comment.author = Author(name="anonymous@anonymous.com",
                                    email="anonymous@anonymous.com")

        # Get the content from our request parameters, in this case,
        # the message is in the parameter "content"
        comment.content = self.request.get("content")

        if not comment.content:
            # Redirect to the comments section of the current notes page with
            # the error query parameter
            error = "&error=error"
            self.redirect(current_path + "?" + comments_name + error +
                          "#comment-section")
        else:
            # Write to the Google Database
            comment.put()
            # Redirect to the comments section after posting a comment
            self.redirect("?" + comments_name + "#comment-section")


app = webapp2.WSGIApplication([("/*", MainPage),
                               ("/stage-[1-5]-notes/", StageNotes)],
                              debug=True)
