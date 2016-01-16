# This file contains a mixtures of lists and namedtuples that allows us to
# keep all of our html content in one place. We then import this content into
# the main.py file for use there, where it is injected into Jinja2 templates.

from collections import namedtuple

Stage = namedtuple("Stage", ["stage_number", "stage_title", "stage_url",
                             "lessons", "concepts"])
Lesson = namedtuple("Lesson", ["lesson_number", "lesson_id", "lesson_title"])
Concept = namedtuple("Concept", ["concept_id", "concept_title",
                                 "concept_description"])

stage_1_lessons = [
                   Lesson(1, "lesson-1", "The Basics of the Web and HTML"),
                   Lesson(2, "lesson-2", "Creating a Structured Document"),
                   Lesson(3, "lesson-3", "Adding CSS Style and HTML Structure")
                  ]

stage_1_concepts = [
                    [
                     Concept("lesson-1-1", "How the Web Works",
                             "<p>"
                               "The main agents in the process of using the web are:"
                             "</p>"
                             "<ol>"
                               "<li><span>The user</span></li>"
                               "<li><span>The web browser</span></li>"
                               "<li><span>The internet</span></li>"
                               "<li><span>HTTP</span></li>"
                               "<li><span>Servers</span></li>"
                             "</ol>"
                             "<p>"
                               "The <span>user</span> opens a <span>web browser</span>"
                               ". The user commands the browser to do something and "
                               "the browser sends a signal over the <span>internet"
                               "</span> ('the world's largest computer network'). "
                               "<span>HTTP</span>, an applications protocol, takes the"
                               " signals and sends them to <span>servers</span> that "
                               "host the content. The servers then send information "
                               "back along the chain of command (through HTTP through "
                               "the internet through my browser) back to me, the user."
                             "</p>"),

                     Concept("lesson-1-2", "What is HTML?",
                             "<p>"
                               "<span>HTML</span> is the main type of document on the "
                               "web that glues the internet together. This type of "
                               "document contains:"
                             "</p>"
                             "<ul>"
                               "<li>Text content (what you see)</li>"
                               "<li>Markup (what it looks like)</li>"
                               "<li>References to other documents (e.g. images and "
                               "videos)</li>"
                               "<li>Links to other pages</li>"
                             "</ul>"),

                     Concept("lesson-1-3", "Tags vs. Elements vs. Attributes",
                             "<p>"
                               "The distinction between HTML tags, elements, and "
                               "attributes was murky for me at first. Luckily, this "
                               "resource from <a href='http://www.456bereastreet.com/a"
                               "rchive/200508/html_tags_vs_elements_vs_attributes/'"
                               "target='_blank'> 456 Berea Street</a> provided some"
                               " clarity. In summary:"
                             "</p>"
                             "<ul>"
                               "<li>An <span>element</span> in HTML represents some "
                               "kind of structure or semantics and generally consists "
                               "of a start tag, content, and an end tag. The following"
                               " is a paragraph element:<em><br>&nbsp;&nbsp;&nbsp;"
                               "&nbsp;&nbsp;&nbsp; &lt;p&gt;<br>&nbsp;&nbsp;&nbsp;"
                               "&nbsp;&nbsp;&nbsp;This is the content of the paragraph"
                               " element.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;/"
                               "p&gt;</em></li>"
                               "<li>A <span>tag</span> is used to mark up the start "
                               "and end of an HTML element. A start tag consists of an"
                               " opening angle bracket followed by the element name, "
                               "zero or more space separated attribute/value pairs, "
                               "and a closing angle bracket. There are also some "
                               "elements that are empty (e.g. the &lt;br&gt; element, "
                               "which is essentially just an opening tag), meaning "
                               "that they only consist of a single tag and do not have"
                               "any content.</li>"
                               "<li>An <span>attribute</span> defines a property for "
                               "an element, consists of an attribute/value pair, and "
                               "appears within the element's start tag. An element's "
                               "start tag may contain any number of space separated "
                               "attribute/value pairs. The most popular misuse of the "
                               "term 'tag' is referring to alt attributes as 'alt "
                               "tags'. There is no such thing in HTML. Alt is an "
                               "attribute, not a tag.</li>"
                             "</ul>"),

                     Concept("lesson-1-4", "Inline vs. Block Elements",
                             "<p>"
                               "There are two varieties of elements: <span>inline</span>"
                               " and <span>block</span>. This is an elementary "
                               "description, but inline elements flow along with text "
                               "content while block elements form an invisible paragraph"
                               " box for its content. <a href='http://www.impressivewebs"
                               ".com/difference-block-inline-css/' target='_blank'>"
                               "Impressive Webs</a> has a thorough description of the "
                               "many characteristics that differentiate inline and block"
                               " elements."
                             "</p>")
                    ],

                    [
                     Concept("lesson-2-1", "HTML's Tree-like Structure",
                             "<p>"
                               "HTML can be viewed as a series of nested elements. "
                               "These nested elements form a <span>tree-like structure"
                               "</span>. This visual representation is called the "
                               "document object model, or <span>DOM</span> (see <a "
                               "href='https://css-tricks.com/dom/' target='_blank'>"
                               "What is the DOM?</a> and the image below for details)"
                               ":<br><img src='http://www.webstepbook.com/supplements/"
                               "slides/images/dom_tree.gif' alt='DOM Tree visualization'"
                               " style='padding-top:12px; padding-bottom: 0px;'>"
                             "</p>"),

                     Concept("lesson-2-2", "How Web Browsers Interpret HTML",
                             "<p>"
                               "This <a href='https://www.addedbytes.com/articles/for-beg"
                               "inners/the-box-model-for-beginners/' target='_blank'>Added"
                               " Bytes page</a> is what Buzz is referring to below with "
                               "regards to how web browsers interpret HTML:"
                             "</p>"
                             "<img src='http://blog.personalministorage.com/wp-content/up"
                             "loads/2014/07/boxes-everywhere.jpg' alt='Buzz Lightyear: "
                             "Boxes, boxes everywhere'>"),

                     Concept("lesson-2-3", "Key Tools",
                             "<p>"
                               "The two key tools we learned to use in this lesson to "
                               "create/review structured documents were:"
                             "</p>"
                             "<ol>"
                               "<li><span>Chrome DevTools</span>: we used this to view "
                               "the HTML and CSS code for live webpages</li>"
                               "<li><span>Sublime Text</span>: we used this specialized "
                               "text editor to easily write code and save it on our "
                               "computer</li>"
                             "</ol>")
                    ],

                    [
                     Concept("lesson-3-1", "What is CSS?",
                             "<p>"
                               "CSS stands for <span>Cascading Style Sheets</span>. CSS "
                               "controls the style of the webpage. The 'cascading' part "
                               "means that CSS rules are applied not only to the "
                               "elements they directly match (via <span>classes</span>),"
                               " but also to all of those elements' child elements (i.e."
                               " <span>inheritance</span>). However, if a child element "
                               "has multiple overlapping rules defined for it, the more "
                               "specific rule takes effect."
                             "</p>"
                             "<p>"
                               "Inheritance prevents certain properties from being "
                               "declared over and over again in a style sheet. It is a "
                               "fundamental building block for the <span>abstract "
                               "thinking</span> portion of a programmer's thought "
                               "process."
                             "</p>"),

                     Concept("lesson-3-2", "Specificity",
                             "<p>"
                               "<span>Specificity</span> is the means by which a browser"
                               " decides which CSS property values are the most relevant"
                               " to an element and therefore will be applied (via <a "
                               "href='https://developer.mozilla.org/en-US/docs/Web/CSS/"
                               "Specificity' target='_blank'>Mozilla Developer Network</a>"
                               "). The hierarchy of specificity power can be found on this"
                               " <a href='http://www.smashingmagazine.com/2007/07/css-"
                               "specificity-things-you-should-know/#specificity-hierarchy'"
                               " target='_blank'>website</a>."
                             "</p>"),

                     Concept("lesson-3-3", "The Importance of Having Good Style and "
                             "Avoiding Repetition",
                             "<p>"
                               "The name of the game is <span>increasing productivity"
                               "</span>. Avoiding repetition by leveraging CSS is "
                               "important because:"
                             "</p>"
                             "<ol>"
                               "<li>It saves the programmer time</li>"
                               "<li>Less code needs to be written, therefore making it "
                               "easier to understand when it is being reviewed</li>"
                               "<li>Less risk of typos and therefore less chance of "
                               "buggy code</li>"
                             "</ol>")
                    ]
                   ]

