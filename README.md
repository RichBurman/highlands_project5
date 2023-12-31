![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Highland Adventures

![Am I Responsive Image](https://res.cloudinary.com/dbagkfamv/image/upload/v1700340031/am_I_responsive_qf6uyg.png)

Github link to the project [Github link](https://github.com/RichBurman/highlands_project5)

Live Link to the project website [Live link](https://highlands-fe23cbc4972e.herokuapp.com/)

## CONTENTS

- [Highland Adventures](#Highland-Adventures)
  - [CONTENTS](#contents)
  - [User Experience (UX)](#user-experience-ux)
    - [Key Information for the site](#key-information-for-the-site)
    - [Business Model](#business-model) 
    - [User Stories](#user-stories)
      - [User Features](#user-features) 
      - [Admin Features](#admin-features)
      - [Client Goals](#client-goals)
      - [First Time Visitor Goals](#first-time-visior-goals)
      - [Returning and Frequent Visitor Goals](#returning-and-frequent-visitor-goals)
  - [Design](#design)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [WireFrames](#wireframes)
  - [Features](#features)
    - [Home Page](#home-page)
    - [The Navigation Bar](#the-navigation-bar)
    - [Footer](#footer)
    - [View Packages](#view-packages)
    - [Package Detail](#package-detail)
    - [About Us](#about-us)
    - [Gallery](#gallery)
    - [Review](#reviews)
    - [Cart](#cart)
    - [Checkout](#checkout)
    - [Order Confirmation](#order-confirmation)
    - [User Reviews](#user-reviews)
    - [Login/Logout](#loginlogout---set-up-using-allauth)
    - [Register](#register---set-up-using-allauth)
    - [User Profile Details](#user-profile-details)
    - [Admin Features](#admin-features)
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

- Highland Adventures is a e-commerce website designed for outdoor hikers and businesses alike, offering a diverse range of hiking packages. It is open for individuals or businesses planning team building events, Highland Adventures offers the perfect hiking package in the Scottish Highlands. 

### Key Information for the site

- A Range of Hiking Packages - available to purchase catering to various preferences and difficulty levels
- User Friendly Experience - user-friendly website making it easy for users to browse, select and purchase hiking packages
- Exclusive Discount for Registered Users - Signing up to become a member and you enjoy discounts. Starting with a discount of 10% on all bookings, which shows on the website to those users that are registered. 
- Secure Account - User accounts and personal is kept safe and secure. 
- Streamlined ordering process - Simple system to allow users to easily place an order. 
- Review Pages - Users can share their personal experience of the hiking packages they have purchased on the reviews. They can also view these reviews prior to making a purchase to see what other users have said about the packages. 

### Business Model

- Highland Adventures

- Highland Adventures operates on a dynamic e-commerce business model, serving both the Business-to-Business (B2B) and Business-to-Consumer (B2C) markets. Our platform is the gateway for outdoor enthusiasts and businesses to explore, purchase, and organise unforgettable hiking experiences in the Scottish Highlands.

- Core Business Intents

- Our business strategy revolves around providing a seamless and enjoyable experience for users, whether they are individual consumers or businesses seeking corporate adventures. Key aspects of our strategy include:

- Curating a Diverse Range of Hiking Packages

- Offering a wide array of hiking packages to cater to various preferences and skill levels.

- User-Friendly Platform

- Ensuring our website is user-friendly, making it easy for users to browse, select, and purchase hiking packages.

- Exclusive Discounts

- Providing registered users with exclusive discounts to incentivise account creation and foster loyalty.

- Secure User Accounts

- Implementing robust security measures to safeguard user accounts and personal information.

- Efficient Order Management

- Streamlining the order placement, processing, and fulfillment process for both individual and corporate clients.

- Community Engagement

- Encouraging user engagement through reviews, ratings, and fostering a sense of community on our platform.

- We have a fantastic facebook business page! 

![Facebook Business Page](https://res.cloudinary.com/dbagkfamv/image/upload/v1700340288/facebook_business_page_idefss.png)


### User Stories

![User Stories](https://res.cloudinary.com/dbagkfamv/image/upload/v1700340281/user_stories1_jzndtw.png)

## User Features

1. **I want to** browse a list of available hiking packages, **so that I can** select which ones I would like to purchase.
2. **I want to** view the details of a specific hiking package, **so that I can** make an informed decision on which one I would like to purchase.
3. **I want to** register an account on the website, **so that I can** access exclusive discounts and have a profile.
4. **I want to** log in and out of my account, **so that I can** access my account and enable secure interactions when logged in.
5. **I want to** update my profile information (name, email, address, phone number, etc.), **so that I can** ensure personal information is up to date and improve the user experience.
6. **I want to** add hiking packages to my shopping cart, **so that I can** use the items when checking out and purchasing.
7. **I want to** view the contents of my shopping cart, **so that I can** review my choices and make adjustments if needed.
8. **I want to** place an order for the hiking package in my cart, **so that I can** complete the booking process by confirming and buying the package.
9. **I want to** submit reviews for hiking packages I have purchased or experienced, **so that I can** share my experiences about a package and provide helpful feedback to users and administrators.
10. **I want to** edit and delete my own reviews, **so that I can** make corrections to a review or delete it altogether.
11. **I want to** see ratings on reviews to quickly gauge the quality of a hiking package, **so that I can** quickly assess the quality or popularity of packages to aid my decision-making.

## Admin Features

1. **I want to** log in and log out of my admin account, **so that I can** have secure access to the website admin features while keeping this information protected.
2. **I want to** manage the list of available hiking packages, including adding, editing, and deleting packages, **so that I can** edit and maintain the list, ensuring it is up to date and correct.
3. **I want to** view a list of registered users and their profile information, **so that I can** address inquiries or issues and ensure a safe, secure, user-friendly experience.
4. **I want to** access and manage user orders, including viewing details and updating the status of an order, **so that I can** oversee and process orders, track sales, and address any issues.
5. **I want to** access and manage user reviews, including the ability to edit and delete reviews, **so that I can** ensure reviews adhere to community guidelines and address anything inappropriate.
6. **I want to** receive notifications or emails when a new order is placed or when a user submits a review, **so that I can** be kept informed of important events happening on the website and respond in a timely fashion.
7. **I want to** view statistics and analytics on website usage, e.g., popular packages, sales trends, etc., **so that I can** make decisions based on the data to enhance the website offerings and user experience.

Github Project

![Github Project](https://res.cloudinary.com/dbagkfamv/image/upload/v1700340872/Github_Project_bzjxkl.png)


#### Client Goals

- My client goals for this website are the following:
    - Increase sales for the client selling the hiking packages to an online market.
    - Enchance User Experience - Making a user friendly website were users can navigate easily and complete any purchases with ease. 
    - Build Brand Awareness - With the website, the mailchimp newsletter set up and a facebook business page, this opens up Highlands Adventures to a wide range of new market of potential customers. 
    - Customer Loyalty - Offering a online discount on orders encourages users to sign up to the site, which encourages loyalty and repeat business
    - Ensuring Security and Data Protection - Ensuring the client meets security and data protection that is needed for online transactions and hosting a secure environment. 
    - Improving the SEO Ranking - Adding robots.txt and sitemap.xml and key meta data to the website encourages a higher ranking on SEO. 

#### First Time Visitor Goals

- My goals for users visiting the website for the first time are the following:
    - The website capturing the attention of the user and that they fully understand easily what the website is about and what it offers. 
    - Easy Navigation around the website, making it easy to find the information they want. 
    - Highlight the key features of Highland Adventures, the packages, the locations, the discount available
    - Encourage them to become a member, with offering them exclusive discount for purchasing packages online. 
    - Encouraging the use of the social media links, where users may be able to find out more information about Highland Adventures, but crucually share Highland Adventures to friends and family which hopefully results in more visitors to the website and potential new customers and therefore more sales. 
    - Encouraging the user to read reviews of previous users experiences and encourage more sales.

#### Returning and Frequent Visitor Goals

-  My goals for returning users are the following:
    - Encouraging users to book new packages after their first booking. With the addition of the review section, users will return to the site to fill in their review of their package and hopefully book another one! 
    - New packages would be highlighted to returning users on the home page and in the packages page. Also with the newsletter and Facebook business page, this is another method of marketing to the user if they haven't recently visited the website. 
    - Community - with the review section, users are encouraged to come back and read the reviews on the other packages and this may encourage them to make a purchase, as long as the reviews are positive! 

## Design

### Typography

- Default fonts were used for the following:
- Headings
- Body
- Messages
- Font Awesome

### Imagery

- Some Images were used from the [Unsplash](https://unsplash.com/) website.
- All other images are owned by Author Richard Burman

### Wireframes

- Below are the Wireframes for the project website. 
- Home Page Wireframe
- ![Home Page Wireframe](https://res.cloudinary.com/dbagkfamv/image/upload/v1701780326/wf_homepage_fhmmgi.png)
- Walking Packages Wireframe
- ![Walking Packages Wireframe](https://res.cloudinary.com/dbagkfamv/image/upload/v1701780327/wf_walkingpackages_rwun7p.png)
- View Package Wireframe
- ![View Package Wireframe](https://res.cloudinary.com/dbagkfamv/image/upload/v1701780326/wf_viewpackage_n9yajf.png)
- About Us Wireframe
- ![About Us Wireframe](https://res.cloudinary.com/dbagkfamv/image/upload/v1701780326/wf_aboutus_q3s5ha.png)
- Gallery Wireframe
- ![Gallery Wireframe](https://res.cloudinary.com/dbagkfamv/image/upload/v1701780326/wf_gallery_jikfbh.png)
- Review Wireframe
- ![Reviews Wireframe](https://res.cloudinary.com/dbagkfamv/image/upload/v1701780326/wf_reviews_xpwgxv.png)
- Individual Review Wireframe
- ![A Review Wireframe](https://res.cloudinary.com/dbagkfamv/image/upload/v1701780326/wf_reviewdetail_rl15ms.png)
- Cart Wireframe
- ![Cart Wireframe](https://res.cloudinary.com/dbagkfamv/image/upload/v1701780325/wf_cart_pw19mx.png)
- Checkout Wireframe
- ![Checkout Wireframe](https://res.cloudinary.com/dbagkfamv/image/upload/v1701780325/wf_checkout_cems79.png)
- Order Confirmation Wireframe
- ![Order Confirm Wireframe](https://res.cloudinary.com/dbagkfamv/image/upload/v1701780325/wf_orderconfirm_d8nd0k.png)


## Features

- The website consist of 20 html pages. Below in no particular order:
    - cart.html
    - checkout_success.html
    - checkout.html
    - about_us.html
    - gallery.html
    - index.html (Home Page)
    - package_detail.html
    - package_list.html
    - add_review.html
    - delete_review.html
    - package_reviews.html
    - review_list.html
    - update_review.html
    - user_reviews.html
    - 404.html
    - base.html
    - custom_user_edit.html
    - display_user_profile.html
    - user_profile_edit.html
    - user_profile.html

    - Base.html is not accessible as a stand-alone page for the user, as it is used at the base template to host the other html pages (aside from 404.html)
    - All other pages are accessible to registered users (depending on their journey on the wesbite, i.e. will see checkout_sucess if they successfully make a purchase of a hiking package)
    - Non registered users are limited to the following pages
        - index.html (Home Page)
        - package_list.html
        - package_detail.html
        - gallery.html
        - review_view.html
    - The reasoning behind this only registered users can make purchases or add reviews on the website and therefore non registered users do not need access to these pages. 

    ### Home Page

    - This is the index/landing page for the website. 
    - It had a clear heading and brief information section informing the user what the website is about. 
    - It has a large image of Ben Nevis to draw the user into the website and capture their attention. 

    ![Home Page](https://res.cloudinary.com/dbagkfamv/image/upload/v1700343694/homepage1_m8ciea.png)

    ### Home Page Image 2

    - This section of the home page is broken into sections to provide the user with information on the following:
        - Brief information section - Explains what we offer on the website
        - Why Join Us? - Explains the benefits of becoming a registered user.
        - Booking Made Easy - Explains the ease of booking a package with us. 
        - Stay in the Loop - Explains about signing up for our newsletter

    ![Home Page Image 2](https://res.cloudinary.com/dbagkfamv/image/upload/v1700343842/homepage2_eqmd2d.png)

    ### Home Page Image 3

    ![Home Page Image 3](https://res.cloudinary.com/dbagkfamv/image/upload/v1700343841/homepage3_ql4apm.png)

    - This is the sign up for to the MailChimp Newsletter for our website. 
    - Below this is a link to our Facebook Business Page
    - ![Facebook Business Page](https://res.cloudinary.com/dbagkfamv/image/upload/v1700340288/facebook_business_page_idefss.png) - I have left the link on the website to Facebook.com to prevent access to the business page, due to this being a project and not a live business. 

    ### The Navigation bar

    ### Navigation Bar for Registered Users

    - The navigation bar on the website is different for different users on the website. The navigation bar for registered users shows the following:
        - Home - links to Home Page
        - View Packages - links to view a list of all the hiking packages offered and available to purchase. Users can select a package and go to a package detail section which displays more information on the package and allows the user to add to cart ready for purchasing. 
        - About Us - links to an About Us page which details about Highland Adventures
        - Gallery - links to a gallery page where users can view images from our packages
        - Reviews - links to Reviews of all the packages on the website. Users can read through current reviews on any package they desire and also add a review to any package they desire. 
        - Cart - links to the cart page, where users can view their cart and what packages they have in their cart for purchase. They can change the quantity, remove the package, or proceed to the checkout. 
        - User Reviews - links to a page when the user can view their own reviews they have made on the website. This lists all their reviews on all packages. The user can view, edit their review or delete it if they wish. 
        - Logout - links to a logout page where the user can logout. 
        - User Profile Details - this has a dropdown menu with 3 options
            - User Profile - links to a page where the user can view their User Profile and Personal Information. Also this displays to the user their discount code. 
            - Edit User Profile - links to a page where the user can edit their user profile
            - Edit Personal Details - links to a page where the user can edit their personal information. 

    ![Navigation Bar for Registered Users](https://res.cloudinary.com/dbagkfamv/image/upload/v1700343517/nav_bar_registereduser_hhcvey.png)

    ###  Navigation Bar for Non Registered/Logged In Users

    - The navigation bar for registered users shows the following:
        - Home - links to Home Page
        - View Packages - links to view a list of all the hiking packages offered and available to purchase. Users can select a package and go to a package detail section which displays more information on the package and allows the user to add to cart ready for purchasing. 
        - About Us - links to an About Us page which details about Highland Adventures
        - Gallery - links to a gallery page where users can view images from our packages
        - Reviews - links to Reviews of all the packages on the website. Users can read through current reviews on any package they desire and also add a review to any package they desire. 
        - Login - links to a login page where the user can login. 
        - Register - links to a page where the user can register to become a registered user. 

    ![Navigation Bar for non Registered Users](https://res.cloudinary.com/dbagkfamv/image/upload/v1700343635/nav_bar_nonuser_nk7vt2.png)

    ###  Navigation Bar for Staff

    - The navigation bar for registered Staff users shows the following:
        - Home - links to Home Page
        - View Packages - links to view a list of all the hiking packages offered and available to purchase. Users can select a package and go to a package detail section which displays more information on the package and allows the user to add to cart ready for purchasing. 
        - About Us - links to an About Us page which details about Highland Adventures
        - Gallery - links to a gallery page where users can view images from our packages
        - Reviews - links to Reviews of all the packages on the website. Users can read through current reviews on any package they desire and also add a review to any package they desire. 
        - Cart - links to the cart page, where users can view their cart and what packages they have in their cart for purchase. They can change the quantity, remove the package, or proceed to the checkout. 
        - User Reviews - links to a page when the user can view their own reviews they have made on the website. This lists all their reviews on all packages. The user can view, edit their review or delete it if they wish. 
        - Logout - links to a logout page where the user can logout. 
        - User Profile Details - this has a dropdown menu with 3 options
            - User Profile - links to a page where the user can view their User Profile and Personal Information. Also this displays to the user their discount code. 
            - Edit User Profile - links to a page where the user can edit their user profile
            - Edit Personal Details - links to a page where the user can edit their personal information. 
        - Admin Login - links to the /admin page where the staff member can login to the admin page for the website. 

    ![Staff Navigation Bar](https://res.cloudinary.com/dbagkfamv/image/upload/v1700347435/staff_nav_qy9k7b.png)

    ### Footer 

    - The footer is displayed on every page on the website to allow users to navigate to the social links for Highland Adventures. 
        - Facebook - This would link to the Highland Adventure business page. I have linked this to facebook.com, as this is a project and not a live business. 
        - Twitter - This would link to the Highland Adventure Twitter page. I have linked this to twitter.com - as this is a project and not a live business. 
        - Instagram - This would link to the Highland Adventure Instagram page. I have linked this to Instagram.com - as this is a project and not a live business. 

    ![Footer](https://res.cloudinary.com/dbagkfamv/image/upload/v1700343840/footer_qxrhkn.png)

    ###  View Packages 

    - View Packages displays all the packages available for the user to purchase.
    - Each package displays:
        - An image from the walking package to draw the user in. When the user hovers over the image, the image enlargens to draw the user in. 
        - A description of the package 
        - A difficuly rating for the package
        - The price of the package (before any discount is applied)


    ![Package List](https://res.cloudinary.com/dbagkfamv/image/upload/v1700344145/packages_list_di1tvj.png)

    ###  Package Detail

    - The package detail displays to the user everything they need to know about the package. 
        - It displays the title of the package.
        - It displays a large image of the package. 
        - It displays the description of the package to the user. 
        - It displays the difficulty rating of the package. 
        - It displays the price of the package. 
        - It displays a Add to Cart button - which if the user clicks, will add the package to the cart. When a user clicks on this button, it adds the package to the cart and redirects them to the cart page to view their cart. 
        - It displays a selection of Customer Reviews for the package. The user can read through the reviews from fellow users to see what their experience of the package was. It provides the user with a fantastic user experience. The user can click on the username of the user who wrote the review, to view their User Profile, where they can see the user bio, profile picture and all the reviews they have added to the website. 

    ![Package Detail](https://res.cloudinary.com/dbagkfamv/image/upload/v1700344175/package_detail_trlzul.png)
    ![]()

    ###  About Us

    - The About Us displays to the user everything about Highland Adventures. It explains who Highlands Adventures are, how the hiking packages work and what type of walk should I do. It provides a good level of detail to the user about the packages. 

    ![About Us](https://res.cloudinary.com/dbagkfamv/image/upload/v1700344495/aboutus_yz5cyg.png)

    ###  Gallery

    - The Gallery displays a selection of images from the packages to the user to view. It offers a good user experience as they can view the images and this may encourage them to purchase a package to see the mountains with their own eyes!

    ![Gallery](https://res.cloudinary.com/dbagkfamv/image/upload/v1700345141/gallery_p3hgqw.png)

    ###  Reviews

    - The Reviews page displays all of the packages to the user, but the user can select to view the reviews for each package by clicking on the View Review button. This will take the user to a page which displays all the user reviews on that specific package. 
    - There is also a Add a Review button. This is only visible to registered users and allows the user to add a review for a specific package. The user can select the following:
        - Difficult Rating - how difficult they found the walking package
        - Overall Rating - the overall rating for the walking package
        - Review - a textbox which allows the user to type in their review of the package and add their own detail. 
        - Submit Button - the user clicks to submit their review. 
    ![Reviews](https://res.cloudinary.com/dbagkfamv/image/upload/v1700345374/customer_reviews_o1b56a.png)
    ![Reviews of a Package](https://res.cloudinary.com/dbagkfamv/image/upload/v1700352700/Reviews_for__package_j9mfxz.png)
    ![Add a Review](https://res.cloudinary.com/dbagkfamv/image/upload/v1700352796/add_review_sknbk0.png)

    ###  Cart

    - Cart displays to the user their cart. It display the following to the user:
        - A list of the items in the cart
            - Package Title
            - Quantity - this can be adjust by the user inputting a number and clicking on Update Quantity button.
            - Update Quantity button - saves any changes the user makes to the quantity. 
            - Remove button - the user can click this button and it will remove the package from the cart. 
            - Total Price - this displays the total price of all the packages in the cart. 
            - Displays a list of the packages and quantities of each. 
            - Proceed to Checkout Button - the user can click on this button and it will take the item(s) in the cart and take the user to the checkout page where they can process the order. 

        - If the user has not added any packages to the cart and clicks on the cart button in the navigation bar, they will find the cart to be empty and this is displayed to the user. 

        ![Empty Cart](https://res.cloudinary.com/dbagkfamv/image/upload/v1700353459/empty_cart_qhvoiy.png)


    ![Cart](https://res.cloudinary.com/dbagkfamv/image/upload/v1700346630/cart_cjchov.png)

    ### Checkout 

    - The checkout allows the user to process the payment of the items from the cart. The checkout contains a form with the following:
        - Address Line 1
        - Address Line 2
        - County
        - Country
        - Order Summary - Display the items the user is purchasing and quantity. 
        - Discount Code - where the user can input a discount code to apply discount (This has now been hidden from the user, due to an error processing discounted payments, please see known bugs)
        - Apply Discount button - this processes the discount on the total price (This has now been hidden from the user, due to an error processing discounted payment, please see known bugs)
        - Card detail field - this is a stripe field where the user inputs their card details.
        - Submit button - this processes the purchase through to stripe. If the form is valid, the order will be submiited. The user will be redirected to order confirmation page. 

        - Please see the image below of the checkout page prior to the hiding of the discount code function. 

     ![Checkout](https://res.cloudinary.com/dbagkfamv/image/upload/v1700357773/all_fields__needed_e7epm7.png)

     - Please see the image below of the checkout page, which now hides the discount code function. 

     ![Live Checkout Page](https://res.cloudinary.com/dbagkfamv/image/upload/v1700387068/Updated_checkout_view_wzsriy.png)

     ### Order Confirmation

     - This is the order confirmation and displays to the user the following:
        - Order Details
            - User 
            - Total Price
            - Items Ordered
        - Shipping Information 
            - Address Line 1
            - Address Line 2
            - County
            - Country
            - Phone Number
        
        - This provides the user with confirmation that the order has been processed and payment has been taken. 

     ![Order Confirmed](https://res.cloudinary.com/dbagkfamv/image/upload/v1700358553/checkout_success_lzx5df.png)

    - 

    ###  User Reviews

    - User Reviews displays for the user all of the reviews they have personally added to the website. If they haven't submitted any reviews this will show as empty. It displays the following: 
        - The package title of the review
        - The date and time the review was created
        - The review text
        - Edit and Delete Buttons - the user can click on the edit button to navigate to a page to edit the review. If the user clicks on the delete review, it will navigate the user to a page where they can delete their review. 
    ![User Reviews](https://res.cloudinary.com/dbagkfamv/image/upload/v1700346523/user_reviews_wlcamf.png)
    ![Edit Review](https://res.cloudinary.com/dbagkfamv/image/upload/v1700353664/Edit_Review_dei62z.png)
    ![Delete Review](https://res.cloudinary.com/dbagkfamv/image/upload/v1700353645/delete_review_inmjkk.png)

    ###  Login/Logout - Set Up using AllAuth

    - This allows the user to login/logout of the website if they are not logged in or logged out. 
    - Login
    - ![Login](https://res.cloudinary.com/dbagkfamv/image/upload/v1700345098/login_fposb8.png)
    - Logout
    - ![Logout](https://res.cloudinary.com/dbagkfamv/image/upload/v1700346454/logout_rlke4p.png)
       

    ###  Register - Set Up using AllAuth

    - This allows the user to register and sign up to become a registered user on the website.The user has to enter the following:
    - Email Address
    - Email Address again
    - Username 
    - Password
    - Password again

    - Once this information is entered, the user will be sent an email asking them to verify their email address and once that is complete, they will be registered on the site and their details added to the database. 
    ![Register](https://res.cloudinary.com/dbagkfamv/image/upload/v1700346576/register_mllzsa.png)

    ###  User Profile Details
    - User Profile

    - User Profile - links to a page where the user can view their User Profile and Personal Information. This also displays to the user a discount code. 

    ![User Profile](https://res.cloudinary.com/dbagkfamv/image/upload/v1700346710/user_profile_ivrlgi.png)
    - Edit User Profile

    - Edit User Profile - links to a page where the user can edit their user profile

    ![Edit User Profile](https://res.cloudinary.com/dbagkfamv/image/upload/v1700346750/edit_user_profile_jvoc9h.png)
    - Edit Personal Details

    - Edit Personal Details - links to a page where the user can edit their personal information. 
    - ![Edit Personal Details](https://res.cloudinary.com/dbagkfamv/image/upload/v1700346750/edit_user_profile_jvoc9h.png)


    ## Admin Features

    ###  Navigation Bar for Staff

    - The navigation bar for registered Staff users shows the following:
        - Home - links to Home Page
        - View Packages - links to view a list of all the hiking packages offered and available to purchase. Users can select a package and go to a package detail section which displays more information on the package and allows the user to add to cart ready for purchasing. 
        - About Us - links to an About Us page which details about Highland Adventures
        - Gallery - links to a gallery page where users can view images from our packages
        - Reviews - links to Reviews of all the packages on the website. Users can read through current reviews on any package they desire and also add a review to any package they desire. 
        - Cart - links to the cart page, where users can view their cart and what packages they have in their cart for purchase. They can change the quantity, remove the package, or proceed to the checkout. 
        - User Reviews - links to a page when the user can view their own reviews they have made on the website. This lists all their reviews on all packages. The user can view, edit their review or delete it if they wish. 
        - Logout - links to a logout page where the user can logout. 
        - User Profile Details - this has a dropdown menu with 3 options
            - User Profile - links to a page where the user can view their User Profile and Personal Information. Also this displays to the user their discount code. 
            - Edit User Profile - links to a page where the user can edit their user profile
            - Edit Personal Details - links to a page where the user can edit their personal information. 
        - Admin Login - links to the /admin page where the staff member can login to the admin page for the website. 

    ![Staff Navigation Bar](https://res.cloudinary.com/dbagkfamv/image/upload/v1700347435/staff_nav_qy9k7b.png)

    ###  Admin Sign In

    - This is where staff will sign in to the access the Django Admin section of the website, where they can access the database for the website. 
    ![Admin Sign In](https://res.cloudinary.com/dbagkfamv/image/upload/v1700345691/admin_signin_vfydef.png)

    ###  Admin View

    - This is where the admin staff can access all the site admin for the website. It has the following items:

    - Email addresses
    - Groups
    - Discount codes
    - Order items
    - Orders
    - Payments
    - Packages
    - Reviews
    - Sites
    - Social accounts
    - social application tokens
    - social applications
    - User profiles
    - Users 

    - The admin can enter any of these sections and create, read, edit and delete any item in any of these sections. 

    ![Admin View](https://res.cloudinary.com/dbagkfamv/image/upload/v1700345694/admin_view_xcxmfy.png)

    ###  Admin Discount View

    - This is where admin staff can create, read, edit and delete any discount codes for the website. It has a two fields:
    - Code - the admin can set the discount code. Currently the discount code for all registered user is HA10, which is showed on the checkout page and User Profile page to registered users. 
    - Discount percentage - the admin can set the percentage of the discount. 

    ![Admin Discount View](https://res.cloudinary.com/dbagkfamv/image/upload/v1700345693/discount_admin_s70wk8.png)

    #### Detailed View

    ![Admin Discount View Discount](https://res.cloudinary.com/dbagkfamv/image/upload/v1700354543/discount_detail_qw3l3g.png)

    ###  Admin Order Items

    - The admin staff can see what items have been ordered on each order. It contains: 
        - Order - who the order belongs to
        - Package - which package was ordered by the user
        - Quantity - what quantity of the package was ordered. 


    ![Admin Order Items](https://res.cloudinary.com/dbagkfamv/image/upload/v1700345690/order_items_admin_cblvmd.png)

    #### Detailed View
    ![Detailed View Order Item](https://res.cloudinary.com/dbagkfamv/image/upload/v1700347890/detail_order_item_udxf0y.png)

    ###  Admin Orders

    - The admin staff can see what the order was for each user. It contains:
        - User - which user placed the order
        - Total Price - the total price of the order
        - Address Line 1 - User first line of address
        - Address Line 2 - User second line of address
        - County - User County
        - Country - User Country - this is set using CountryField, so the user can select from all the countries. 
        - Phone Number - User phone number
    ![Admin Orders](https://res.cloudinary.com/dbagkfamv/image/upload/v1700345688/orders_admin_iqafey.png)

    #### Detailed View
    ![Detailed View Order ](https://res.cloudinary.com/dbagkfamv/image/upload/v1700347953/detail_order_runngi.png)

    ###  Admin Payments

    - The admin staff can see the payments for all orders that have been processed. It contains:
        - Order - who the order is for. 
        - Amount - how much the order is for. 
    ![Admin Payments](https://res.cloudinary.com/dbagkfamv/image/upload/v1700345686/payment_admin_colzin.png)

    ####  Detailed View
    ![Detailed View Payment ](https://res.cloudinary.com/dbagkfamv/image/upload/v1700348031/detail_payment_ed4xgl.png)

    ###  Admin Packages

    - The admin staff can create, edit, view and delete all the packages that are on the website. It contains a list of all the packages and if the admin click on a package they can see the following:
        - Title - the title of the package
        - Description - Package Description
        - Price - The price of the package
        - Image - The image for the package
        - Difficulty Rating - the setting of difficult for the package, the options are:
            - Easy
            - Moderate
            - Difficult
            - Challenging

    ![Admin Packages](https://res.cloudinary.com/dbagkfamv/image/upload/v1700345696/packages_admin_at0g2f.png)

    ####  Detailed View
    ![Detailed View Packages ](https://res.cloudinary.com/dbagkfamv/image/upload/v1700348122/detail_package_dkkeyg.png)

    ###  Admin Reviews

    - The admin staff can view, edit, create and delete the reviews for all the packages on the website here. If the admin staff click on one of the reviews, they can see the following: 
        - User - which user created the review
        - Package - which package the review is for
        - Text - what text is entered in the textbox for the review
        - Difficulty Rating - what difficulty rating was set by the user
        - Overall Rating - what overall rating was set by the user. 
    ![Admin Reviews](https://res.cloudinary.com/dbagkfamv/image/upload/v1700345685/review_admin_gcwdrm.png)

    ####  Detailed View
    ![Detailed View Review ](https://res.cloudinary.com/dbagkfamv/image/upload/v1700348179/detail_review_nzssmi.png)

    ###  Admin User Profiles

    - The admin staff can view, edit, create and delete the user profiles for all the users on the website. If they click on one of the user profiles they can see the following: 

        - User - which user profile this is. 
        - Bio - the text the user entered for their bio. 
        - Profile Picture - the profile picture the user submited for their profile picture. 
    ![Admin User Profiles](https://res.cloudinary.com/dbagkfamv/image/upload/v1700345683/user_profile_admin_drdfcz.png)

    ####  Detailed View
    ![Detailed View User Profile ](https://res.cloudinary.com/dbagkfamv/image/upload/v1700348228/detail_userprofile_jsnyu5.png)

    ###  Admin Users

    - The admin staff can view, edit, create and delete the users on the website here. This displays the username, first and last name, email, phone number, staff status and superuser status.
    
    ![Admin Users](https://res.cloudinary.com/dbagkfamv/image/upload/v1700345682/users_admin_jmzbu9.png)

    ####  Detailed View

    - If they click on one of the users they can see the following: 
    ![Detailed View User](https://res.cloudinary.com/dbagkfamv/image/upload/v1700348296/detail_user_n3azrs.png)




### Future Implementations

- Please find below a detailed list of future implementations for the website. 

- Discount code functionality
    - As detailed in the bugs section below, sadly the discount code functionality is not operating in full. The discount codes work, when a user enters the discount code and applies it at the checkout. However, Stripe will take the full total price and not the discounted price, but the website will process and display to the user that the discount price has been paid. This would lead to an extremely poor user experience and would need to be fixed or addressed prior the website going live. The discount code function has now been hidden and a message displayed informing the user of this (please see known bugs for further information)
- Users only being able to submit reviews on packages they have an order history of purchasing
    - At the momemnt a user can submit a review on any package, whether they have purchased it or not. I would like to set up where the user can only submit a review on packages they have purchased. The reasoning behind this is to enchance the user experience, as the user will only be reading reviews from users who have purchased the packages. 
- Admin approving reviews before they are visible on the reviews. 
    - Currently users can submit their review and this will go live on the site. It would be good to set up, where the review has to go through to admin staff first, where the review can be approved by staff, before it is live on the site. 
- Cart in Nav Bar showing item numbers
    - It would be good when a user adds an item to the cart, it displays the total quantity in the nav bar next to the cart. It would allow the user to see on any page on the website, how many items are in their cart, without having to go to the cart. 
- Email the user when they register and delivering them unique discount codes.
    - This would enhance the user experience and allow the discount codes to change. Also, it would be good if discount codes had expiry dates or limited uses, to encourage sales and also prevent too many discounts. 
- Webhooks and adapting the database
    - The website currently does not have webhooks set up. When an order is processed to Stripe, the payment goes through and the database is updated via the website code. For a more detailed and synced database to Stripe, the use of webhooks would be a huge benefit. Also for user experience, for admin and users, as it is easier to see all the information about orders in the database and not having to compare to Stripe. 

- Information email to User when they register or complete a purchase.
    - When the user registers as a user, it would be good User experience, if they receieved a personal email welcoming them to the site. 
    - When the user completes an order, it would be good User experience, if they receieved an email with their order confirmation. 
- Orders having Order Numbers for the user and admin
    - This would allow orders to be found at ease for admin and also give the user a unique order number if they need to enquire about their order. 
- Register an user account using social media
    - User being able to create an account via social media, e.g. facebook, twitter etc. This would be good user experience, as users can create accounts very quickly and also offered marketing oppportunities for Highlands Adventures. 
- Payment via ApplePay, Pay Pal etc
    - Currently payment is card only. It would be good to offer more methods of payment to the user to improve user experience. 
- Validation on checkout form 
    - Currently there is no validation on the checkout form, apart from that field needs to be filed. This is bad user experience and validation needs to be added to ensure valid data is entered in the form. 

## Technologies Used

- Included a robots.txt and sitemap.xml (www.xml-sitemaps.com). 

### Languages Used

HTML, CSS, Javascript, Python and Django

### Frameworks

Django - A high-level Python web framework that encourages rapid development and clean, pragmatic design.

Google sheets and Google Docs - To draw up user stories and writing up content for html pages.

Codeanywhere - For version control

Github - To save and store the files for the website

Bootstrap - The framework for the website.

Google Dev Tools - To troubleshoot and test features, solve issues with responsiveness and styling.


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

www.xml-sitemaps.com to create sitemap.xml

Font Awesome

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


#### **Preparation for deployment in Codeanywhere**

### Local Development

#### How to Fork

To fork the repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, RichBurman/highlands_project5
3. Click the Fork button in the top right corner.

#### How to Clone

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, RichBurman/higlands_project5
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.



## Testing

- Testing was ongoing throughout the entire build. I utilised Chrome developer tools while building to pinpoint and troubleshoot any issues as I went along.

### Full Testing

- To fully test the website I performed the following tests using a number of different browsers, as well as testing on a MacBook Pro 16" and a iPhone 13 Pro Max.

- I also went through each page using google chrome developer tools to ensure that they responsive on all different screen sizes.

### Packages and Cart

 - All packages can be added to the cart for the package detail page.  
 - In the Cart
    - package quantities can be updated using the update quantity button
    - packages can be removed using the remove button
    - The user can proceed to the checkout and all items from the cart will be transfereed succesfully to the checkout. 

### Checkout

- All fields allow input
- Once all fields are completed, the order can be submited to Stripe. 

- The discode code field accepts the discount code and when Apply Discount button clicked, it subtracts the discount. 

![Discount Code entered](https://res.cloudinary.com/dbagkfamv/image/upload/v1700358305/eneter_discount_code_pmybev.png)
![Discount worked](https://res.cloudinary.com/dbagkfamv/image/upload/v1700358321/discount_success_funpui.png)
![Discount Message](https://res.cloudinary.com/dbagkfamv/image/upload/v1700358294/discount_message_mxlb7k.png)

 - The checkout form has validation to make sure all the boxes are filled in, before the form is submited. The form needs validation on what is inputted in each box, as currently there is no validation on what can be entered into the fields. 
 ![](https://res.cloudinary.com/dbagkfamv/image/upload/v1700357709/form_complete_iqesnm.png)
- All fields on the checkout need to be complete before the order can be submitted. 
 ![All Fields needed](https://res.cloudinary.com/dbagkfamv/image/upload/v1700357773/all_fields__needed_e7epm7.png)

 - The Discount code section has now been hidden from the checkout.html page now as this is detailed in the known bugs section below. 

 ## Problem with Discount Code

 - When the order is processed to Stripe, full payment is taken, not the discounted price. 
 
 - The order confirmation shows the total price was £135.00
 ![Discounted Price](https://res.cloudinary.com/dbagkfamv/image/upload/v1700358553/checkout_success_lzx5df.png)
- But the Stripe payment was £150.00. Stripe is not taking the discounted price. 
 ![Full Pay Stripe](https://res.cloudinary.com/dbagkfamv/image/upload/v1700358547/stripe_payment_ufaxti.png)

 - - The Discount code section has now been hidden from the checkout.html page now as this is detailed in the known bugs section below. 
 ### Messages 
 - All messages throughout the website work as expected.
 ### Database

 - Database Updated when ordered is processed. 

 - All orders that are processed are updated to the database. This has been checked for orders on every package type with various quantities and using different user types. 

 ### Users

 - New users can be registered. 
 - Admin can add new users, staff users and superuser is the admin. 

 ### User Profile and User Personal Information

 - All user profile and user personal information can be edited and works as expected. 

 ### User Reviews

 - All user reviews worked as expected, can be viewed by user or admin. User reviews can be edited/deleted by the user who created them and also by Admin. 

### Admin

- All Admin work in the Admin section and can only be accessed by staff. Working as expected. 

### Links

- All navigation links on the entire website work as expected, opening in the same window. The footer links work as expected, but open in a seperate window. 

### W3C Validator

All html pages passed W3C testing. (Apart from Parse Errors)
All css pages passed W3C testing. 

### Solved Bugs

- I had a serious bug when the checkout form would not submit through to Stripe. The issue was, I had deleted card details from the checkout.html which was previously on the checkout.html, but I had not removed these details from the checkout form in forms.py in the checkout app. The form was constantly showing as invalid, because it was still requiring those payment details to complete the validation of the form. This took over two days to work out and fix. 

### Known Bugs

#### Discount Code Bug

 - When the order is processed to Stripe, full payment is taken, not the discount price. 
 
 - The order confirmation shows the total price was £135.00
 ![Discounted Price](https://res.cloudinary.com/dbagkfamv/image/upload/v1700358553/checkout_success_lzx5df.png)
- But the Stripe payment was £150.00. Stripe is not taking the discounted price. 
 ![Full Pay Stripe](https://res.cloudinary.com/dbagkfamv/image/upload/v1700358547/stripe_payment_ufaxti.png)

 - I have tried to change the structure of the process_checkout view, but I have been unable to solve this bug. 

 - In the meantime, I have hidden the discount code section on the checkout.html, to prevent the user from inputting discount codes, to enhance the user experience. So if they process an order it will be at the full price and no discount will be applied. Please see the image below, how the checkout page now looks. 

 ![Discount Input Removed Checkout.html](https://res.cloudinary.com/dbagkfamv/image/upload/v1700386530/remove_discount_code_ys44hj.png)

 - I have added a message to the checkout page to display to the user that the discount code is currently not functioning. 

 ![New Checkout View](https://res.cloudinary.com/dbagkfamv/image/upload/v1700387068/Updated_checkout_view_wzsriy.png)

 #### user_payment app

 - When I was having trouble trying to get Stripe payments to work, as explained in my solved bugs, I tried to use Stripe Checkout. I created a new app which is user_payment, which is still included in the code. If I delete this app and trying to remove all the links to it, it would prevent the website loading and give various different errors. I had to go back to previous commit messages to have the user_payment app back and then the website/project would load. I want to remove the app as it isn't used, to my knowledge on the page. 

 #### Database 

 The database is not linked to Stripe using webhooks, which means the database is not as accurate as it could and should be. Due to the discount code bug, I run out of time to adapt the database structure and set up webhooks. 



### Lighthouse

- The lighthouse scores show the following:

![Lighthouse](https://res.cloudinary.com/dbagkfamv/image/upload/v1700360138/lighthouse1_qigzqp.png)

- Image Size is affecting the performance. However, the quantity of the images add to the user experience. 
![Lighthouse 2](https://res.cloudinary.com/dbagkfamv/image/upload/v1700360132/lighthouse2_tv6ytq.png)

## Credits

[Kera Cudmore README Template and Deployment Code](https://github.com/kera-cudmore/Bully-Book-Club/blob/main/README.md)


### Code Used

Code was used for the base.html from the [Boutique_ado](https://github.com/Code-Institute-Org/boutique_ado_v1) walkthrough. 

### Content

Content for the website was written by Richard Burman
Research using [w3c](https://www.w3schools.com/), [bootstrap](https://getbootstrap.com/), [Stripe](https://stripe.com/gb)

### Media

- Some images were taken from Unsplash
- All other images are owned by Richard Burman. 
- All images were compressed using Optimizilla to aid website performance.
- Screenshots taken from the following website for this README
- Lighthouse
- Jigsaw validator
- W3C validator
- Am I Responsive?

### Acknowledgments

- I would like to thank the following:
    - A huge thank you to my family for your huge support and understanding throughout the project! Thank you
    - A big thanks to my mentor! You have been fantastic thank you
    - Thank you to Student support, who helped with issues with Stripe not taking payments. 
    - Thank you to fellow students in Slack for your support and help at times. 