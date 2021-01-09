# CI-MilestoneProjectFour

[![Build Status](https://travis-ci.com/lewisclark4/CI-MilestoneProjectFour.svg?branch=master)](https://travis-ci.org/lewisclark4/CI-MilestoneProjectFour) ![Django](https://img.shields.io/badge/Django-3.1-pink) [Python](https://img.shields.io/badge/python-3.8-pink.svg) [Code style](https://img.shields.io/badge/code%20style-pep8-success)

## Table of Contents
1. [Overview](#overview)
2. [Live Site](#live-site)
3. [User Experience & Design](#ux)

    - [Wireframes](#Wireframes)
4. [Technologies and Tools](#technologies-and-tools)
5. [Features](#features)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)

## Overview

Hex Cosmetics is a fictitious new e-commerce site which is has a requirement to be user friendly store that is easy to navigate.

Hex Cosmetics provides a wide array of commonly used cosmetic products (mascara, foundation, lipstick etc.).

Hex Cosmetics also provides a range of different well known brands to enable site users to be confident in the quality of products that they are purchasing.

The site's home page easily allows a site user to select the specific type of make-up they are looking for, as well as being able to shop all products, or view the site's featured products or sale products.

_NOTE: This is my final project in relation to my studies with Code Institute. This project should display the knowledge I have gained throughout the course, for the programming languages HTML, CSS, JavaScript & Python, while utilsing some of their associated open source libraries and frameworks._

## Live site
My project is hosted on Heroku and can be found [here](https://hex-cosmetics.herokuapp.com/).


## UX

### High Level Design Decisions

Below are some of the high level decisions taken to fit with common convention across most ecommerce sites:

* The navigation bar has been fixed to ensure a user can quickly navigate around the site to view other products, a user profile, access the search tool, or easily navigate to the basket.

* The home page contains cards which a user can select to view particular types of product, or allows them to navigate to all products (the search bar is also always available in the Navigation bar).

* The Home page also displays a large image of the HEX Cosmetics Logo to help instil brand awareness.

* Products are displayed in a consistent card format, and users can select the products to drill down into a detailed view of the product.

* Users are able to easily sort product views (e.g. price low to high) to aid their search.

* Feedback is given to users on major action taken across the site in using Django messages.

* Integrated with google to enable expedited user registration.

* Use of 'slugs' do display readable URLs. This improves user experience, looks more professional & can also assist with SEO.

* The user's basket total is available in the navigation bar at all times to allow them to easily identify their current spend.

* Contact, About & FAQ URLs can be found in the footer (and therefore available across the whole site).

* Users have the ability to sign up to the Hex Cosmetics Newsletter via the footer (so this can be used for targeted advertisement etc.).

* Links to social media profiles can also be found in the footer in an attempt generate further online engagement with users and increase sales.

#### Other Design Decisions

* The initial plan was to implement pagination across the site (particularly for larger searches such as 'all products').

However, I decided that given the current product catalog wasn't particularly large, that implementing pagination would have a navigate impact on user experience (i.e. having to click to load more products).

Had the product catalog been much larger (or should it grow in future) then it would make sense to implement this to balance against the response time for loading more products.

### Strategy

The key design principle of this site, is to keep the site very visual and not overcrowded with text (excluding products details, given users may want to understand more about any given product). 
Site visitors will generally be looking for a specific product(s) (or type of product(s)), and therefore it needs to be quick and easy for them to locate and purchase them.
The site therefore needs to be very intuitive, and have simple & easy to use navigation that is expected of e-commerce sites.

### Goals

#### Visitor Goals

The target audience for Hex Cosmetics are:
- People who are looking for a one-stop shop for their make-up products.
- People who value buying products from known brands.
- People who want 

User goals are:
- Easily find & purchase the makeup products that I want.
- Be able to navigate the shop quickly & easily.
- Feel confident that I am making a safe and secure purchase.
- Buy from a professional & trustworthy online shop.

#### Business Goals

The goals of the Hex Cosmetics business are:
- Provide a visually appealing online store that helps the user to feel safe that they are buying from a trustworthy source.
- Make sales of products easy for buyers to increase sales.
- Connect with customers through Hex Cosmetics social media/ increase social media following.
- Increase the Hex Cosmetics newsletter subscription.


### User stories

#### Viewing and Navigation
| Done | As a... | I would like to be able to... | So that I may...|
| ---- | ------- | ----------------------------- | --------------- |
|&checkmark;| user    | view a list of available products | identify if there are any products I would like to purchase |
|&checkmark;| user    | view individual products details | view the price, description and reviews |
|&checkmark;      | user    | View the total of my cart at any time | see how much money I will spend on the products I want to purchase |

#### Registration and User Accounts
| Done | As a... | I would like to be able to... | So that I may...|
| ---- | ------- | ----------------------------- | --------------- |
|&checkmark;| user    | register for an account | have an account to be able to store my details for repeat use |
|&checkmark;| user    | login or logout | to access my account and help ensure security of my personal information |
|&checkmark;| user    | log into my account using my Google account | speed up the registration process |
|&checkmark;| user    | recover my password | recover access to my account if I forget my credentials |
|&checkmark;| user    | have a personalized user profile | view my order history and store delivery information for future use |

#### Scrolling and Searching
| Done | As a... | I would like to be able to... | So that I may...|
| ---- | ------- | ----------------------------- | --------------- |
|&checkmark;| user    | sort the list of products| easily identify the best-priced products|
|&checkmark;| user    | search for a product by name or description. | find a specific product I would like to purchase |
|&checkmark;| user    | easily see what I have searched for | quickly decide whether the product I want is available |

#### Purchasing and Checkout
| Done | As a... | I would like to be able to... | So that I may...|
| ---- | ------- | ----------------------------- | --------------- |
|&checkmark;| user    | easily add or remove the product I want to purchase | easily make changes to my purchase before checkout |
|&checkmark;| user    | view items in my basket to be purchased  | confirm I am purchasing all the products I intend |
|&checkmark;| user    | view the total cost of the products | identify the total cost of my purchase and all the products I wish to purchase |
|&checkmark;| user    | enter my payment information  | check out and pay for the products I want to buy |
|&checkmark;| user    | feel my personal and payment information is safe and secure | confidently provide the needed information to make a purchase |
|&checkmark;| user    | view an order confirmation after checkout | verify that I have not made any errors and confirm that my order has been submitted |
|&checkmark;| user    | receive an email confirmation after checking out | keep the confirmation of what I have purchased for my records |

#### About HEX
| Done | As a... | I would like to be able to... | So that I may...|
| ---- | ------- | ----------------------------- | --------------- |
|&checkmark;| user    | view a list of frequently asked questions | identify the answer to a query I may have|
|&checkmark;| user    | view details about Hex Cosmetics | so that I can become more familiar with the brand |
|&checkmark;| user    | subscribe to the Hex Cosmetics newsletter | so that I can keep up to date with the latest products & offers |
|&checkmark;| user    | find Hex Cosmetics on social media | so that I can follow the brand and keep up to date with their latest content |

#### Admin and Store Management
| Done | As a... | I would like to be able to... | So that I may...|
| ---- | ------- | ----------------------------- | --------------- |
|&checkmark;| Admin   | add a product | add new products to the store |
|&checkmark;| Admin   | edit a product | change product prices, descriptions, images and other criteria |
|&checkmark;| Admin   | delete a product | remove products that are no longer for sale |
|&checkmark;| Admin   | have access to an admin dashboard | manage products and orders |
|&checkmark;| Admin   | view any previous order made | see what was purchased to ensure they get fulfilled |

### Wireframes

<details>
<summary>Home wireframes</summary>
<p align="center">
    <img height="400" src="https://i.ibb.co/hyfMTY2/Home.jpg">
</p>
</details>

<details>
<summary>Product Listing wireframes</summary>
<p align="center">
    <img height="400" src="https://i.ibb.co/1qvkjXM/Products-Search-Results.jpg">
</p>
</details>

<details>
<summary>Product Details wireframes</summary>
<p align="center">
    <img height="400" src="https://i.ibb.co/BTQhXLB/Listings.jpg">
</p>
</details>

<details>
<summary>Shopping Bag wireframes</summary>
<p align="center">
    <img height="400" src="https://i.ibb.co/8bkz570/Cart.jpg">
</p>
</details>

<details>
<summary>Shipping Details wireframes</summary>
<p align="center">
    <img height="400" src="https://i.ibb.co/CtDfCRQ/Checkout-Shipping.jpg">
</p>
</details>

<details>
<summary>Payment Details wireframes</summary>
<p align="center">
    <img height="400" src="https://i.ibb.co/k2ph0NT/Checkout-Payment.jpg">
</p>
</details>

<details>
<summary>Order Confirmation wireframes</summary>
<p align="center">
    <img height="400" src="https://i.ibb.co/mBQFSK9/Checkout-Order-Confirmation.jpg">
</p>
</details>

<details>
<summary>About us wireframes</summary>
<p align="center">
    <img height="400" src="https://i.ibb.co/5KnpP6g/About.jpg">
</p>
</details>

<details>
<summary>FAQs wireframes</summary>
<p align="center">
    <img height="400" src="https://i.ibb.co/dBnYDgZ/FAQs.jpg">
</p>
</details>

### Surface

#### Font

In-keeping with the clean, modern & simplistic design for the application, the font 'Quicksand' was chosen as the primary font for this site.

Quicksand is a display sans serif with rounded terminals.

It is designed for display purposes but kept legible enough to use in small sizes as well, and therefore is perfect for use across and should not cause any issues with users reading text.

A standard Sans-serif font is used as a back-up font, should there be any issues with loading the Quicksand font, and should not cause any significant issue with the look and feel of the site.

#### Logo

The logo is light pink, with a white image that looks like eyelashes. This fits with the brand and products offered by HEX Cosmetics.

The logo also displayed the HEX Cosmetics name and tagline.

There is also a version of the logo which just has the image, and this is used as the favicon for the site.

#### Colour Scheme 

The primary colour for the site is a light pink `#f8bab1` colour and was selected due to its likeness to many makeup products, and it is a bright fresh colour that is aesthetically pleasing.

* ![#f8bab1](https://placehold.it/15/f8bab1/000000?text=+) `#f8bab1` - Primary colour

This colour also matches the Hex Cosmetics logo, and therefore reinforces the brand look/ colour across the site. 

This primary colour is offset across the site by 2 text colours - black + white.

* ![#000](https://placehold.it/15/000/000000?text=+) `#000`
* ![#fff](https://placehold.it/15/fff/000000?text=+) `#fff`

The black text is the main text colour across the site and is used for its readability, as well as the contrast against the white background.

The white text is used against light pink `#f8bab1` backdrop, and is used to reinforce the brand colours (matching the logo etc.).

There are a few other colours used across the site (but much more sparingly):

Form text is grey and still offers a contrast to the white background, however provides a distinction from the black text that is used to display site/ product information.

* ![#6c757d](https://placehold.it/15/6c757d/000000?text=+) `#6c757d`

There is also the use of green (success), orange (warning), red(error) & lightblue (info) within the messages displayed on the site, and these offer a stark contrast to the primary colours used to draw the users attention to the message when it is displayed.

[Back to Top](#overview)

## Technologies and Tools

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - Used as the main language for the templates
* [CSS3](https://www.w3.org/Style/CSS/current-work.en.html)
    - Used for styling the webpage
* [Bootstrap](https://www.bootstrapcdn.com/)
    - CSS framework used to assist with website responsiveness.
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - Used mostly for DOM manipulation upon user interaction
* [jQuery](https://jquery.com/)
    - JavaScript Library to simplify and expedite JavaScript coding.
* [Python](https://www.python.org/)
    - Used for backend data manipulation
* [Django](https://www.djangoproject.com/) 
    - Python web framework for quick development.
* [Django-aullauth](https://django-allauth.readthedocs.io/en/latest/index.html)
    - Django authentication toolset
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) 
    - to style the django forms.
* [Jinja2 ](https://pypi.org/project/Jinja2/)
    - Used as the main language for template manipulation.
* [Pillow](https://pillow.readthedocs.io/en/stable/) 
    - Python imaging library to support opening, manipulating, and saving images.
* [Stripe](https://stripe.com/gb)
    - Payment infrastructure to validate and accept credit card payments securely.
* [Git](https://git-scm.com/) 
    - To handle version control.
* [GitHub](https://github.com/)
    - To store my project source code
* [Gitpod](https://www.gitpod.io/)
    - Used as my IDE
* [Google fonts](https://fonts.google.com/)
    - Used for website fonts
* [Font Awesome](https://fontawesome.com/)
    - To utilise the icon set.
* [Canva](https://www.canva.com/) 
    - used to design site to create the logo for Hex Cosmetics.
* [Balsamiq](https://balsamiq.cloud/) 
    - used to create the wireframes for this project.

## Database

* [SQlite3](https://www.sqlite.org/index.html) 
    - Used as development database.

[Back to Top](#overview)

## Features

## Future Features to implement

[Back to Top](#overview)

## Testing

### General code validation

* HTML validation with [W3C Markup Validation Service](https://validator.w3.org/). My code is fully compliant and there are no errors.
    - When completing the validation, I came across a few minor errors:
        - A couple of stray div end tags.
        - Missing alt attributes for a couple of images.
        - Some duplicate ids (see bug 3 for more detailed explanation)

* CSS validation with [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). My code is fully compliant and there are no errors.

* Javascript validation with [JSHint](https://jshint.com/). My code is fully compliant. There are some warnings about the undefined $ variable being used (e.g given the use of jQuery in my js files).
    - When completing this validation, I also identified a few missing semi colons from my code.

* Python validation with [PEP8 Online](http://pep8online.com/). My code is fully compliant, and there are no errors.
    - When completing the validation, I came across a few minor errors:
        - Mostly, these were lines being too long. I have updated the majority of these. There are some instances where I have intentionally left the line 'too long', where it would the code too unreadable.
        - It identified a couple of cases where imports were not being used, so I have removed them.
        - It also identified a couple of cases where variables had been assigned but not used.

### Unit Tests

#### How to run Python unit tests

To run the existing Python tests:
1. Activate your IDE.
2. In the terminal enter the following command: `python3 manage.py test`
    * If you wish to run the tests for a specific app you can enter the following command: `python3 manage.py test <app name>`
3. The test results will be shown within the terminal.

_NOTE: Depending on your IDE, the Python command may differ, such as `python` or `py`_

### Coverage

[Coverage.py](https://coverage.readthedocs.io/en/v4.5.x/) was used to provide feedback during testing. This was invaluable to identify which parts of my code the tests had covered.

#### How to run coverage

To view the coverage, you can run the following commands:

1. `coverage run --source=. manage.py test` This will run all tests/
2. `coverage report` The coverage will be shown within the terminal, broken down by .py file.
3. You can view an interactive version by using `coverage html`, and then `python3 -m http.server`, and you can view the htmlcov folder in the browser, select specific files, and view which particular sections of code are or aren't being covered by the e


### Browser & Device Compatibility

| **Browser**      | **Device** | **Compatibility**                                            | **Version**            |
| :--------------- | :--------- | :----------------------------------------------------------- | :--------------------- |
| Google Chrome    | PC         |                                                              |                        |
| Microsoft Edge   | PC         |                                                              |                        |
| IE 11            | PC         |                                                              |                        |
| Google Chrome    | Mobile     |                                                              |                        |
| Firefox          | Mobile     |                                                              |                        |
| Microsoft Edge   | Mobile     |                                                              |                        |
| Mi Browser       | Mobile     |                                                              |                        |
| Safari           | iPad       |                                                              |                        |


### Google Lighthouse

| **Device** | **Performance** | **Accessibility** | **Best Practices** | **SEO** |
| :----------| :---------      | :-----------------| :----------------- | :------ |
| Desktop    |                 |                   |                    |         |
| Mobile     |                 |                   |                    |         |


### Functional testing


### Bugs & Interesting Issues Encountered & Fixed

1. The first interesting bug/ hurdle I encountered was when implementing the sorting filter (by price/ rating). The issue I found was that when I initially created the function, the URL was only designed to pass in the sort type and direction, and thereore if I had already filtered the list to a specific category, using the sort order returned all products.
    - To fix this I needed to pass in the category (if it had be selected). I utilised slugs to help acheive this (which also improved the URL naming) and passed these arguments into the all_products view.

2. Following the implementation of slugs, I had the issue when attempting to view 'all products' as I was getting a NoReverseMatch error, in this case because a catgeory slug was not being passed into my href url against each product.
    - To fix this I created the get_absolute_url model method in the product class, to allow me to obtain the catgeory slug via the Product Class, and pass this, and the product slug as args.

3. I have multiple forms/ models which have an email field include. When using django crispy forms, this was creating elements with the same ID. This wouldn't be an issue, except the subscription form is passed to every page via a context processor, and therefore was creating some duplicates.
    - To fix this, I simply update the field name from email to email_address, and this meant when two forms were on the same page, that they had different IDs.

4. When updating the quantity in the basket, I was submitting the form each time a user clicked the increment/ decrement button, which was updating the quantity as expected, but sometimes resulted in multiple messages being displayed on screen.
    - To fix this, I added a timer, so that the form would only submit 1 second after the button had been pressed, and the timer would be reset

[Back to Top](#overview)

## Deployment

### Requirements

To allow you to access all functionality you will require access to the following (free services are sufficient):

* [Stripe](https://dashboard.stripe.com/register)
    - [Test Keys](https://stripe.com/docs/keys)
    - [Webhook Secret](https://stripe.com/docs/webhooks/signatures)

* [AWS](https://aws.amazon.com/)
    - [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

* [Google Account](https://support.google.com/accounts/answer/27441?hl=en)
    - [App Password](https://support.google.com/mail/answer/185833?hl=en-GB)

Documentation above to confirm how to create the account, and locate the required environment variables.

### Environment Variables

| Variable Name         | Comment                                                       | 
| --------------------- | ------------------------------------------------------------- |
| USE_AWS               | To use AWS S3 for static & media files instead of local files |
| AWS_ACCESS_KEY_ID     | Access to AWS S3 Bucket - Generated by AWS                    |
| AWS_SECRET_ACCESS_KEY | Access to AWS S3 Bucket - Generated by AWS                    |
| DATABASE_URL          | Can be automatically generated using Heroku Postgres add-on   |
| HEX_SECRET_KEY        | The Django Secret Key for securing signed data                |
| EMAIL_HOST_PASSWORD   | App password to sign in to gmail. Generated in Google Account |
| EMAIL_HOST_USER       | App user / email for gmail. E-mails sent from this address    |
| STRIPE_PUBLISHABLE    | To identify your account with Stripe                          |
| STRIPE_SECRET         | To perform an API request to Stripe                           |
| STRIPE_WEBHOOK_SECRET | Secret key for webhook endpoint                               |
| PRODUCTION            | To run in production mode with DEBUG = False                  |
| DEBUG                 | CAUTION - This is optional and will set DEBUG in Production   |

For Local Deployment, you can replace `PRODUCTION` with `DEVELOPMENT`. This will set DEBUG to TRUE.

### Cloning

The site can be cloned to your local repository as follows steps - [GitHub guide](https://help.github.com/en/articles/cloning-a-repository):

1. On GitHub, navigate to the main page of the repository.

2. Above the list of files, click the 'Code' button. To clone the repository using HTTPS, select HTTPS and copy the URL.

3. in your IDE, change the current working directory to the location where you want the cloned directory.

4. Type git clone, and then paste the URL you copied earlier - `git clone https://github.com/<USERNAME>/<REPOSITORY>` - and press enter.

5. The clone will be created.

6. Install all required modules using the command
    - `pip install -r requirements.txt.`

7. Migrate the models to create your test database (i.e. in SQLite) using the following command.
    - `python manage.py migrate`

8. You can load the fixtures using the following commands (they must be completed in order).
    - `python manage.py load data categories`
    - `python manage.py load data products`
    - `python manage.py load data colours`

9. Create your superuser to access the django admin panel and database using the following command (then follow the instructions in your command line)
    - `python manage.py createsuperuser`

10. You can now run locally using the following command.
    - `python manage.py runserver`


### Continuous integration

You can implement automated testing before deployment to ensure that all tests are passed prior to changes being deployed to the live site.

Instructions for setting this up can be found at [Travis-CI](https://docs.travis-ci.com/user/tutorial/)

1. Sign up to Travis CI via your Github profile.
2. Grant Travis CI with the required authorisations to your Github.
3. Activate your account and select your repo to connect for Travis-CI.
4. Travis-CI will run the .travis.yml file and provide feedback if there are any errors preventing deployment (i.e. failed tests or missing environment variables).

### Heroku Deployment

To deploy this site to Heroku, complete the following steps:

1. Create a [Heroku](https://signup.heroku.com/) account and log in.
2. Create a new app in Heroku
3. In the settings tab, set the [Environment Variables](#Environment-Variables) detialed above
4. From the Heroku dashboard of your application, click on "Deploy" > "Deployment method" and select GitHub.
5. Connect to the appropriate GitHub repository.
6. Set the project up for automatic deploys it will deploy once the master branch is updated.
    - OR in the manual deployment section, select the master branch and click 'Deploy Branch'.
7. You can also select the option for 'Wait for CI to pass before deploy', which will ensure the Travis-CI build is successful prior to deployment.
8. The site should be successfully deployed.

If you do not set the project up for automatic deploys, you are also able to push updates from your command line.
- login to Heroku using the command `heroku login` and complete your user details.
- Push to Heroku using the command  `git push heroku master`.

### Contributions

1. If you wish to implement changes to the code, I would recommend creating a separate branch, as this will keep the original master branch as a backup if the any issues arise.
2. Use `git checkout -b <branchname>` to create a new branch.
3. You can now edit the code accordingly.
4. Once you have made changes, you need to stage the changes to be committed. You can do this as follows `git add <filename>` for a single file or `git add .` to stage all updated files.
5. You then need to commit the changes. You can do this as follows `git commit -m "summary of updates"`.
4. Use `git push origin <branchname>`to push the changes to the branch in the repository.
5. You will need to merge these changes to the master branch in order for them to be deployed to the live site.
6. To do this, switch to the new branch on GitHub using the branch selector dropdown menu.
7. Create a new pull request, note the changes made in the comments section, and merge.

[Back to Top](#overview)

## Credits

### Content

* [kaggle](https://www.kaggle.com/oftomorrow/herokuapp-makeup-products) my fixture data was obtained from this dataset. I then pruned the data to extract the relevant data that was loaded into the project.
* [TheBrandBoy](https://thebrandboy.com/make-up-company-about-us/) the content of my about us page was copied from this page, and the wording altered slightly for grammatical purposes.
* [mdbootstrap](https://mdbootstrap.com/snippets/jquery/mdbootstrap/949845#css-tab-view) the order progress section in my basket/checkout pages adapted the code found on this page (html & css).
* [Stackoverflow](https://stackoverflow.com/questions/19966417/prevent-typing-non-numeric-in-input-type-number) I adapted the solution on this page to stop non numeric characters being entered into the input box on the basket page.

### Images
* [kaggle](https://www.kaggle.com/oftomorrow/herokuapp-makeup-products) The Kaggle data set contains applicable URLs to all product images across the site.
* [Pixabay](https://pixabay.com/) The category images were sourced from the Pixabay images library, and are all free for use, sharing or modification.

### Acknowledgements

* [learndjango](https://learndjango.com/tutorials/django-slug-tutorial) + CI Tutor Miklos Sarosi for guidance on implementing slugs into my project to assist with 'bug #1 / #2'.
* [Code Institute](https://codeinstitute.net/) For the excellent overall content & mini projects within the course.
* [ckz8780 - Github](https://github.com/ckz8780/boutique_ado_v1) ckz8780's fantastic Django module produced for the Code Institute has been invaluable in providing guidance for creating key functionality across the project.
* [Django documentation](https://docs.djangoproject.com/en/3.1/topics/testing/advanced/) for guidance on the setUp and tearDown test methods to keep the database clean.
* [Django documentation](https://docs.djangoproject.com/en/3.1/topics/testing/tools/) for guidance on the available testing tools and required arguments to be passed etc.
* [Stackoverflow](https://stackoverflow.com/questions/4424435/how-to-convert-a-django-queryset-to-a-list) for guidance on transforming data for assertQuerysetEqual tests.
    - [w3schools](https://www.w3schools.com/python/python_lambda.asp) for explanation of Lambda function.
* [Stackoverflow](https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages) for guidance on testing messages.
* [Stackoverflow](https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places) for guidance on how to fix an issue when testing the order model which was preventing me from matching values due to floating point imprecision. 
* CI Tutor Kevin, for his guidance on test unit testing for my basket. I was having an issue with passing the correct data in the post request (which was resulting in a 404 error), and Kevin pointed out that I had incorrectly named a parameter that I was passing as post data.
* [Flickity](https://flickity.metafizzy.co/style) for guidance on the styling of the slider for my featured products.
* [Medium](https://whizzoe.medium.com/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5) for guidance on how to set up the Google social login/ registration.
* [Travis-CI](https://docs.travis-ci.com/user/languages/python/) for guidance on how to create the .yml file for my continuous integration builds + ensuring all tests pass before deployment to Heroku.
* [Stackoverflow](https://stackoverflow.com/questions/39985774/custom-404-django-template) for guidance on creating custom error templates.
* [Stackoverflow](https://stackoverflow.com/questions/3015319/settimeout-cleartimeout-problems) for guidance on the timeout issues I was having when updating the basket quantity, see bug/fix #4.
* [w3schools](https://www.w3schools.com/howto/howto_css_hide_arrow_number.asp) for guidance on how to update the input field so the default up/down arrows weren't displayed.

[Back to Top](#overview)