stage_2_lessons = [
                   Lesson(1, "lesson-1", "Variables and Strings"),
                   Lesson(2, "lesson-2", "Input --> Function --> Output"),
                   Lesson(3, "lesson-3", "Decisions and Repetition (If and While)"),
                   Lesson(4, "lesson-4", "How to Solve Problems")
                  ]
stage_2_concepts = [
                    [
                     Concept("lesson-1-1", "Puppies",
                             "<p>"
                               "Neatly packaged notes content was not the deliverable for"
                               " this stage so please refer to <a href='http://learn-2-co"
                               "de.appspot.com/nanodegree_notes/course/2/#lesson-2' target"
                               "='_blank'>Andy's Notes</a> and enjoy this picture of two "
                               "puppies."
                             "</p>"
                             "<img src='http://www.hd-wallpapersdownload.com/upload/bulk"
                             "-upload/cute-dog-images-with-words-dowload.jpg' alt='Two "
                             "puppies'>")
                    ],

                    [
                     Concept("lesson-2-1", "Monkey",
                             "<p>"
                               "Neatly packaged notes content was not the deliverable for"
                               " this stage so please refer to <a href='http://learn-2-co"
                               "de.appspot.com/nanodegree_notes/course/2/#lesson-3' target"
                               "='_blank'>Andy's Notes</a> and enjoy this picture of a "
                               "monkey."
                             "</p>"
                             "<img src='https://shechive.files.wordpress.com/2011/01/cut"
                             "e-animals-4.jpg?quality=94&strip=info&w=920' alt='A monkey'>")
                    ],

                    [
                     Concept("lesson-3-1", "Kitten",
                             "<p>"
                               "Neatly packaged notes content was not the deliverable for"
                               " this stage so please refer to <a href='http://learn-2-co"
                               "de.appspot.com/nanodegree_notes/course/2/#lesson-4' target"
                               "='_blank'>Andy's Notes</a> and enjoy this picture of a "
                               "kitten."
                             "</p>"
                             "<img src='https://i.ytimg.com/vi/3dzUgmpXPX0/hqdefault.jpg"
                             "' alt='A kitten'>")
                    ],

                    [
                     Concept("lesson-4-1", "Bunny Rabbit",
                             "<p>"
                               "Neatly packaged notes content was not the deliverable for"
                               " this stage so please refer to <a href='http://learn-2-co"
                               "de.appspot.com/nanodegree_notes/course/2/#lesson-5' target"
                               "='_blank'>Andy's Notes</a> and enjoy this picture of a "
                               "bunny rabbit."
                             "</p>"
                             "<img src='http://7-themes.com/data_images/out/40/6907695-"
                             "cute-animals.jpg' alt='A bunny rabbit'>")
                    ]
                   ]

