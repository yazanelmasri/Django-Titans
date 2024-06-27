
#Django Titans

This is a full-stack framework project built using Django, Python, HTML and CSS. Welcome to our Car Service Booking Site! 

##About

This platform is designed to provide a seamless and efficient way for users to book various car services. Whether you need routine maintenance, emergency repairs, or specialised services, our site connects you with trusted service providers in your area. Our goal is to create a functioning and responsive website, that allows users to post, comment and like or unlike recipes. This project has been built for educational purposes.

##Table of Contents
UX
-User Stories
Scope 
-Features
Structure
Wireframes
Database schema
Surface
Technologies Used
Testing
Deployment
Credits

UX
*

##User Stories
Epic: Registration/Login
Given I am a new user, I should be able to create an account with my email and password.
Given I am a returning user, I should be able to log in with my email and password.

Epic: Search for Services
Given I am logged in, I should be able to search for specific car services (e.g., oil change, brake repair).
I should be able to filter service providers based on location, ratings, and availability.

Epic: Select a Service Provider
Given I have searched for a service, I should see a list of available service providers.
I should be able to view detailed information about each provider, including ratings, reviews, and available time slots.

Epic: Book a Service
Given I have selected a service provider, I should be able to choose a convenient date and time for the service.
I should be able to provide any necessary details about my car and the service required.

Epic: Payment
Given I have selected a service and a time slot, I should be able to proceed to payment.
I should be able to choose from multiple secure payment options (e.g., credit card, PayPal).

Epic:Confirmation
Given I have completed the payment, I should receive a confirmation email with all the booking details.
I should be able to view and manage my upcoming appointments through my account dashboard.


##Scope
Features
*

##Structure
*

##Wireframes
All wireframes were created used Balsamiq

Wireframes for each device are linked here:

Desktop
(image)

Tablet
(image)

Mobile
(image)

Database schema
![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/05ea3b75-bf86-4ae3-9582-0bb055b4a08e)



Models
Post Model


Comment Model


Surface

Design


##Technologies Used
Languages
HTML5
CSS3
Python

##Frameworks, Libraries & Programs Used
GitHub - Holds the repository of my project, GitHub connects to GitPod and Heroku.

GitPod – Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository.

Heroku - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilised/tested.

Django - This framework was used to build the foundations of this project

Gunicorn - Gunicorn is a pure-Python HTTP server for WSGI applications.

*Dj Database URL - This allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

*Bootstrap - Used to quickly add design to my website, Bootstrap focuses on mobile first design meaning this website is responsive across multiple devices ans screen sizes.

Cloudinary - Used to store images online for the recipe posts.

Summernote Used to add a text area field to the admin setup to enable a list of ingredients and method steps.

*Google Fonts - provide fonts for the website.

*Font Awesome -was used for icons.

Balsamiq - was used to create site wireframes.

*Am I Responsive - to check if the site is responsive on different screen sizes.

*Pixabay and Unsplash - were used for all the images

W3C Markup Validator - was used to validate HTML

W3C CSS Validator - was used to validate CSS

*Coolors - to make color palette

##Testing
User Story Testing
Testing Users Stories form (UX) Section
EPIC: Superuser / Admin

As a site Admin I can create, edit and delete recipes and comments so that I can manage the site content
As a site Admin I can access the admin panel so that I can manage recipes and comments
As a site Admin I can log out of the admin panel so that I can disconnect from the website
This was tested by accessing the Django Admin Panel. By creating a Superuser we can access the Django Admin Panel where the administrator can perform all the CRUD functionalitis

EPIC: User Interaction

As a logged-in User I can write comments on recipes so that I can leave my feedback


As a logged-in User I can like and unlike recipes so that I can mark which recipes I like


As a User I can view the number of likes on recipes so that I can see which recipes are the most popular


As a User I can view comments on recipes so that I can read other users opinions


EPIC: User Recipes

As a logged-in User I can post a recipes so that other users can see them


2. As a User I can delete my recipes so that I can remove any unwanted recipes that I have made


3. As a User I can edit recipes so that I can update any changes or mistakes to my recipes


4. As a logged-in User I can upload an image along with my recipe so that other users can see what the dish looks like


EPIC: Login/Register

As a User I can register for an account so that I can interact with the site content


As a User I can log in/out off my account if I wish so that I can connect or disconnect from the website


3. As a User I can easily see if I'm logged-in or logged-out so that I can be sure what my status is




EPIC: Navigation

As a User I can easily navigate through the site so that I can view desired content


As a User I can search the desirable recipe by keyword so that I can find the recipe I want faster


3. As a User I can see the most loved recipes so that I can quickly find inspiration and see which recipes are most famous


As a User I can see the most recent recipes so that I can keep up to date with the latest recipes


Bugs and Issues
*

Deployment
This project was deployed using Github and Heroku.

Github
To create a new repository I took the following steps:

Logged into Github.
Clicked over to the ‘repositories’ section.
Clicked the green ‘new’ button. This takes you to the create new repository page.
Once there under ‘repository template’ I chose the code institute template from the dropdown menu.
I input a repository name then clicked the green ‘create repository button’ at the bottom of the page.
Once created I opened the new repository and clicked the green ‘Gitpod’ button to create a workspace in Gitpod for editing.
Django and Heroku
To get the Django framework installed and set up I followed the Code institutes Django Blog cheatsheet

Credits
*

Media
*

Acknowledgements
*
