### END TO END ML PROJECT FINAL

Step1:
step2: Train test and pipeline building

```
step3: Testing and Debugging:
I use Flask(web app/framework) to run a local server(same as local mine comp) for testing and debugging my model prediction. This allows me to verify functionality before global deployment. Key testing types include:
1. Functional Testing: Ensures the application behaves as expected when interacting with the web interface.
2. Environment Testing: Confirms the app runs correctly in the specified Python environment with all dependencies.
3. Code Debugging: Helps identify and fix bugs using Flask's debug mode for clear error messages.
Integration Testing: Verifies that all components work together seamlessly.
This local testing phase is crucial for refining the application before deployment.

```
About Flask:
1. Flask application can be considered an API(it processes requests (from the HTML forms) and provides responses (e.g., predictions) , if it is designed to process requests and return results, even if it primarily interacts through HTML pages.

2. Flask is a web framework for Python that allows you to build web applications. When you run a Flask application, it starts a local server on your laptop (typically at http://127.0.0.1:5000). This local server enables you to develop and test your web app in a controlled environment before deploying it to a global server or the internet.

3. 

```
How Flask works:
1. Create App.py: Start by defining an app.py file where you initiate the creating flask aobject as app with app = Flask(__name__). The entry point is defined with if __name__ == "__main__": app.run(), which launches the Flask server to listen for incoming requests. Conditional Check:
The entry point is typically defined using the conditional statement if __name__ == "__main__":. This checks whether the script is being executed directly (rather than being imported as a module in another script).
2. Running the Application:
Inside this conditional block, you call app.run(), which starts the Flask development server. This command makes your application listen for incoming requests on the specified host and port (default is 127.0.0.1:5000).

```
Process and set up:
1. Create app.py where flask server is directly started to recieve requests.

2. Inside app.py, first create flask object and define entry point to check if the script running directly from the same place.

3. I created 2 files : index.html(welcome page), home.html(user can add data) under Template folder.

4. Route Purpose: 
When we define a route like /predict in app.py, it serves as a specific endpoint for application. Here’s how it works in a simplified way:

1. Local Server: When you run your Flask app, it starts a local server on your computer. The server listens for incoming requests at a specific URL (e.g., http://127.0.0.1:5000).

2. Handling Requests: When a client (like a web app or a user’s browser) sends a request to this URL:

3. GET Request: If the request is for the home page (using /), Flask responds by displaying the HTML page defined in index.html. This is handled by the GET method.
4. POST Request: If the request is to /predictor some action , this route is activated when the user submits a form. For that, here we use htmlpage as home.html, which is made for user to enter data and also action is also defined under html page as post, which on submisiion triggers the post def in app.py.

5. Data Submission:
The HTML form collects input data from the user (e.g., features for a machine learning model) and is set to send this data using a POST request to /predict.
In app.py, there are two functions (or handlers) defined for this route:
a. GET Function: This function displays the HTML form so the user can enter their data.
b. POST Function: After the user fills out the form and submits it, this function processes the input data and uses the model to make a prediction.

```

```
Work Flow:
Step 1: User accesses http://127.0.0.1:5000/, and the GET request triggers the function that renders index.html.
Step 2: User fills in the form on index.html and submits it.
Step 3: This triggers a POST request to /predict, where the data is processed, and a prediction is made using the model.

```

```
Step5:

"Deployment of app on AWS beanstalk:"
```


```
AWS Beanstalk:
AWS Elastic Beanstalk(instance) is a fully managed service that simplifies the deployment and scaling of web applications. It is actually an server of some instance like linux machine where you can deploy web here. It supports multiple programming languages and platforms, allowing developers to focus on writing code without worrying about the underlying infrastructure. With features like automatic scaling, load balancing, and integrated monitoring, Elastic Beanstalk ensures high availability and performance. Customization options, such as the use of .ebextensions, enable you to tailor the environment to your application's specific needs, making it an ideal choice for rapid deployment.
```

```
Settings Before deploying from m local env(set as venv python = 3.8):

```
Requirements for deploymnet in AWS Beanstalk:

1. .ebextensions : Under this, create python.config which contains WSGI path to tell how to use now app.py ie not to run locally here but run on beanstalk globally.

2. Instead of using app.py for flask server and routing defination, rename as application.py 

3. create flask obj as application only. application = Flask(__name__)
4. Remove debug = true if given inside while running flask as app.run(host)
5. Add to git 


```
```

1. .ebextensions: The .ebextensions directory in your AWS Elastic Beanstalk project allows to customize the deployment environment to closely match my local development environment. This ensures that my application runs smoothly in production without conflicts.

2. .ebextensions Helps Align Environments.

3. It ensures consistency and reduces deployment issues by:----
a. Custom Configuration: Define environment settings specific to your application.
b. Dependency Installation: Specify additional packages to be installed during deployment.
c. Environment Variables: Set environment variables needed for your application securely.
d. Command Execution: Run commands for setup tasks like database migrations.
e. Resource Management: Create or modify AWS resources as needed

4. Role of .ebextensions and WSGI Configuration
In my project, the .ebextensions directory contains configuration files that not only set the environment but also specify how my app.py should run once deployed on Elastic Beanstalk.

Environment Configuration: Within these files, I can define environment variables, software requirements, and any other settings needed for my application to function correctly in the cloud environment.

WSGI Configuration: By specifying the wsgi_path in the configuration, I indicate to Elastic Beanstalk where to find the WSGI application callable (e.g., app:app): code under python.config: option_settings:
  aws:elasticbeanstalk:application:environment:
  WSGI_PATH: application:application  # This points to your WSGI callable, where fisrt application name is applictaion.py instead of app.py created and then add all contents od app.y to application.py as its requiremnet here. Second one application is obj u created as application = Flask(__name__)

This tells Beanstalk to use the Flask application defined in app.py to handle incoming requests.
Instead of calling app.run() locally, this configuration directs Elastic Beanstalk to manage the server, allowing the application to run in a global, scalable environment.
Summary
Thus, using .ebextensions, I not only set the necessary environment for my application but also ensure that it runs correctly on Elastic Beanstalk, enabling global access rather than being limited to local execution.


```

```
"Transition from Local to Global Hosting""
1. Initially, my Flask application was running on a local server using app.run(), which allowed me to test and debug the application on my laptop. This local setup was limited to my machine, meaning only I could access it through a specific URL (e.g., http://127.0.0.1:5000).

2. Now, with the deployment to Elastic Beanstalk, the transition to a global server environment has been established. Here’s how it works:

3. Environment Configuration: By using .ebextensions, I set up the necessary environment variables and configurations for my application in the cloud.

4. WSGI Configuration: The wsgi_path setting specifies the location of my WSGI application callable (e.g., app:app). This tells Elastic Beanstalk how to run my Flask application.

5. Global Accessibility: Rather than running app.run() locally, Elastic Beanstalk manages the server infrastructure, making my application globally accessible via a public URL. This allows users from anywhere to interact with the application, vastly expanding its reach and usability.
```

```
"Process of deployment from git hub to Elastic Beanstalk using CODE PIPELINE."
step 1: aws beanstalk instance ie in linux
step2: then create env
step 3: create code pipeline and integrate with our code repository
step4: then deploy on Beanstaak
step5: create aws and got beanstalk. and create application.

Any change in code, it wil ask for deploying  on beanstalk. This pipeline is continous delivery pipeline.
```