stage_3_lessons = [
                   Lesson(1, "lesson-1", "Use Functions"),
                   Lesson(2, "lesson-2", "Use Classes"),
                   Lesson(3, "lesson-3", "Make Classes")
                  ]

stage_3_concepts = [
                    [
                     Concept("lesson-1-1", "Harp Seal",
                             "<p>"
                               "Neatly packaged notes content was not the deliverable for"
                               " this stage so please refer to <a href='http://learn-2-co"
                               "de.appspot.com/nanodegree_notes/course/3/#lesson-1' target"
                               "='_blank'>Andy's Notes</a> and enjoy this picture of a "
                               "baby harp seal."
                             "</p>"
                             "<img src='http://hdwallnpics.com/wp-content/gallery/cute-"
                             "pictures-of-animals/animals_hdwallpaper_cute-animal_73158"
                             ".jpg' alt='A baby harp seal'>")
                    ],

                    [
                     Concept("lesson-2-1", "Frog",
                             "<p>"
                               "Neatly packaged notes content was not the deliverable for"
                               " this stage so please refer to <a href='http://learn-2-co"
                               "de.appspot.com/nanodegree_notes/course/3/#lesson-2' target"
                               "='_blank'>Andy's Notes</a> and enjoy this picture of a "
                               "frog."
                             "</p>"
                             "<img src='https://pixabay.com/static/uploads/photo/2015/09"
                             "/06/20/31/frog-927764_960_720.jpg' alt='A frog'>")
                    ],

                    [
                     Concept("lesson-3-1", "Deer",
                             "<p>"
                               "Neatly packaged notes content was not the deliverable for"
                               " this stage so please refer to <a href='http://learn-2-co"
                               "de.appspot.com/nanodegree_notes/course/3/#lesson-5' target"
                               "='_blank'>Andy's Notes</a> and enjoy this picture of a "
                               "deer."
                             "</p>"
                             "<img src='http://animals.ekstrax.com/wp-content/uploads/20"
                             "14/09/beautiful-and-cute-animals-wallpaper-23.jpg' alt='A "
                             "deer'>")
                    ]
                   ]

