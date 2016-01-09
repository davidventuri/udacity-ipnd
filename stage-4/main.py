import os
import jinja2
import webapp2
from collections import namedtuple
from google.appengine.api import users
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), "templates")

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

Stage = namedtuple("Stage", ["stage_number", "stage_title", "stage_url", "lessons", "concepts"])
Lesson = namedtuple("Lesson", ["lesson_number", "lesson_id", "lesson_title"])
Concept = namedtuple("Concept", ["concept_id", "concept_title",
                                 "concept_description"])

stage_1_lessons = []
stage_1_concepts = []

stage_2_lessons = []
stage_2_concepts = []

stage_3_lessons = []
stage_3_concepts = []

stage_5_lessons = []
stage_5_concepts = []

stage_4_lessons = [
          Lesson(1, "lesson-1", "Lesson 1: Understanding of Servers"),
          Lesson(2, "lesson-2", "Lesson 2: Importance of Validating Input"),
          Lesson(3, "lesson-3", "Lesson 3: HTML Templates and Abstraction")
          ]

stage_4_concepts = [
            [Concept("lesson-1-1", "The Request",
                     "<p>"
                       "Your browser sends an <span>HTTP request</span> to "
                       "the web server after you enter a URL into the browser "
                       "and the browser looks up the IP address for the domain"
                       " name entered."
                     "</p>"
                     "<p>"
                       "The <span>HTTP request line</span> has the following "
                       "form:"
                         "<ul>"
                           "<li>Method Path Version</li>"
                           "<li>GET http://udacity.com/ HTTP/1.1</li>"
                         "</ul>"
                     "</p>"
                     "<p>"
                       "Two of the most common methods are <span>GET requests"
                       "</span> and <span>POST requests</span>. A GET request "
                       "sends its parameters via the URL (e.g. "
                       "http://www.example.ca/page.html<span>?var1=value1"
                       "</span>), while a POST request sends its parameters in"
                       "the request body, just under the headers (<a href= '"
                       "http://igoro.com/archive/what-really-happens-when-you-"
                       "navigate-to-a-url/'>source</a>)."
                     "</p>"
                     "<p>"
                       "The request line is followed by a number of <span>"
                       "headers</span>, which provide information about the "
                       "request. Headers have the form 'name: value'. The "
                       "value can contain whitespace, however the name cannot."
                       " Some examples of headers are:"
                         "<ul>"
                           "<li>Host: udacity.com</li>"
                           "<li>User-Agent: Chrome</li>"
                         "</ul>"
                     "</p>"),
             Concept("lesson-1-2", "Handling the Request",
                     "<p>"
                       "The server receives the HTTP request and processes it."
                       " This processing step involves server software "
                       "deciding which <span>request handler</span> should be "
                       "executed to handle this request."
                     "</p>"
                     "<p>"
                       "A request handler is a program that reads the request "
                       "and generates HTML for the response based on the "
                       "information in the request."
                     "</p>"),
             Concept("lesson-1-3", "The Response",
                     "<p>"
                       "After handling the HTTP request, the server sends an "
                       "<span>HTTP response</span> to the browser. This "
                       "response contains the HTML for the requested web page."
                       " The response looks very similar to the request."
                     "</p>"
                     "<p>"
                       "The <span>status line</span> is the HTTP request line "
                       "of the HTTP response. The status line has the form:"
                         "<ul>"
                           "<li>Version Status code Reason phrase</li>"
                           "<li>HTTP/1.1 200 OK</li>"
                         "</ul>"
                     "</p>"
                     "<p>"
                       "The <span>status code</span> is a three-digit integer "
                       "that tells us whether or not the request was satisfied"
                       ". The first digit (between 1 and 5) defines the class "
                       "of the status code, where the following meanings are "
                       "observed (<a href='http://www.w3.org/Protocols/rfc2616"
                       "/rfc2616-sec6.html'>source</a>):"
                         "<ul>"
                           "<li>1xx: Informational. Request received, "
                           "continuing process.</li>"
                           "<li>2xx: Success. The action was successfully "
                           "received, understood, and accepted.</li>"
                           "<li>3xx: Redirection. Further action must be taken"
                           " in order to complete the request.</li>"
                           "<li>4xx: Client Error. The request contains bad "
                           "syntax or cannot be fulfilled.</li>"
                           "<li>5xx: Server Error. The server failed to "
                           "fulfill an apparently valid request.</li>"
                         "</ul>"
                     "</p>"
                     "<p>"
                       "Like the request line, the status line is followed by "
                       "a number of headers (e.g. Date, Server (analogous to "
                        "user agent), Content-Type (e.g. text/html))."
                     "</p>"
                     "<p>"
                       "There are two types of responses: <span>static</span> "
                       "and <span>dynamic</span>. Examples of static responses"
                       " are pre-written files and images. Dynamic responses "
                       "are pages built dynamically on the fly by programs "
                       "called web applications. Web applications live on a "
                       "web server, speak HTTP, and generate the content that"
                       " your browser requests."
                     "</p>"
                     "<p>"
                       "The browser then renders the HTML contained in the "
                       "response. This rendering starts before the browser has"
                       " received the entire HTML document."
                     "</p>")],

            [Concept("lesson-2-1", "Input Validation",
                     "<p>"
                       "Web applications are notorious for taking practically "
                       "any type of input, assuming that it's valid, and "
                       "processing it further. Not validating input is one of "
                       "the greatest mistakes that web application developers "
                       "can make (<a href='http://searchsoftwarequality.techta"
                       "rget.com/tip/The-importance-of-input-validation'>"
                       "source</a>)."
                     "</p>"
                     "<p>"
                       "<span>Input validation</span> means verifying on the "
                       "server side that we have received what we expected to "
                       "receive. After checking the input, the form either "
                       "points out that the user made an error, or assures "
                       "that the provided data is accurate."
                     "</p>"),
             Concept("lesson-2-2", "Security",
                     "<p>"
                       "Malicious users can send parameters with arbitrary "
                       "junk directly to our server, even if the forms on our "
                       "page limit user input options (e.g. checkbox or "
                        "dropdown list). This insertion of malformed data can "
                        "<span>confuse, crash, or make the web application "
                        "divulge too much information</span> to the attacker. "
                        "It is important that our server validates input to "
                        "diffuse these attacks and protect our information."
                     "</p>"
                     "<p>"
                       "<a href='http://searchsoftwarequality.techtarget.com/"
                       "tip/The-importance-of-input-validation'>This page</a> "
                       "has detailed information on several types of input "
                       "attacks and their consequences."
                     "</p>"),
             Concept("lesson-2-3", "User Experience",
                     "<p>"
                       "Input validation is important for user experience "
                       "because it provides a medium for conversation with "
                       "users and guides them through the difficult times of "
                       "errors and uncertainty (<a href='http://designmodo.com"
                       "/ux-form-validation/'>source</a>)."
                     "</p>"
                     "<p>"
                       "<span>HTML escaping</span> is also important for user "
                       "experience to ensure that the visual structure of the "
                       "web page is maintained."
                     "</p>")],

            [Concept("lesson-3-1", "Why Programmers Use Templates",
                     "<p>"
                       "Templates allow for the <span>separation</span> of "
                       "HTML code from other code (e.g. Python code). This "
                       "separation makes the code easier to read and maintain."
                     "</p>"
                     "<p>"
                       "Templates allow for the <span>modularization</span> of"
                       " code. Each part of the page (e.g. the head section, a"
                       " common header/footer, and the body section) can be "
                       "defined in separate sections and/or files. This "
                       "modular approach allows programmers to avoid "
                       "repetition. <a href='https://discussions.udacity.com/t"
                       "/why-and-how-adding-jinja-to-my-notes/42435/2'>"
                       "andrew_R</a> from the Udacity discussion forum has a "
                       "great anecdote for why templates are useful:"
                         "<p class='quote'>"
                           "Imagine you are building a site with 10 different "
                           "pages. They all have their own use, but certain "
                           "parts of each page are the same, like the HEADER "
                           "and the NAV MENU. From personal experience let me "
                           "tell you, maintaining the same bits of code across"
                           " all 10 HTML page files can become very, very "
                           "tedious. Let's say I change a link url in one NAV "
                           "MENU. Then, I have to go to each and every other "
                           "file and make the same change. And then whoops I "
                           "made a typo in that first change. Time to go back"
                           " to every single page and fix that same little "
                           "thing! You can probably feel my pain through the "
                           "computer screen."
                         "</p>"
                         "<p class='quote'>"
                           "Using templates makes that process much more "
                           "convenient. If all 10 pages inherit from the same "
                           "base.html template, and I make a change to a "
                           "common section like in the HEADER, I only need to "
                           "go to one file and make that change. The other "
                           "pages will inherit this stuff when the Jinja "
                           "program builds the actual HTML pages."
                         "</p>"
                     "</p>"),
             Concept("lesson-3-2", "How Templates Help Programmers Avoid "
                                   "Repetition",
                     "<p>"
                       "Templates are like an HTML page <span>skeleton</span>."
                       " As mentioned above, a template will define certain "
                       "parts of the page. Other pages can then <span>inherit"
                       "</span> or <span>extend</span> from that template. "
                       "This allows the page to inherit everything that was "
                       "defined in the template plus the content the page "
                       "itself defines."
                     "</p>"
                     "<p>"
                       "Inside of the template files, we can specify locations"
                       " in the code that change the resulting HTML page "
                       "<span>depending on the variables we pass into the "
                       "template</span>. This feature allows us to 1) pass in "
                       "lists of variable length using for or while loops and "
                       "2) use logical statements to pass in variables in some"
                       " scenarios but not in others."
                     "</p>"),
             Concept("lesson-3-3", "The Importance of Avoiding Repetition",
                     "<p>"
                       "The name of the programming game is <span>increasing "
                       "productivity</span>. Avoiding repetition by using "
                       "templates is important because:"
                         "<ul>"
                           "<li>It saves the programmer time</li>"
                           "<li>Less code needs to be written, therefore "
                           "making it easier to understand when it is being "
                           "reviewed</li>"
                           "<li>Less risk of typos and therefore less chance "
                           "of buggy code</li>"
                         "</ul>"
                     "</p>")]
           ]

