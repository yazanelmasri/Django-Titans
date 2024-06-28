
# Django Titans

This is a full-stack framework project built using Django, Python, HTML and CSS. Welcome to our Car Service Booking Site! 

## About

This platform is designed to provide a seamless and efficient way for users to book various car services. Whether you need routine maintenance, emergency repairs, or specialised services, our site connects you with trusted service providers in your area. Our goal is to create a functioning and responsive website, that allows users to post, comment and like or unlike recipes. This project has been built for educational purposes.

## Table of Contents
- UX
    1. User Stories
- Scope 
    1. Features
- Structure
- Wireframes
- Database schema
- Surface
- Technologies Used
- Testing
- Deployment
- Credits

UX
*

## User Stories

- Given I am a new user, I should be able to create an account with my email and password.
- Given I am a returning user, I should be able to log in with my email and password.
- Given I am logged in, I should be able to search for specific car services (e.g., oil change, brake repair).
- I should be able to filter service providers based on location, ratings, and availability.
- Given I have searched for a service, I should see a list of available service providers.
*- I should be able to view detailed information about each provider, including ratings, reviews, and available time slots.
- Given I have selected a service provider, I should be able to choose a convenient date and time for the service.
- I should be able to provide any necessary details about my car and the service required.
- I should be able to view and manage my upcoming appointments through my account dashboard.
- As a user, I want to navigate the website easily so that I can find the information I need without difficulty.
- As a service provider, I want to update the status of a service (e.g., in progress, completed) so that customers are informed about the progress.
- As a service provider, I want to view upcoming service appointments so that I can plan my schedule.


## Scope
### Features
#### Home page
![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/3f8e7745-3f33-48fb-80a4-de37f762c6bb)

#### Login
![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/d775d12f-d3ea-4a45-8976-b4b171502619)

#### Sign-Up
![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/3b0a9a4a-b885-498c-ac62-ab5653c27454)





## Structure
*

## Wireframes
All wireframes were created used Balsamiq

Wireframes for each device are linked here:

- Desktop

![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/bbee04fe-4e7d-4a4b-8347-eb1c39aed2f9)


- Tablet

![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/85d9fac5-dde8-4fa7-b10d-444c5ac53b0d)


- Mobile

![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/84cfb05a-9590-4cb6-88bd-abf947d437f1)


#### Database schema
![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/05ea3b75-bf86-4ae3-9582-0bb055b4a08e)



#### Models
![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/e9a7a5d8-427c-4638-b2cb-3d59da32ad2e)
![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/67353026-93cc-4e7e-823d-5dba4c4f9ea5)
![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/e46480d6-ffaf-422d-9b22-90c8392c5ba0)









## Surface
### Design
### Chosen colours
![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/7c4c66e8-b637-4298-bd25-707bb2b50495)



## Technologies Used
Languages
- HTML5
- CSS3
- Python

## Frameworks, Libraries & Programs Used
GitHub - Holds the repository of my project, GitHub connects to GitPod and Heroku.

GitPod – Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository.

Heroku - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilised/tested.

Django - This framework was used to build the foundations of this project

Gunicorn - Gunicorn is a pure-Python HTTP server for WSGI applications.

*Dj Database URL - This allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

Bootstrap - Used to quickly add design to my website, Bootstrap focuses on mobile first design meaning this website is responsive across multiple devices ans screen sizes.

Cloudinary - Used to store images online for the recipe posts.

Summernote Used to add a text area field to the admin setup to enable a list of ingredients and method steps.

Balsamiq - was used to create site wireframes.

W3C Markup Validator - was used to validate HTML

W3C CSS Validator - was used to validate CSS

Coolors - to make color palette

## Testing
User Story Testing
Testing Users Stories form (UX) Section


## Bugs and Issues
- Procfile error introduced a conflict preventing us from merging.
  
![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/efafe4c7-d99b-4edb-8b05-db686564495b)

- Issue with deploymet on Heroku
  
![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/e521d787-600d-441f-9042-7448255eaa22)

- we forgot to add some packages to the requirements.txt file

  ![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/5965869d-05c4-4f1a-9e33-17eb72b76dde)

- when opening a new workspace we forgot to install the requirements.txt file

![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/fea0730f-ba09-4cc0-9cf7-7db056a1a72d)

- we forgot to add each of our gitpod urls to allowed hosts

![image](https://github.com/yazanelmasri/Django-Titans/assets/165275718/47ee1393-ca6b-41f0-8e49-418f7e301770)






## Deployment
This project was deployed using Github and Heroku.

Github
Here are the steps I took to create a new repository and set up Django with Heroku:

- Logged into GitHub.
- Navigated to the ‘repositories’ section.
- Clicked the green ‘new’ button to create a new repository.
- On the create new repository page, selected the Code Institute template from the ‘repository template’ dropdown menu.
- Entered a repository name and clicked the green ‘create repository’ button at the bottom of the page.
- After creating the repository, opened it and clicked the green ‘Gitpod’ button to create a workspace in Gitpod for editing.

#### Django and Heroku Setup
- To install and set up the Django framework, I followed the steps outlined in the Code Institute Django Blog cheatsheet.

## Credits
- Django blog resources from Code Institute LMS.
- Additional clarification from Django projects on YouTube.
- Bug solutions from Stack Overflow.
- User persona and user stories generated using founderpal.ai.
- Support from the cohort.
- Book cover details from Waterstones Website.
- Icons from Font Awesome.
- Fonts from Google Fonts.

## Media
*

## Acknowledgements
*