stage_4_lessons = [
                   Lesson(1, "lesson-1", "Understanding Servers"),
                   Lesson(2, "lesson-2", "The Importance of Validating Input"),
                   Lesson(3, "lesson-3", "HTML Templates and Abstraction")
                  ]

stage_4_concepts = [
                    [
                     Concept("lesson-1-1", "The Request",
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
                               "navigate-to-a-url/' target='_blank'>source</a>)."
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
                               "/rfc2616-sec6.html' target='_blank'>source</a>):"
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
                             "</p>")
                    ],

                    [
                     Concept("lesson-2-1", "Input Validation",
                             "<p>"
                               "Web applications are notorious for taking practically "
                               "any type of input, assuming that it's valid, and "
                               "processing it further. Not validating input is one of "
                               "the greatest mistakes that web application developers "
                               "can make (<a href='http://searchsoftwarequality.techta"
                               "rget.com/tip/The-importance-of-input-validation' "
                               "target='_blank'>source</a>)."
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
                               "tip/The-importance-of-input-validation' target='_blank'>"
                               "This page</a> has detailed information on several types "
                               "of input attacks and their consequences."
                             "</p>"),

                     Concept("lesson-2-3", "User Experience",
                             "<p>"
                               "Input validation is important for user experience "
                               "because it provides a medium for conversation with "
                               "users and guides them through the difficult times of "
                               "errors and uncertainty (<a href='http://designmodo.com"
                               "/ux-form-validation/' target='_blank'>source</a>)."
                             "</p>"
                             "<p>"
                               "<span>HTML escaping</span> is also important for user "
                               "experience to ensure that the visual structure of the "
                               "web page is maintained."
                             "</p>")
                    ],

                    [
                     Concept("lesson-3-1", "Why Programmers Use Templates",
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
                               "/why-and-how-adding-jinja-to-my-notes/42435/2' target="
                               "'_blank'>andrew_R</a> from the Udacity discussion forum"
                               " has a great anecdote for why templates are useful:"
                               "<img src='http://i.imgur.com/0BEf98w.png' style='"
                               "padding-top: 12px; padding-bottom: 0px;' alt='andrew_R"
                               " from the discussion forum discussing templates'"
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
                             "</p>")
                    ]
                   ]

stage_5_lessons = [
                   Lesson(1, "lesson-1", "Meet Javascript"),
                   Lesson(2, "lesson-2", "The Power of APIs"),
                   Lesson(3, "lesson-3", "Recursion and Parallel Computing"),
                   Lesson(4, "lesson-4", "Responsive Web Design"),
                   Lesson(5, "lesson-5", "Solving Big Problems")
                  ]