stages = [
         Stage(1, "Stage 1: Webpages, Documents, and Structure", "/stage-1-notes/", stage_1_lessons, stage_1_concepts),
         Stage(2, "Stage 2: Telling Computers What To Do", "/stage-2-notes/", stage_2_lessons, stage_2_concepts),
         Stage(3, "Stage 3: The Power of Abstraction", "/stage-3-notes/", stage_3_lessons, stage_3_concepts),
         Stage(4, "Stage 4: The Full Stack", "/stage-4-notes/", stage_4_lessons, stage_4_concepts),
         Stage(5, "Stage 5: The Power of APIs (Elective)", "/stage-5-notes/", stage_5_lessons, stage_5_concepts)
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
        """Creates a Jinja template and stores it in 't'."""
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    """Displays the home page using a get request."""
    def get(self):
        self.render("main_page.html", stages=stages)

class StageFourNotes(Handler):
    """Displays the Stage 4 notes page using a get request."""
    def get(self):
        comments_name = DEFAULT_COMMENTS

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
        current_url = self.request.url

        self.render("comments.html", stages = stages, error=error,
                    user_name=user_name, user_url=user_url,
                    user_url_linktext=user_url_linktext, comments=comments,
                    user=user, current_url=current_url)


    """Posts a comment on the notes page using a post request."""
    def post(self):
        comments_name = DEFAULT_COMMENTS
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

        # Get the path of the current notes page
        current_path = self.request.path

        if not comment.content:
            # Redirect to the comments section of the current notes page with
            # the error query parameter
            error = "&error=error"
            self.redirect(current_path + "?"+ comments_name + error + "#comment-section")
        else:
            # Write to the Google Database
            comment.put()
            # Redirect to the comments section after posting a comment
            self.redirect("?" + comments_name + "#comment-section")


app = webapp2.WSGIApplication([("/*", MainPage),
                               #("/stage-1-notes", StageOneNotes),
                               #("/stage-2-notes", StageTwoNotes),
                               #("/stage-3-notes", StageThreeNotes),
                               ("/stage-4-notes/", StageFourNotes)],
                               #("/stage-5-notes", StageFiveNotes),
                               #("/post-comment", PostComment)],
                              debug=True)
