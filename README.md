![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Project Name

![Am I Responsive Image]()

Github link to the project [Github link](https://github.com/your-username/your-project-repo)

Live Link to the project website [Live link](https://your-live-link.com)

## CONTENTS

- [Project Name](#project-name)
  - [CONTENTS](#contents)
  - [User Experience (UX)](#user-experience-ux)
    - [Key Information for the site](#key-information-for-the-site)
    - [Business Model](#business-model) 
    - [User Stories](#user-stories)
      - [Client Goals](#client-goals)
      - [First Time Visitor Goals](#first-time-visior-goals)
      - [Returning and Frequent Visitor Goals](#returning-and-frequent-visitor-goals)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [Future Implementations](#future-implementations)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks](#frameworks)
    - [Libraries \& Programs Used](#libraries--programs-used)
    - [Accessibility](#accessibility)
  - [Deployment \& Local Development](#deployment--local-development)
    - [Deployment](#deployment)
      - [**Create the Live Database**](#create-the-live-database)
      - [**Heroku app setup**](#heroku-app-setup)
      - [**Preparation for deployment in Codeanywhere**](#preparation-for-deployment-in-codeanywhere)
    - [Local Development](#local-development)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
  - [Testing](#testing)
    - [Full Testing](#full-testing)
    - [W3C Validator](#w3c-validator)
    - [Solved Bugs](#solved-bugs)
    - [Known Bugs](#known-bugs)
    - [Lighthouse](#lighthouse)
      - [Index Page](#index-page)
      - [My Bookings](#my-bookings)
      - [New Bookings](#new-bookings)
      - [Edit Bookings](#edit-bookings)
      - [Booking Success](#booking-success)
  - [Credits](#credits)
    - [Code Used](#code-used)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

- [Add your project description here]

### Key Information for the site

- [Add your key information here]

### Business Model

- [Add your key information here]

### User Stories

![User Stories](media/images/README/userstories.png)

The user stories are split into User and Admin.

[Add your user and admin stories here]

#### Client Goals

- [Add your client goals here]

#### First Time Visitor Goals

- [Add your first-time visitor goals here]

#### Returning and Frequent Visitor Goals

- [Add your returning and frequent visitor goals here]

## Design

### Colour Scheme

![Color Palette](media/images/README/Coolors.png)

- [Add your color scheme information here]

### Typography

- [Add your typography information here]

### Imagery

- [Add your imagery information here]

### Wireframes

- [Add your wireframes information here]

## Features

[Describe your features here]

### Future Implementations

- [Add your future implementations here]

## Technologies Used

### Languages Used

HTML, CSS, Javascript, Python and Django

### Frameworks

Django - A high-level Python web framework that encourages rapid development and clean, pragmatic design.

Google sheets and Google Docs - To draw up user stories and writing up content for html pages.

Codeanywhere - For version control

Github - To save and store the files for the website

Bootstrap - The framework for the website.

Google Dev Tools - To troubleshoot and test features, solve issues with responsiveness and styling.

[Add the frameworks you used here]

### Libraries & Programs Used

Font Awesome - For the icongraphy on the website.

Django Allauth

Stripe 

Cloudinary

Django Star Ratings - but didn't use on project in the end. 

Pillow

Django-countries

gunicorn

dj_database_url

psycopg2

Pip - for install python packages

### Accessibility

- I have been mindful during the coding to ensure that the website is as accessible and user friendly as possible. I have achieved this by:
- Using semantic HTML.
- Using descriptive alt attributes on images on the site.
- Ensuring that there is a sufficient colour contrast throughout the site.
- Ensuring menus are accessible by marking the current page as active for screen readers.

## Deployment & Local Development

### Deployment

The project is deployed using Heroku. To deploy the project:

#### **Create the Live Database**

We have been using the sqlite3 database in development, however this is only available for use in development so we will need to create a new external database which can be accessed by Heroku.

1. Go to the [ElephantSQL](https://www.elephantsql.com/) dashboard and click the create new instance button on the top right.
2. Name the plan (your project name is a good choice), select tiny turtle plan (this is the free plan) and choose the region that is closest to you then click the review button.
3. Check the details are all correct and then click create instance in the bottom right.
4. Go to the dashboard and select the database just created.
5. Copy the URL (you can click the clipboard icon to copy)

#### **Heroku app setup**

1. From the [Heroku dashboard](https://dashboard.heroku.com/), click the new button in the top right corner and select create new app.
2. Give your app a name (this must be unique), select the region that is closest to you and then click the create app button bottom left.
3. Open the settings tab and create a new config var of `DATABASE_URL` and paste the database URL you copied from elephantSQL into the value (the value should not have quotation marks around it).

#### **Preparation for deployment in Codeanywhere**

1. Install dj_database_url and psycopg2 (they are both needed for connecting to the external database you've just set up):

```bash
pip3 install dj_database_url==0.5.0 psycopg2
```

2. Update your requirements.txt file with the packages just installed:

```bash
pip3 freeze > requirements.txt
```

3. In settings.py underneath import os, add `import dj_database_url`

4. Find the section for DATABASES and comment out the code. Add the following code below the commented out database block, and use the URL copied from elephantSQL for the value:

(NOTE! don't delete the original section, as this is a temporary step whilst we connect the external database. Make sure you don't push this value to GitHub - this value should not be saved to GitHub, it will be added to the Heroku config vars in a later step, this is temporary to allow us to migrate our models to the external database)

```python
DATABASES = {
'default': dj_database_url.parse('paste-elephantsql-db-url-here')
}
```

5. In the terminal, run the show migrations command to confirm connection to the external database:

```bash
python3 manage.py runserver
```

6. If you have connected the database correctly you will see a list of migrations that are unchecked. You can now run migrations to migrate the models to the new database:

```bash
python3 manage.py migrate
```

7. Create a superuser for the new database. Input a username, email and password when directed.

```bash
python3 manage.py createsuperuser
```

8. You should now be able to go to the browser tab on the left of the page in elephantsql, click the table queries button and see the user you've just created by selecting the auth_user table.
9. We can now add an if/else statement for the databases in settings.py, so we use the development database while in development (the code we commented out) - and the external database on the live site (note the change where the db URL was is now a variable we will use in Heroku):

```python
if 'DATABASE_URL' in os.environ:
DATABASES = {
'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
else:
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
}
}
```

10. Install gunicorn which will act as our webserver and freeze this to the requirements.txt file:

```bash
pip3 install gunicorn
pip3 freeze > requirements.txt
```

11. Create a `Procfile` in the root directory. This tells Heroku to create a web dyno which runs gunicorn and serves our django app. Add the following to the file (making sure not to leave any blank lines underneath):

```Procfile
web: gunicorn seaside_sewing.wsgi:application
```

12. Log into the Heroku CLI in the terminal and then run the following command to disable collectstatic. This command tells Heroku not to collect static files when we deploy:

```bash
heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name-here
```

13. We will also need to add the Heroku app and localhost (which will allow GitPod to still work) to ALLOWED_HOSTS = [] in settings.py:

```python
ALLOWED_HOSTS = ['{heroku deployed site URL here}', 'localhost' ]
```

14. Save, add, commit and push the changes to GitHub. You can then also initialize the Heroku git remote in the terminal and push to Heroku with:

```bash
heroku git:remote -a {app name here}
git push heroku main
```

15. You should now be able to see the deployed site (without any static files as we haven't set these up yet).

16. To enable automatic deploys on Heroku, go to the deploy tab and click the connect to GitHub button in the deployment method section. Search for the projects repository and then click connect. Click enable automatic deploys at the bottom of the page.

Heroku was used to deploy the live website. The instruction to achieve this are below:

1. Log in to Heroku.
2. Find the app from this project and open - highlands
3. Click on deploy.
4. Find 'App connected to Github' and link to Github account.
5. Search for repository and link - RichBurman/highlands_project5
6. Find Manual Deploy and click Deploy Branch.
7. Click on Open App at the top right of the screen to view the live site.

#### **Create the Live Database**

[Add your live database creation steps here]

#### **Heroku app setup**

[Add your Heroku app setup steps here]

#### **Preparation for deployment in Codeanywhere**

[Add your Codeanywhere deployment preparation here]

### Local Development

#### How to Fork

[Add your forking steps here]

#### How to Clone

[Add your cloning steps here]

## Testing

[Add your testing information here]

### Full Testing

[Add your full testing information here]

### W3C Validator

[Add your W3C Validator results here]

### Solved Bugs

[Add your solved bugs information here]

### Known Bugs

[Add your known bugs information here]

### Lighthouse

[Add your Lighthouse testing results here]

## Credits

### Code Used

[Add the code you used here]

### Content

[Add your content information here]

### Media

- [Add your media information here]

### Acknowledgments

- [Add your acknowledgments here]