stage_5_concepts = [
                    [
                     Concept("lesson-1-1", "Llama",
                             "<p>"
                               "Stephen Chapman provides a great JavaScript overview on "
                               "<a href='http://javascript.about.com/od/reference/p/javas"
                               "cript.htm' target='_blank'>About.com</a>. Here is a quick "
                               "summary:"
                               "<ul>"
                                 "<li>JavaScript is a programming language that is used "
                                 "to make web pages interactive.</li>"
                                 "<li>It runs on your visitor's computer and doesn't require"
                                 " constant downloads from your website.</li>"
                                 "<li>JavaScript and Java are two completely different "
                                 "computer languages. Only their names are similar.</li>"
                                 "<li>JavaScript support is built right into all the major "
                                 "web browsers. Provided that the visitors to your site are"
                                 " using web browsers that support JavaScript (most do) and"
                                 " have JavaScript enabled (it is by default), then your "
                                 "JavaScript will run when they visit the page.</li>"
                                 "<li>JavaScript is an interpreted language, so no special "
                                 "program is required to create usable code.</li>"
                                 "<li>JavaScript can go in the same file as HTML, however "
                                 "your scripts will be more easily reused on multiple pages"
                                 " of your site if you place them in separate files (using "
                                 "a .js extension). You then just link the JavaScript to "
                                 "your HTML by inserting a &lt;script&gt; tag in the HTML "
                                 "file.</li>"
                               "</ul>"
                             "</p>"
                             "<p>"
                               "This <a href='http://www.w3schools.com/js/js_intro.asp' "
                               "target='_blank'>W3Schools page</a> lists some examples"
                               " of what JavaScript can do. Here is a quick summary:"
                               "<ul>"
                                 "<li>JavaScript can change HTML content.</li>"
                                 "<li>JavaScript can change HTML attributes.</li>"
                                 "<li>JavaScript can change HTML styles (CSS).</li>"
                                 "<li>JavaScript can validate data.</li>"
                               "</ul>"
                             "</p>"
                             "<p>"
                               "Click me to make me <span>DANCE!</span> Below is an example"
                               " of JavaScript modifying HTML content:"
                             "</p>"
                             "<img id='myImage' onclick='changeImage()' "
                             "src='http://i.imgur.com/BBLXmzG.jpg' alt='A llama'>"
                             "<script src='/scripts/llamaDance.js'></script>")
                    ],

                    [
                     Concept("lesson-2-1", "Fennec Fox",
                             "<p>"
                               "Neatly packaged notes content was not the deliverable for"
                               " this stage so please refer to these <a href='https://www"
                               ".quora.com/What-is-an-API' target='_blank'>Quora answers"
                               "</a> and enjoy this picture of a fennec fox."
                             "</p>"
                             "<img src='http://images6.alphacoders.com/426/426613.jpg' "
                             "alt='A fennec fox'>")
                    ],

                    [
                     Concept("lesson-3-1", "Bear Cubs",
                             "<p>"
                               "Neatly packaged notes content was not the deliverable for"
                               " this stage so please refer to this <a href='http://programm"
                               "ers.stackexchange.com/questions/25052/in-plain-english-what-"
                               "is-recursion' target='_blank'>StackExchange page</a> "
                               "and this <a href='https://en.wikipedia.org/wiki/Parallel_"
                               "computing' target='_blank'>Wikipedia article</a> and "
                               "enjoy this picture of two bear cubs."
                             "</p>"
                             "<img src='http://www.wildnatureimages.com/images%202/050612-1"
                             "00..jpg' alt='Two bear cubs'>")
                    ],

                    [
                     Concept("lesson-4-1", "Tea Cup Pig",
                             "<p>"
                               "Neatly packaged notes content was not the deliverable for"
                               " this stage so please refer to this <a href='https://deve"
                               "lopers.google.com/web/fundamentals/design-and-ui/responsi"
                               "ve/fundamentals/?hl=en' target='_blank'>Google Developers"
                               " page</a> and enjoy this picture of a baby tea cup pig."
                             "</p>"
                             "<img src='https://41.media.tumblr.com/tumblr_lx9jqwbrnR1ql7i"
                             "mwo1_1280.jpg' alt='A baby tea cup pig'>")
                    ],

                    [
                     Concept("lesson-4-1", "Wolf Cub",
                             "<p>"
                               "Neatly packaged notes content was not the deliverable for "
                               "this stage so please refer to this <a href='http://www.bbc"
                               ".co.uk/education/guides/zqqfyrd/revision' target='_blank'>"
                               "BBC page on decomposition</a>, which was a key concept in "
                               "Peter Norvig's <a href='https://www.udacity.com/courses/cs"
                               "212' target='_blank'>Design of Computer Programs</a> class"
                               ", and enjoy this picture of a howling arctic wolf cub."
                             "</p>"
                             "<img src='http://i.imgur.com/Aa7s8wZ.jpg' alt='A howling "
                             "arctic wolf cub'>")
                    ]
                   ]

stages = [
         Stage(1, "Stage 1: Webpages, Documents, and Structure",
               "/stage-1-notes/", stage_1_lessons, stage_1_concepts),
         Stage(2, "Stage 2: Telling Computers What To Do",
               "/stage-2-notes/", stage_2_lessons, stage_2_concepts),
         Stage(3, "Stage 3: The Power of Abstraction",
               "/stage-3-notes/", stage_3_lessons, stage_3_concepts),
         Stage(4, "Stage 4: The Full Stack",
               "/stage-4-notes/", stage_4_lessons, stage_4_concepts),
         Stage(5, "Stage 5: Explore!",
               "/stage-5-notes/", stage_5_lessons, stage_5_concepts)
         ]
