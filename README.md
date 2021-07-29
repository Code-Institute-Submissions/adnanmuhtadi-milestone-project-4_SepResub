<h1 align="center">Milestone Project 4 - Clout Mafia</h1>

[View project here](#)

This eCommerce site is based on advertising and selling exclusive sneakers. The target market audience has a unique market for individuals who have a taste in fashion. Being able to register/login/log out as well as adding/updating/deleting items from the inventory as well as the shopping basket. Giving users the different options of sneakers and sizes as well as being able to search for them to select from depending on availability. 

As the business is a startup, products sold will still be advertised but marked sold disabling and removing the opportunity to be repurchased. The reason for this approach is to build the hype for the user client tell and to showcase what users have missed out on. 

This site would be utilizing Python and Django which was taught from the Code Institute. I will also be using various technologies such as HTML5, CSS3, JQuery and Bootstrap. This project will be responsive and accessible to different size browsers and devices.

<h2 align="center"><img src="https://clout-mafia-ms4.herokuapp.com/"></h2>

## User Experience (UX)

### The Audience

The intended audience for this project is individuals who are into casual contemporary fashion, namely exclusive designer footwear and streetwear.

### User Objectives

To be able to find and purchase a pair of sneakers easily. Navigate through the site with a consistent layout and structure making the sneakers clear to be seen and accessible. When a pair of sneakers is selected, it will direct the user to a detailed product page, which would display a larger picture of the product, a description and sneaker size.

After having some items added to the basket, to be able to preview the selected sneakers and to see the total price. Once decided to make an order, to be able to go and check out and put in all the card details to purchase the items. To also have the ability to create an account and store the previous orders associated with the account.

Having an additional option to post a testimonial about the service/website to share with other users and having it displayed on the home page to be seen by other users.

### My Objectives

To create a site that would allow a user to register and have a profile on the site. For the user to be able to search for a product and select it to find out more details about it. Either on the products page or the product detail page, the user would be able to add the product to the shopping basket. Then having the user then go to checkout and purchase their order.

The site would have a CRUD software architectural style (Create, Read, Update and Delete) for basic operations of persistent storage with the products being added by the admin user. Validation would be included in the site when it comes to adding products, user details and user card details. When a user sends an email to the site admin, to have the subject automatically post to the database for analysing. 

### User Stories

The intended type of users which this website is targeted for are individuals who enjoy online shopping and have a unique taste is fashion.

1. As a user, I want to be able to view a list of products, so that I can purchase one of them.
1. As a user, I want to be able to view the details of an individual item, so I can see the price, description, product image and available size.
1. As a user, I want to be able to sort the sneakers, so I can identify the best priced and alphabetically 
1. As a user, I want to be able to sort a specific category of sneakers, so I can find the specific sneakers I am looking for
1. As a user, I want to be able to search by name and/or description, so I can find sneakers easily
1. As a user, I want to be able to see the number of results that appear from my search, so I can see how many sneakers are available from my search
1. As a user, I want to be able to select the size and quantity of a pair of sneakers, so I can ensure I purchase the right size and amount of my desired order
1. As a user, I want to be able to easily register for an account, so I can have a personal account within the site and be able to view my personal information
1. As a user, I want to be able to recover my password, so I can recover it if needed.
1. As a user, I want to be able to view a personalised profile page, so I can view my personal information as well as my order history
1. As a user, I want to be able to view the overall total of my shopping bag, so I can see my total spending
1. As a user, I want to be able to update my shopping bag at the checkout by updating the quantity of my order, so I can have the option to change my mind if I don’t want to spend as much
1. As a user, I want to be able to easily enter my payment details, so I can easily purchase my items
1. As a user, I want to be able to view an order confirmation after I have purchased my items, so I can verify my purchase order.
1. As a user, I want to be able to post a testimonial, so I can express my opinion of the service/website.
1. As a user, I want to be able to see the products that have already been sold, so I can see the other types of products I have missed out on and what this company has already sold
1. As a site owner, I want to be able to add a product, so I can a new pair of sneakers to my store
1. As a site owner, I want to be able to edit, update a product in my store, so I can amend the name, price, description, image and any other product details
1. As a site owner, I want to be able to mark a product as sold when a product has been purchased, so I can ensure it will not be purchased again
1. As a site owner, I want to be able to delete a product, so I can remove the product from my store.
1. As a site owner, I want to be able to see a list of subjects that get used when contacting the site admin, so I can see what user are mostly asking

### Design
-   #### Colour Scheme
    -   The colour scheme I will be working with is mainly black and white to keep it simple and easy on the eyes. The concept is to make the images of the sneakers be the focus of the site.

-   #### Typography
    -   I have chosen to use [Barlow Condensed](https://fonts.google.com/specimen/Barlow+Condensed) and [Sarabun](https://fonts.google.com/specimen/Sarabun) font as the main fonts throughout the website with Sans Serif as the emergency font in the case for any reason the font is not being imported into the site correctly. Both [Barlow Condensed](https://fonts.google.com/specimen/Barlow+Condensed) and [Sarabun](https://fonts.google.com/specimen/Sarabun) are attractive fonts to use as it easy to clear and easy to read. [Barlow Condensed](https://fonts.google.com/specimen/Barlow+Condensed) would be used for all the headers of the site whereas [Sarabun](https://fonts.google.com/specimen/Sarabun) would be used for the rest of the content

-   #### Imagery
    -   The images that were used as based on the purpose of the site being focused on selling sneakers. All images have been taken personally as I would also be advertising sneakers that have been sold before this project. Other images for this project were taken from [Unsplash](https://unsplash.com/)

*   ### Wireframes

    #### Home Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/home-page.pdf)

    - I altered the design during development by not including the categories under the testimonials as it was redundant while having the categories displayed permanently in the footer

    #### Register Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/register-page.pdf)

    #### Login Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/login-page.pdf)

    #### All Products Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/all-products-page.pdf)

    - I altered the design during development as having 4 items in a row looked better than having 3 items in a row.

    #### Product Details Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/product-details-page.pdf)

    #### Basket Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/bag-page.pdf)

    - I altered the design during development and not included the quantity due to the fact it's not the purpose of the site.

    #### Checkout Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/checkout-page.pdf)

    #### Order Confirmation Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/order-confirmation-page.pdf)

    #### Superuser Add/Edit Product Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/superuser-add-edit-product.pdf)

    #### Testimonials Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/testimonials-page.pdf)

    - I altered the design during development as the form meant more meaningful when having ratings and title behind the message

    #### Shipping & Returns Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/shipping-and-returns-page.pdf)

    #### Privacy Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/privacy-page.pdf)

    #### Terms & Conditions Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/terms-page.pdf)

    #### About Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/about-page.pdf)

    #### Contact Us Page - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/contact-us-page.pdf)
    
    #### Master Wireframes
    - Master Wireframes - [View](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/wireframes/clout-mafia-wireframes.bmpr)
    
#### Database Structure

During the development of my project, I was using sqlite for my database, but then changed over to postgres when it was deployed (Postgres is an addon provided by Heroku).

Database Structure - [View Tables](https://github.com/adnanmuhtadi/milestone-project-4/blob/main/documentation/database/database_structure.md)

#### Database Mapping

The database was designed using an online tool called [DB Diagram](https://dbdiagram.io/). The tables where mapped depending on the field requirements.

Database Design - [Mapping](#)

## Features

The features that will be utilised in this project will be as follows:

### Existing Features

#### Site Features

-   Responsive on devices sized 1024px, 768px, 425px, 375px and 320px.
-   Navigation bar and footer are pulled from the base file throughout all pages.
-   Different navigation bar options depend on the type of user who accesses the site.
-   Offer header is fixed throughout the site and changes depending on screen size
-   Navigation changes with screen size and different users have different access depending on their access
-   Footer is displayed across the site with different site pages, (note: Refunds, Privacy, T&C's pages work but only for visual elements and taken from other websites) 

#### Home Page

-   Carousel will rotate and will take the user to different parts of the shop depending on the carousel and button
-   Testimonials are fetched from the database and display the newest three

#### Registration Page

-   Email validation if the emails do not match and if the email has already been used
-   Password validation error appears if the passwords don't match

#### Login Page

-   Validation if either the email and/or password is wrong

#### Profile Page

-   To see the history of the user previous orders
-   To be able to revisit the order confirmation of a previous order once clicked on.
-   To view and update the current delivery details

#### Products Page

-   Displayed multiple products on the page with images as well as product details
-   A buy a now button under each product and updating the basket.
-   Successful message with the product added to the basket appears.
-   Error message appears when the same time has been added more than once in the basket
-   Search criteria looks searches within the title and description of each product
-   Site admin has the power to edit and delete products from that page if desires. 
-   Can sort items via multiple options.
-   Once the product has been purchased and is confirmed in a checkout order summary, that specific product would have the 'Buy Now' button removed and would have the product marked sold. The reason behind that is due to the early stages of the business as it is trying to build up the hype for the users. It is to display what users have missed out on while informing at the same time the kind history of designs that has come to store.

#### Shopping Bag Page

-   Displays the products and their details that have been selected in one view
-   Option to delete the product from the basket
-   Confirmation appears once a product has been removed from the basket
-   Price updates when the basket has been altered
-   Overall summary prices are stuck on the side view so it is always visible

#### Checkout Page

-   Order summary available at checkout page
-   Option to save user details to the profile if they have an account
-   Stripe validation if card entered is wrong
-   Option to adjust the shopping basket before proceeding to payment

#### Checkout Success Page

-   Email confirmation when the order has been completed
-   Order number generated and is displayed
-   Basket clears once the order has been completed
-   Product marked as sold once checked out

#### Testimonial Page (Add/View/Delete/)

-   To add a title, a message and a rating out of 5
-   To view and sort the testimonials once posted with the ability to sort via different methods
-   Testimonial owners can Edit/Delete their posts
-   Site admins can Edit/Delete any testimonial that has been posted
-   Each testimonial post are added to the database

#### About Page

-   Google Maps Api connected to the site to identify where the 'Business' is based

#### Checkout Success Page

-   Once a user contacts the site admin, the site admin would receive an email
-   Once a user contact the site admin, The email would be saved to the database for the capabilities for furth analytics

### Features Left to Implement

-   For a button to appear allowing the user to go back to the top of the page.
-   Continue working with AllAuth, enabling the password reset
-   To add Pagination, so the user can see up to 20 items per page
-   A page for the site admin to see the email states instead of logging into Django admin.

## Technologies Used

###  Programming Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - HTML5 was used to structure and present content on my website.
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - CSS3 was used to provide my website with style.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - JavaScript was used to make the site interactive.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - Python was used as the backend language to access and parse data.

### APIs, Databases, Frameworks, Libraries, Programs and Templates Used

#### APIs
1. [Google Places:](https://developers.google.com/maps/documentation/places/web-service/overview
    - Google Places were used to use google maps in my ‘About’ page to show the address of the business

#### Databases
1. [DB Diagram](https://dbdiagram.io/)
    - Online tool to design the database.
1. [SQLite3:](https://www.sqlite.org/index.html)
    - Database which stores the data to be recalled onto the website.
1. [Heroku Postgresql:](https://www.sqlite.org/index.html)
    - Reliable and powerful database as a service based on PostgreSQL.

#### Frameworks
1. [Bootstrap:](https://getbootstrap.com)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [JQuery Core:](https://code.jquery.com/)
    - JQuery library was implemented to use features within Materialize

#### Library
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

#### Programs
1. [Google Chrome:](https://www.google.co.uk/intl/en_uk/chrome/)
    - Default browser is used to visually display the build process as well as utilising Chrome Dev Tools to assist where needed.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the code of the project after being pushed from GitPod.
1. [Visual Studio Code](https://code.visualstudio.com/)
    - Code editing software was used to replace GitPod as the free license expired due to over 50 hours of usage. 
1. [GitHub Desktop:](https://desktop.github.com/)
    - A tool that allows you to interact with GitHub from the desktop
1. [Grammerly:](https://app.grammarly.com/)
    - Online tool which assists with English grammar.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](#) during the design process.
1. [Stripe:](https://stripe.com/gb)
    - Online payment processing for internet businesses.
1. [Heroku:](https://www.heroku.com)
    - A platform as a service (PaaS) that enables me to deploy my website in the cloud.
1. [AWS:](https://aws.amazon.com/?nc2=h_lg)
    - Amazon Web Services (AWS) is a secure cloud services platform, allowing the running web and application servers in the cloud to host dynamic websites.

#### Other
1. [Django Secret Key Generator:](https://miniwebtool.com/django-secret-key-generator/)
    - The Django Secret Key Generator is used to generate a new SECRET_KEY that you can put in your settings.py module.

## Testing

...

### Validation


On code completion, I ensured my code was validated with no snytax errors. I used [W3C Markup Validator](https://validator.w3.org/) for HTML5, [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) for CSS3 to ensure my code is W3C Compliant. I used [JSHint](https://jshint.com/) to helps to detect errors and potential problems in your JavaScript code. I also used [PEP8 Online](http://pep8online.com/) to validate my python scripts

#### Results

Page | Initial Errors | Resolved Errors | Error Notes
------------ | ------------- | ------------- | -------------
index.html| [Initial Errors](#) | [Resolved Errors](#) | ...

or use this template

#### HTML - [W3C Markup Validator](https://validator.w3.org/)

- 

#### CSS - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - [Results](#)

- 

#### JS - [JSHint](https://jshint.com/) - [Results](#)

- 

#### Python - [PEP8 Online](http://pep8online.com/) - [Results](#)

- 

### Further Testing

#### User Stories Testing from User Experience (UX) Section - [View Results](#)



#### Functionality and Usability Testing - [View Results](#)



#### Browser and Responsive Testing



### Known Issues

- 

## Deployment

### Making a Clone



### Making a Deployment



## Credits

### Content



### Code



### Media



### Acknowledgements

