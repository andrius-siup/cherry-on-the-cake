# X Cherry

## Project Summary

This is an X Cherry eCommerce website, for the users will find the products associated with the boxing sport. There is also a Blog section, where the admin has grand to add posts associated with healthy living and combat sports. The registered users have access to view the single post and add comments. I hope this website will create a boxing sports community, where the advanced boxers can share tips with beginners. The admin also has access to add, edit or delete products from the store, remove users' comments, and lots more. The website has a responsive design, from small phone devices to large screens. The website was created for educational purposes.

## Contents

- [User Experency (UX)](#ux)
  - [Ideal user](#ideal-user)
  - [User Stories registered](#user-stories-registered)
  - [User stories admin](#user-stories-admin)
  - [User stories not registered user](#user-stories-not-registered-user )
- [Goals](#goals)
  - [Visitors Goals](#visitors-goals)
  - [User Goals](#user-goals)
  - [Business Goals](#business-goals)
  - [X Cherry Goal](#x-cherry-goal)
- [Strategy](#strategy)
- [Scope](#scope)
- [Structure](#structure)
- [Skeleton](#skeleton)
  - [Wireframe](#wireframe)
- [Features](#features)
  - [Navigation Bar](#navigation-bar)
  - [Home app features](#home-app-features)
  - [Products app features](#products-app-features)
  - [Blog app features](#blog-app-features)
  - [Profiles app features](#profiles-app-features)
  - [Bag app features](#bag-app-features)
  - [Checkout app features](#checkout-app-features)
  - [Footer](#footer)
  - [Future Features ideas](#future-features-ideas)
- [Responsive](#responsive)
- [Deployment](#deployment)
  - [Requirements](#requirements)
  - [Download](#download)
  - [Clone Repository](#clone-repository)
  - [Creating an Environment File](#creating-an-environment-file)
  - [Deployment to Heroku](#deployment-to-heroku)
- [Testing](#testing)  
  - [Code validators](#code-validators)
  - [Lighthouse](#lighthouse)
  - [Manual Testing](#manual-testing)
- [Technologies Used](#technologies-used)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Code](#code)
  - [Resources](#resources)
  - [Acknowledgements](#acknowledgements)

## (ux)

## Ideal user

The ideal user is English reading and writing shopper, who loves boxing sport. The user who wants to purchase the boxing gear, or clothes, read the blog posts, and be active in comments.

## User Stories registered

- As a user, I expect that the site logo always brings me to the home page.
- As a user, I expect to be able to sign up to this website and get the email confirmation.
- As a user, I want to be able to sign up to this site and get all user access, buy products, read the blog posts, write comments.
- As a user, I expect to be able to save my sign-in details for future access to this site.
- As a user, I expect to be able to restore my forgotten password.
- As a user, I want to easily navigate through all the pages.
- As a user, I expect to be able to the shopping bag icon with the amount into the navigation bar, to easily manage my spending.
- As a user, I want to get success, info, and errors messages for my daily uses.
- As a user, I want to know if there is a free delivery from this site.
- As a user, on the Products page, I want to find products by category, subcategories.
- As a user, on the Products page, I want to sort products by price, rating, name, and category.
- As a user, on the Products page I want to be able to access to the product detail page, to see product description, choose size and quantity, also see the rating and category a clickable.
- As a user, on the Products page, I want to see the Back to Top button if there is a lot of products.

- As a user, on the Product Detail page, I want to be able to see the product image in the bigger view.
- As a user, on the Product Detail page, I want to see the ADD TO BAG button in the product details page, to add a product in the shopping bag.
- As a user, on the Product Detail page, I want to see the message success when I added the product into the shopping bag.
- As a user, on the Product Detail page I expect to be able to see success messages with all details of the product like name, how many items are in the bag, items image, total, info line with getting free delivery, and button go to checkout.

- As a user, in the Shopping bag page, I expect to be able to do changes like add more and remove the number of products, also see updates of bag total, delivery cost, and grand total.
- As a user, on the Shopping bag page I expect to be able to see the cost of the products: like bag total, delivery cost, and grand total. Also, the info text with calculations to get free delivery.
- As a user, on the Shopping bag page, I expect to be able to see buttons like: back to the Products page and go to Secure Checkout page.

- As a user on the checkout page I want to see the form to complete my order, like my own details, delivery information, and payment card field.
- As a user on the checkout page I expect to be able to see the Order summary with all totals.
- As a user on the checkout page I expect to be able to save my own delivery information for future shoppings.
- As a user on the checkout page, I expect to want to be able to back into the shopping bag to do some change.

- As a user, on the Checkout Success page, I want to see the order information with all details.
- As a user, on the Checkout Success page, I want to see the success message with the order number and email confirmation.
- As a user, on the Checkout Success page, I expect to want to be able back to the products page.

- As a user of the website I would like to has access to the site Blog, to read the useful posts.
- As a user on the Blog page I want to see the latest post at, top of the Blog.
- As a user on the Blog page, I want to see all posts with a short text, to read a little bit, and if is interest go to the post detail page.
- As a user on the Blog page I want to see the search bar to quick and easy find the post.
- As a user on the Blog page, I want to sort the posts by name, category, date.
- As a user on the Blog page I want to find the posts by category label below the post text. That is to see all posts in this category.
- As a user on the Blog page I want to see the Back to Top button, for quick back to the top of the page.
- As a user on the Blog page I expect to -e able to see the post detail page.

- As a user, on the Blog post detail page, I want to see the full post and Back to Blog button.
- As a user, on the Blog post detail page, I want to add a comment below the post, or ask interesting questions-
- As a user, in the Blog post detail page, I want to see others registered users' comments.
- As a user in the Blog post detail page, I want to see the latest comment at top of the all comments.
- As a user, in the Blog post detail page, I want to see the Back to Top button, to quickly back to the top of the page.

- As a user I want to be able to access the My Profile page with delivery information, also can be an editable form if something changes with my address.
- As a user, I expect to be able to see my order history on my profile page.

## User stories admin

- As an admin of the website, I want to have access to the add, edit or delete products and blog posts also access to delete user's comments.
- As an admin of the website, in the My Account icon, I want to see the Product Management link, which will be redirected to Add product page.
- As an admin of the website, on the Add Product page, I would like to see a user-friendly input form, that I can manually add new products.
- As an admin of the website, in the Add Product page form, I want to see the form fields:
  - Category
  - SKU
  - Name
  - Description
  - Have sizes
  - Price
  - Rating
  - Image URL
  - Add local image
    - buttons:
      - Add Product - save the new data and redirect to the Product Detail page. To look at how everything looks from the user's side.
      - Cancel - data not saved and simple back into the Products page.

- As an admin of the website, in the Products page and Product detail page, I want to see the edit and delete product links.
- As an admin of the website, on the Edit Product page, I want to see the form with the all details of the product that I want to edit.
- As an admin of the website, on the Edit Product page, I want to simply remove old information and add new text or replace the image.
- As an admin of the website, on the Edit Product page, I want to see two buttons:
  - Update - save new information and redirected to the Product Detail page, to see how looks from the customer side.
  - Cancel - leave the old data(same data) and redirected to the Products page.
- As an admin of the website, in the Products page and Product Detail page, I want to see the Delete link, for a simple removed product with all data from the site.

- As an admin of the website, on the Blog page, near the search bar button, I want to has the Add Post button, to add new posts.
- As an admin of the website, on the Add Post page, I want to see a simple input form with fields:
  - Choose Category
  - Post Titl-
  - Input text
  - Created by
  - Two buttons:
    - Add Post - Save all information and redirected to the Post Detail page.
    - Cancel - simply redirected to the Blog page.

- As an admin of the website, in the Blog page and in the Post Detail page, I want to see the edit and delete links:
  - Edit link - which will be redirected into the Edit Post page, with all post details saved into form.
    - In the Edit Post form I want to simply edit text or change the category.
    - Also I want to see two buttons:
      - Update - save the new data and redirected to the Post detail page.
      - Cancel - leave the old data(same data) and redirected to the Blog page.
    - Delete link - simple removed post with all data from the site.
- As an admin of the website, in the Post Detail page, in the single comment, I want to see the delete link, which simply removed the comment from the site.

## User stories not registered user

- As a non-register user, I expect that the site logo always brings me to the home page.
- As a non-register user, I expect to be able to Sign Up for this website.
- As a non-register user, I want to easily navigate through all the pages.
- As a non-register user, I want to know if there is a free delivery from this site.
- As a non-register user, on the Products page, I want to find products by category, subcategories.
- As a non-register user, on the Products page, I want to sort products by price, rating, name, and category.
- As a non-register user, on the Products page, I want to see the Back to Top button if there is a lot of products.
- As a non-register user, on the Products page, I want to be able to access the Product Detail page, to see full product information product.

- As a non-register user, on the Product Detail page I want to be able to see the product full information:
  - Product Name
  - Price
  - Category (link to this category)
  - Description
  - Rating
  - Choose Size (if has size - xs, s, m, l, xl)
  - Quantity (buy more than one - 1-99)
  - Buttons :
    - Back to Products - simple redirecting the non-register user into the Products page.
    - Add to Bag - add the product into the shopping bag, display the item price into the bag icon(into the navigation bar).
- As a non-register user, on the Product Detail page, I want to see the message success when I added the product into the shopping bag.
- As a non-register user, on the Product Detail page I expect to be able to see success messages with all details of the product like name, how many items are in the bag, items image, total, info line with getting free delivery, and button go to checkout.

- As a non-register user, on the Shopping bag page, I expect to be able to do changes like add more and remove the number of products.
- As a non-register user, on the Shopping bag page I expect to be able to see the cost of the products: like bag total, delivery cost, and grand total. Also, the info text with calculations to get free delivery.
- As a non-register user, on the Shopping bag page I expect to be able to see buttons like:
  - Back to Products - redirecting non-register user into the Products page.
  - Secure Checkout - redirecting the non-register user to the Sign In page. The non-register user can't buy items without sign in to the website.

- As a non-register user, I would like to has access to the site Blog, to read the useful posts.
- As a non-register user, on the Blog page, I want to see the latest post at, top of the Blog.
- As a non-register user, on the Blog page, I want to see all posts with a short text, to read a little bit, and if is interest go to the post detail page.
- As a non-register user, on the Blog page, I want to see the search bar to quickly and easily find the post.
- As a non-register user, on the Blog page, I want to sort the posts by name, category, date.
- As a non-register user, on the Blog page, I want to find the posts by category label below the post text. That is to see all posts in this category.
- As a non-register user, on the Blog page, I want to see the Back to Top button, for quick back to the top of the page.
- As a non-register user, on the Blog page I want to see the button View More:
  - View More - button the non-registered user simply redirecting into the Sign In page, as only registered user has access to the Post Detail page.

## Goals

### Visitors Goals

The target audience for X Cherry store are:

- Beginner boxers who will look to purchase a new product for their boxing lessons.
- Advance boxers who will look to update the boxing gear or clothes.
- Boxing clubs who will look to purchase training gear or boxing gear equipment.
- all Boxing sports fans for being active in the Blog.

### User Goals

- Easily navigate through the website.
- Securely sign up, sign in, and login into the website.
- Restore the password.
- Simply buy the product, with calculations for free delivery.
- Saved the delivery information, for future shopping.
- Keep the Order history.
- Used search bar to find the products.
- Sort the products.
- Read the posts on the website Blog.
- Leave the comments for a single post.

### Business Goals

- Sell the products.
- Attract new customers.
- Keep the existing shoppers, sell good quality products for a competitive price.
- Provide all the customer's information they need online so that they do not need to call or email.
- Have an online payment system and keep secure.
- Have instant email notification of purchased products with customer details.

### X Cherry Goal

- Earn income on each sold product.
- Be a leader in sports stores.
- Keep the existing customers and always find new ones.
- Always sold good quality products.
- Customer always the right.

## Strategy

## Scope

## Structure

## Skeleton

### [Wireframe](WIREFRAME.md)

## Features

### Navigation bar

- All pages: Templates (base.html, mobile-top-header.html, main-nav.html)
  - Mobile version - navbar:
    - Click the Hamburger button - drop down the page links:
      - Click the Home link - redirecting to the home page.
      - Clicking the All Products link - the drop-down the 4 links:
        - By Price - show sorted all products for descending order.
        - By Rating - show sorted all products by ascending rating order.
        - By Category - show sorted all products by ascending category order.
        - All Products - show all products.
      - Clicking the Clothing link - the drop-down the 4 links:
        - Compressions - show all compressions clothes from the store.
        - T-Shirts - show all T-Shirts from the store.
        - Shorts - show all shorts from the store.
        - All Clothing - shows all clothing categories on one page.
      - Clicking the Boxing Gear link - the drop-down the 4 category links:
        - Gloves - shows all boxing gloves from the store.
        - Head Guard - shows all head guards from the store.
        - Protective Gear - shows Mouthguard, Groin Guard, Handwraps, Chest Guard Womens from the store.
        - All Boxing Gear - shows all the products from three categories.
      - Clicking the Training Gear link - the drop-down the 4 category links:
        - Skipping Ropes - shows the skipping rope products.
        - Boxing Bag - shows the boxing bag categories products.
        - Speed Bag Platform - shows the speed bag platform category products.
        - All Training Gear - shows all 3 categories of products.
      - Clicking the Blog link - redirecting to the site blog page.
    - Clicking Search bar - input a word and search engine look at the products section.
    - Click the My Account icon:
      - Non-register user - drop down the links for Register and Login pages.
      - Logged in user - drop down the My Profile and Logout pages.
      - Logged in admin - drop down the Product Management, My Profile, Logout pages.
    - Click the Shopping Bag icon - redirecting to the Shopping bag page.
    - Click the Search bar icon - input a word and search engine look at the products section.
    - Click the My Account icon:
      - Non-register user - drop down the links for Register and Login links.
      - Logged in user - drop down the My Profile and Logout links.
      - Logged in admin - drop down the Product Management, My Profile, Logout links.
    - Click the Shopping Bag icon - redirecting to the Shopping bag page.
  - Desktop version - nav bar:
    - Click the Logo - redirecting to the home page.
    - Clicking Search bar - input a word and search engine look at the products section.
    - Click the My Account icon:
      - Non-register user - drop down the links for Register and Login pages.
      - Logged in user - drop down the My Profile and Logout pages.
      - Logged in admin - drop down the Product Management, My Profile, Logout pages.
    - Click the Shopping Bag icon - redirecting to the Shopping bag page.
    - Clicking the All Products link - the drop-down the 4 links:
      - By Price - show sorted all products for descending order.
      - By Rating - show sorted all products by ascending rating order.
      - By Category - show sorted all products by ascending category order.
      - All Products - show all products.
    - Clicking the Clothing link - the drop-down the 4 links:
      - Compressions - show all compressions clothes from the store.
      - T-Shirts - show all T-Shirts from the store.
      - Shorts - show all shorts from the store.
      - All Clothing - shows all clothing categories on one page.
    - Clicking the Boxing Gear link - the drop-down the 4 category links:
      - Gloves - shows all boxing gloves from the store.
      - Head Guard - shows all head guards from the store.
      - Protective Gear - shows Mouthguard, Groin Guard, Handwraps, Chest Guard Womens from the store.
      - All Boxing Gear - shows all the products from three categories.
    - Clicking the Training Gear link - the drop-down the 4 category links:
      - Skipping Ropes - shows the skipping rope products.
      - Boxing Bag - shows the boxing bag categories products.
      - Speed Bag Platform - shows the speed bag platform category products.
      - All Training Gear - shows all 3 categories of products.
    - Clicking the Blog link - redirecting to the site blog page.

### Home app features

- Hero image on loading page.
- Shop Now button. Mouse over change the button background color. Redirecting to the products page.

### Products app features

- products.html features are to store all products on a single page. The single product is wrapped in the card.
  - Product counter - shows how many products are in the store.
  - The card shows the product image, name, price, category(link to this category products), and rating. The website admin has access to edit and delete links beside the rating.
  - The drop-down sort bar - sorting products by price, rating, name, or category.
  - Back to top link - bring you to the top of the page.
  - Break Line - separate the products by the device screen size.
- product_details.html features are single product pages. There is display all information about the product.
  - Product image - bigger size image.
  - Product name
  - Product price
  - Product category - the link that redirected into products page by this category.
  - Product description - the full information about the product.
  - Size - if the product has more than one size there is a drop-down size bar - the user can choose the size.
  - Quantity - how many items the user wants to buy. Always shows 1, but the user can choose from 1-99. There are plus(+) and minus(-) symbols buttons, or the user can simply input the number.
  - Keep Shopping button - redirecting the user into the products page.
  - Add to Bag button - adding the item into the shopping bag. The shopping bag icon in the navbar displays the price and pop-up Success message, which displays all information: product name, size, quantity, total(without delivery), total how much to spend to get free delivery, and button to the checkout page.
- add_product.html features are input form to add the product to the store. Only the admin has access to this page. The form fields are:
  - Category - drop-down bar with all categories that added admin from the Django administration page.
  - SKU - it is product detail short code, the admin can input the max character 254 lengths.
  - Name - product name, max character length are 254 and have an attribute, required.
  - Description - input text, not specified max length, the admin should enough for product description, has attribute required.
  - Has sizes - drop down bar with 3 choices, yes, no, unknown. The choice yes will display the drop-down bar on the Product Detail page.
  - Price - input max 6 numbers with 2 decimal places, has attribute required.
  - Rating - has input max one number and max 2 decimal places.
  - Image URL - has input max 1024 character long URL. Not required, then used default image.
  - Select Image button - add an image from your computer. Not required, then used default image.
  - Cancel button - redirecting the user into the products page.
  - Add Product button - save all input data and redirecting to the Product Detail page. All form fields must be filed as required, otherwise, the error message will pop up.
- edit_product.html features are to edit the Product Detail page. There is the same form as on the Add Product page and all requirements are the same. Here you can simply edit text, replace image. The pop-up messages will display for your success or error for wrong inputs in the form. Only the admin has access to this page.
- Delete product - there are delete product links into Products and the Product Detail pages besides the product rating. Simply removing all product data from the website. Only Admin has access to do it.

### Blog app features

- Blog app features are to store the website post. There only the admin can add new, edit or delete posts. All posts will be displayed by added date order. The Latest added will be first on the page.
  - blogs.html features are:
    - Search bar - searched the input word into the post title or post content. If the word will match the founded posts show by latest first, also displaying how many posts find.
    - Sorting bar - sorting posts by name, category, and date. You can use the search bar to find the post and sort than by date. To reset your searches click the Back to Blog link.
    - Add Post button - only admin has access to this page, there is a hide for other users, but if the user goes to this page by URL, then he will be redirected to 404 error page.
    - The single post will displays into a card: post title, created date, short content about 50 words, post category(link to this category posts), and button to redirecting to the Post Detail page.
    - Back to Top button - stick in the right bottom page corner, simply bring the user top of the page.
  - blog_post_detail.html features are to see the single post with all content.  A registered user has access to this page. There is also a link to edit and delete the post(only admin has access), post category link, button to back to Blog home page. Below the Post Detail content displaying the user's comments. At the bottom of the page, there is the Add Comment form with a button. Added new comments will be displayed at the top in the comment section. Only the admin has access to delete comments. Every single comment has a delete link.
  - add_blog_post.html features are to add a post into the blog. Only the admin has access to do this. There is a form:
    - Category - drop-down bar with categories list, that was added from the Django administration page, has attribute required.
    - Post Title - input field with max 254 character length, has attribute required.
    - Content - input text, not specified max length, the admin should enough for post content, has attribute required.
    - Created by - input text, with max 25 character length, has attribute required.
    - Cancel button - not save the input data and redirecting to the blogs page.
    - Add Post button - save all input data and redirecting to the post_detail page.
  - edit_blog_post.html features are to edit single the blog post. Only the admin has access to this page. There is a form same as like to add post form, just with saved all data that admin can edit or replace. There are two buttons:
    - Cancel button - not save the input data, leave the old data, and redirecting into the blogs page.
    - Update Post button - save the input data and redirecting to the Post Detail page.
  - delete post features are to delete posts with all data from the website. Only the admin has access to do this.

### Profiles app features

- Profiles app features are to keep the user delivery information and order history.
  - profile.html features are the page divided into 2 parts:
    - Default Delivery information - a form with saved user details after the first bought product. All form fields are simply editable if the user needed:
      - Phone Number - the input field with a max of 20 characters long.
      - Street Address 1 - the input field with the max 80 character length.
      - Street Address 2 - the input field with the max 80 character length.
      - Town or City -  the input field with the max 40 character length
      - County, State - the input field with the max 80 character length
      - Postal Code -  the input field with the max 20 character length
      - Country - drop-down bar with a list of countries.
      - Update information - saved the delivery form data and keep the input text into the form.
    - Order History - short order template to store all user orders:
      - Order Number - displaying the long unique order number(link) that will redirect the user into the order history page with the single order information.
      - Date - displaying the order created date.
      - Items - displaying the product item's name.
      - Order total - displaying grand total of the order.

### Bag app features

- Bag app features are the keep all user products before to buy it. There are displaying:
  - Products image
  - Products name
  - SKU
  - Size(if has size)
  - Price
  - Quantity - there is an input bar with plus and minus buttons. The user can use both methods to change the quantity of the product from 1-99.
    - Update link - the user change the product's quantity, click the update link and automatically update all calculations(subtotal, bag total, delivery cost, grand total).
    - Remove link - simply remove the product from the shopping bag page, also update all calculations(subtotal, bag total, delivery cost, grand total).
  - Bag Total
    - Bag Total - product price without delivery cost.
    - Delivery - delivery cost if bag total less than 50, added delivery cost 10% of the Bag Total.
    - Grand Total - are the sum of the Bag Total and Delivery cost.
    - Free delivery message - there is the free delivery message that informs the user how much is left to spend to get free delivery.
  - Keep Shopping button - redirecting the user into the products page and save all products into the shopping bag page. The user can simply back into the shopping bag clicked the bag icon in the navbar.
  - Secure Checkout button - redirecting the user into the checkout page.

### Checkout app features

- Checkout app features are a form and stripe payment details. The page is divided into two sections, user delivery form and order summary. There is also an input payment field and buttons to complete the order. Also, generate unique order number max 32 characters long, that will be displayed in the order history. A confirmation email s sent to the user.
  - Form
    - Full Name - the input field with a max of 50 characters long.
    - Email Address - the input field with a max of 254 characters long.
    - Phone Number - the input field with a max of 20 characters long.
    - Street Address 1 - the input field with a max 80 character length.
    - Street Address 2 - the input field with a max 80 character length.
    - Town or City -  the input field with a max 40 character length
    - County, State - the input field with a max 80 character length
    - Postal Code -  the input field with a max 20 character length
    - Country - drop-down bar with a list of countries.
    - Tick box - for save user form details, for future shopping.
    - Payment - input fields that required Card long number, month/year(mm/yy), Card Certification Code(CVC) and ZIP(Post Code).
    - Adjust Bag button - redirecting the user back to the shopping bag page, save all products in the bag.
    - Complete Order button - proceed with the order(Success message pop-up, email confirmation send) and redirecting the user into the Order History page.
    - The informative small text below the buttons with grand totals calculation.
  - Order Summary(Displaying number of items):
    - Displaying the Products image
    - Displaying the Products name
    - Displaying the Size(if has size)
    - Displaying the Quantity
    - Displaying the Subtotal - single item totals.
    - Order Total - products cost without delivery price.
    - Delivery - delivery cost if bag total less than 50, added delivery cost 10% of the Bag Total.
    - Grand Total - are the sum of the Bag Total and Delivery cost.

### Footer

- The footer features have social media links. The social links open on the new blank tab.

### Future Features ideas

- In the will be added button "Contact Us", the shopper will be redirected to the contact us page. There will be a form that the user will fill in and send to us.
- On the product detail, the page will be adding more products images. That the user can look at the item from all angles. Also will be adding products reviews below the all product detail page. The users can will  write a comment about the product.
- Add Nutrition category on the page. That the user could purchase food supplements.
- Add special offer discount for some period on some products.
- Create social media login to this website.
- Below the hero image will be put on a google map, with pin store location, for users that they want to collect the purchase items.
- At the bottom of the Home page will be a section with "click and collect" information, for local users.

## Responsive

The website using the Bootstrap break point system, dividing the page content from one in the mobile devices, for tablets page content in two parts, laptops in three parts and for others in four parts.

- The navigation bar has responsive design - mobile and tablet divices will be moved into hamburger button.
- The Products pages are moving cards from mobile devices - one card per screen, tablets - two cards, laptops - three cards and for desktops and above four product cards per row.
- The Product Detail page has responsive design - page divided in two parts: image and other product information. On the mobile device, image are top and other information are below, like from tablet view and above, the image and product information are side to side.
- Blog - mobile and tablets devices main post page are keeping single post, laptop have two posts per page, desktop have three posts per page.
- My Profile page are divided in two parts: Delivery information and Order History. Only on the mobile devices those parts splits, delivery info goes up and the order history part goes below for fully strech on the mobile devices. For Tablets and above, those two parts staying side to side.
- Shopping Bag page have responsive design - single product are divided into five parts: those parts on the mobile device, goes in to vertical line for full size on the small screen. The tablets view and above, those parts goes into single row.
- Checkout page are divided in two parts: Delivery form and Order Summary. On the mobiles and tablets view, Order Summary are above to Delivery Form. On the others devices they staying side to side.
- Website all forms has responsive design that will stop the full streach on the biger screens.

## Technologies Used

- [Gitpod](https://www.gitpod.io/) - used to build all the project.
- [GitHub](https://github.com/) - used to host the website.
- [Heroku](https://www.heroku.com/) - used to deploy the website.
- [Django](https://www.djangoproject.com/) - a python web framework for rapid development and design.
- [Stripe](https://stripe.com/en-gb-lt) - payment platform to validate and accept credit card payments securely.
- [AWS S3 Bucket](https://aws.amazon.com/) - store static files and images entered into the databases.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - style Django forms.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) - a collection of custom storage backends with Django to work with boto3 and AWS S3.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- [Gunicorn](https://docs.gunicorn.org/en/stable/) - WSGI HTTP Server for UNIX to aid in deployment of the Django project to Heroku.
- [Pillow](https://pillow.readthedocs.io/en/stable/) - python imaging library to aid in processing image files to store in the database.
- [Psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for python.
- [PIP](https://pip.pypa.io/en/stable/getting-started/) - installation of tools needed for this project.
- [Balsamiq](https://balsamiq.com/) - used to create wireframes.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - used all the time when created the website.
- [Grammarly](https://www.grammarly.com/) - used to check typo mistakes.
- [W3C Markup Validation Service](https://validator.w3.org/) - used to validate HTML code.
- [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - used to validate CSS code.
- [JSHint](https://jshint.com/) - used to validate the jQuery code.
- [PEP8 online](http://www.pep8online.com/) - used to validate the Python code.
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - used to improve the quality of the webpage.

### Databases

- [PostgreSQL](https://www.postgresql.org/) - for the production database, provided by Heroku.
- [SQLite3](https://docs.python.org/3/library/sqlite3.html) - development database, provided by Django.

### Libraries

- [jQuery](https://jquery.com/) - used to make the website interactive.
- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/) - used to create responsive design, grid system, buttons, navbar, dropdown, footer, toast, cards, forms.
- [FontAwesome](https://fontawesome.com/) - provide icons.
- [Google Fonts](https://fonts.google.com/) - styled the website fonts.

### Languages

- [HTML](https://www.w3schools.com/html/default.asp) - used for creating the website.
- [CSS](https://www.w3schools.com/css/default.asp) - used for styling the website.
- [Python3](https://www.w3schools.com/python/default.asp) - for the backend development.

## Deployment

The website was developed using Gitpod workspace to commit and push to GitHub. The project uses GitHub for hosting and has been deployed using Heroku.
To access my page please follow these steps:

### Requirements

- Gitpod or Visual Studio Code
- PIP - install packages in Python.
- stripe - create an account for online payments.
- AWS - create an account cloud storage(create an S3 bucket) for online backup of website static files.
- git - version control system of code source.

### Download

- Navigate to my repository `https://github.com/andrius-siup/cherry-on-the-cake.git` .
- Click the **Code** button.
- Click the **Download Zip**.
- Extract where you want to keep all files.

### Clone Repository

- GitHub navigate to **andrius-siup/cherry-on-the-cake**.
- Click the **Code** button.
- To clone with **HTTPS** copy the URL in the box `https://github.com/andrius-siup/cherry-on-the-cake.git`
- Open your Git Bash.
- Changed the directory to the location you want to clone to be made.
- Type git clone than paste the copied URL  `git clone https://github.com/andrius-siup/cherry-on-the-cake.git` .
- Enter and your local clone will be created.

### Creating an Environment File

Install Requirements.txt file, in your terminal type `pip3 install -r requirements.txt` . Next you will need to create **env.py** file for storing sensitive data,
type `touch env.py` in terminal. This file should never be pushed to GitHub, so type `touch .gitignore` to be able to ignore it. Than open the **.gitignore** file and lets
ignore your **env.py** file typed:

```bash
 env.py 
__pycache__/
```

save and close it.

In the env.py file we need to hide several bits of data. Open env.py file and type:

```bash
import os

os.environ.setdefault("SECRET_KEY", "********")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "********")
os.environ.setdefault("STRIPE_SECRET_KEY", "********")
os.environ.setdefault("STRIPE_WH_SECRET", "********")
```

Replace the secret keys with your own values from your accounts:

- The SECRET_KEY can be generated from the [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) .
- The STRIPE_SECRET_KEY and the STRIPE_PUBLIC_KEY:
  - Sign In stripe.com > Developers > API keys > and you will find the keys.
- The STRIPE_WH_SECRET > Sign In stripe.com > Developers > Webhooks > Add endpoint( run server > copy the URL and add at the end 'checkout/wh/') > than open up the Webhook Details page with Signing key.

Make sure that your env.py file isn't being tracked, type  `git status` and make sure that you can not see it listed.

Or you can store environment variables in Gitpod > Settings > Variables > Environment Variables:

```bash
'DEVELOPMENT', 'True'
'SECRET_KEY', '<copy from Django Secret Key Generator>'
'STRIPE_PUBLIC_KEY', '<copy Stripe Public key>'
'STRIPE_SECRET_KEY', '<copy Stripe Secret key>'
'STRIPE_WH_SECRET', '<copy the Webhook Secret key>'
```

In the settings.py change the DEBUG mode.

```bash
DEBUG = True 
```

Set up the local database by running those commands:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Create a superuser for the database, in order to access Django administration page.

```bash
python3 manage.py createsuperuser
```

And followed the instructions create admin: input name, email, password and repeat the password.

Start your server by typing:

```bash
python3 manage.py runserver
```

### Deployment to Heroku

To deploy the app using Heroku, use the following steps:

1. Go to [Heroku](https://www.heroku.com/) page and login.
1. Create new app by click on **New** and **Create New App** . Enter your unique app name, select your region and than click **create app**.
1. Than find the Resources tab and install the addon Heroku Postgres.
1. To be able to read Heroku environment variables go to **Settings**  than click on **Reveal Config Vars** .
1. Add the following variables:

    ```bash
      KEY 'AWS_ACCESS_KEY_ID' VALUE '<your value>'
      KEY 'AWS_SECRET_ACCESS_KEY' VALUE '<your value>'
      KEY 'DATABASE_URL' VALUE 'Heroku added aytomaticly'
      KEY 'SECRET_KEY' VALUE '<your value>'
      KEY 'STRIPE_PUBLIC_KEY' VALUE '<your value>'
      KEY 'STRIPE_SECRET_KEY' VALUE '<your value>'
      KEY 'STRIPE_WH_SECRET' VALUE '<your value>'
      KEY 'USE_AWS' VALUE 'True'
    ```

1. Migrate the database:

    ```bash
    python3 managa.py makemigrations
    python3 managa.py migrate
    ```

1. Create a superuser for the database, in order to access Django administration page.

    ```bash
    python3 manage.py createsuperuser
    ```

1. Install Green unicorn, which will act as our webserver:

    ```bash
    pip3 install gunicorn
    pip3 freeze > requirements.txt
    ```

1. Create a new Procfile file to tell Heroku create the web dyno:

    ```bash
    web: gunicorn x_cherry.wsgi:application
    ```

1. Push all changes in the Github
1. In the Heroku page, go to Deploy tab and choose the deployment method Github.
1. Enter your Github link and choose the Automatic Deployments, enable every commit to push directly to Heroku.

## Testing

- [Manual Testing](TESTING.md)
- [Code validators](TESTING.md)
- [Lighthouse](TESTING.md)

## Credits

### Media

The [hero image](https://unsplash.com/photos/23h4tMUzGZk) image was borrowed from unsplash website.

All product images and descriptions were borrowed from the real web stores.

- Compressions:

  - [UNDER ARMOUR Heatgear Core Baselayer Shorts Mens](https://www.sportsdirect.com/under-armour-heatgear-core-baselayer-shorts-mens-428276#colcode=42827603)

  - [UNDER ARMOUR Armour Heat Gear Armour Compression Sleeveless Tee](https://www.sportsdirect.com/under-armour-armour-heat-gear-armour-compression-sleeveless-tee-427262#colcode=42726203)

  - [UNDER ARMOUR Heat Gear Armour Long Sleeve Baselayer](https://www.sportsdirect.com/under-armour-heat-gear-armour-long-sleeve-baselayer-427265#colcode=42726503)

  - [UNDER ARMOUR HeatGear Core Tights Mens](https://www.sportsdirect.com/under-armour-heatgear-core-tights-mens-428095#colcode=42809503)

  - [UNDER ARMOUR Heatgear Core T Shirt Mens](https://www.sportsdirect.com/under-armour-heatgear-core-t-shirt-mens-427502#colcode=42750226)

  - [UNDER ARMOUR Heatgear Core T Shirt Mens](https://www.sportsdirect.com/under-armour-heatgear-core-t-shirt-mens-427502#colcode=42750226)

  - [UNDER ARMOUR Heatgear Core T Shirt Mens](https://www.sportsdirect.com/under-armour-heatgear-core-t-shirt-mens-427502#colcode=42750203)

  - [UNDER ARMOUR HeatGear Short Sleeve Compression Baselayer Mens](https://www.sportsdirect.com/under-armour-heatgear-short-sleeve-compression-baselayer-mens-407013#colcode=40701301)

  - [UNDER ARMOUR HeatGear Core Long Sleeve Baselayer Mens](https://www.sportsdirect.com/under-armour-heatgear-core-long-sleeve-baselayer-mens-427500#colcode=42750018)

  - [UNDER ARMOUR HeatGear Core Tights Mens](https://www.sportsdirect.com/under-armour-heatgear-core-tights-mens-428277#colcode=42827703)

  - [UNDER ARMOUR HeatGear Training Baselayer Top Mens](https://www.sportsdirect.com/under-armour-heatgear-training-baselayer-top-mens-427503#colcode=42750326)

  - [UNDER ARMOUR Rush Compression Short Sleeve T Shirt Mens](https://www.sportsdirect.com/under-armour-rush-compression-short-sleeve-t-shirt-mens-427477#colcode=42747702)

  - [UNDER ARMOUR Cg Armour Mock](https://www.sportsdirect.com/under-armour-cg-armour-mock-407020#colcode=40702091)

  - [UNDER ARMOUR Armour High Gear Armour T Shirt](https://www.sportsdirect.com/under-armour-armour-high-gear-armour-t-shirt-427263#colcode=42726309)

- T-Shirts:

  - [LONSDALE Performance Vest Mens](https://www.sportsdirect.com/lonsdale-performance-vest-mens-632019#colcode=63201908)

  - [LONSDALE Performance Vest Mens](https://www.sportsdirect.com/lonsdale-performance-vest-mens-632019#colcode=63201918)

  - [LONSDALE Boxing Vest Top Mens](https://www.sportsdirect.com/lonsdale-boxing-vest-top-mens-632249#colcode=63224925)

  - [LONSDALE Box Tank Vest Men](https://www.sportsdirect.com/lonsdale-box-tank-vest-mens-632251#colcode=63225125)

  - [LONSDALE Boxing Vest Top Mens](https://www.sportsdirect.com/lonsdale-boxing-vest-top-mens-632249#colcode=63224922)

  - [LONSDALE Boxing Vest Top Mens](https://www.sportsdirect.com/lonsdale-boxing-vest-top-mens-632249#colcode=63224901)

  - [LONSDALE T Shirt Mens](https://www.sportsdirect.com/lonsdale-t-shirt-mens-632252#colcode=63225225)

  - [LONSDALE T Shirt Mens](https://www.sportsdirect.com/lonsdale-t-shirt-mens-632252#colcode=63225226)

  - [adidas Base Punch Boxing Vest Red](https://www.elverys.ie/elverys/en/Elverys/Sports/Combat-Sports/Boxing-Equipment/adidas-Base-Punch-Boxing-Vest-Red/p/000000000001086117_RED)

  - [adidas Base Punch Box Vest Black](https://www.elverys.ie/elverys/en/Elverys/Sports/Combat-Sports/Boxing-Equipment/adidas-Base-Punch-Box-Vest-Black/p/000000000001086118_BLACK)

- Shorts:

  - [LONSDALE Box Short Mens](https://www.sportsdirect.com/lonsdale-box-short-mens-632004#colcode=63200450)

  - [LONSDALE Box Short Mens](https://www.sportsdirect.com/lonsdale-box-short-mens-632004#colcode=63200461)

  - [500 WOMEN'S BOXING SHORTS - BLACK](https://www.decathlon.co.uk/p/500-women-s-boxing-shorts-black/_/R-p-196252?mc=8543061&c=BLACK)

  - [LIGHT AND BREATHABLE BOXING SHORTS 500 - GREY](https://www.decathlon.co.uk/p/light-and-breathable-boxing-shorts-500-grey/_/R-p-327374?mc=8600430&c=GREY)

  - [adidas Amateur Boxing Shorts Red White](https://www.fightwearshop.eu/en/adidas-amateur-boxing-shorts-red-white.html)

  - [adidas Amateur Boxing Shorts Blue White](https://www.fightwearshop.eu/en/adidas-amateur-boxing-shorts-blue-white.html)

  - [Lonsdale Box Lightweight Shorts Mens](https://www.sportsdirect.com/lonsdale-box-lightweight-shorts-mens-632244#colcode=63224403)

- Gloves:

  - [Reebok Retail Boxing Gloves](https://ie.sportsdirect.com/reebok-retail-boxing-gloves-762055#colcode=76205571)

  - [EVERLAST 1910 Fight Gloves Unisex Adults](https://ie.sportsdirect.com/everlast-1910-fight-gloves-unisex-adults-421951#colcode=42195116)

  - [EVERLAST 1910 Fight Gloves Unisex Adults](https://ie.sportsdirect.com/everlast-1910-fight-gloves-unisex-adults-421951#colcode=42195190)

  - [EVERLAST P/EL Training Gloves](https://ie.sportsdirect.com/everlast-p/el-training-gloves-762277#colcode=76227718)

  - [EVERLAST P/EL Training Gloves](https://ie.sportsdirect.com/everlast-p/el-training-gloves-762277#colcode=76227703)

  - [ADIDAS Hybrid 100 Boxing Gloves](https://ie.sportsdirect.com/adidas-hybrid-100-boxing-gloves-762031#colcode=76203140)

  - [ADIDAS Hybrid 100 Boxing Gloves](https://ie.sportsdirect.com/adidas-hybrid-100-boxing-gloves-762031#colcode=76203108)

- Head Guards:

  - [ADIDAS Rookie Headguard](https://ie.sportsdirect.com/adidas-rookie-headguard-762202#colcode=76220203)

  - [EVERLAST Elite Head Gaurd Mens](https://ie.sportsdirect.com/everlast-elite-head-gaurd-mens-762022#colcode=76202218)

  - [Adidas AIBA Professional Headguard Boxing Red](https://www.fightwearshop.eu/en/adidas-aiba-professional-headguard-boxing-red.html)

  - [Adidas AIBA Professional Headguard Boxing Blue](https://www.fightwearshop.eu/en/adidas-aiba-professional-headguard-boxing-blue.html)

  - [LONSDALE Club Open Face Headguard](https://www.sportsdirect.com/lonsdale-club-open-face-headguard-770221#colcode=77022169)

  - [Hit Boxing Headguard](https://www.mcsport.ie/collections/boxing-accessories-2629/products/hit-fitness-boxing-headguard)

  - [ADIDAS SPEED FULL FACE HEAD GUARD](https://www.boxfituk.com/adidas-speed-full-face-head-guard/)

  - [ADIDAS SPEED HEADGUARD](https://www.boxfituk.com/adidas-speed-headguard/)

- Protective Gear:

  - [RADIUS HYBRID HAND WRAP SYSTEM](https://www.boxfituk.com/radius-hybrid-hand-wrap-system/)

  - [FLY HAND WRAPS](https://www.boxfituk.com/fly-hand-wraps/)

  - [adidas Men’s PU Groin Guard Black/White](https://www.elverys.ie/elverys/en/Elverys/Sports/Combat-Sports/Boxing-Equipment/adidas-Men%E2%80%99s-PU-Groin-Guard-Black-White/p/000000000001115031_BLACK)

  - [](https://www.elverys.ie/elverys/en/Elverys/Sports/Combat-Sports/Boxing-Equipment/adidas-Base-Punch-Boxing-Short%2C-Black/p/000000000001086116_BLACK)

  - [](https://www.elverys.ie/elverys/en/Elverys/Sports/Combat-Sports/Boxing-Equipment/adidas-Base-Punch-Boxing-Short%2C-Red/p/000000000001086115_RED)

  - [](https://www.elverys.ie/elverys/en/Elverys/Running-%26-Fitness/All-Training-/Nike-Mens-2-Short-Black/p/000000000001114065_BLACK)

  - [PUMA MENS KNIT 10 SESSION SHORT BLACK](https://www.elverys.ie/elverys/en/Elverys/Running-%26-Fitness/All-Training-/Puma-Mens-Knit-10-Session-Short-Black/p/000000000001111873_BLACK)

  - [Everlast 180 inch Handwrap](https://www.sportsdirect.com/everlast-180-inch-handwrap-762057#colcode=76205710)

  - [Everlast 180 inch Handwrap](https://www.sportsdirect.com/everlast-180-inch-handwrap-762057#colcode=76205706)

  - [adidas Knuckle Protectors](https://www.sportsdirect.com/adidas-knuckle-protectors-762321#colcode=76232103)

  - [](https://www.elverys.ie/elverys/en/Elverys/Men/Clothing/T-shirts/Energetics-Mens-Allen-IV-2n1-Short-Black/p/000000000001114789_BLACK)

- Skipping ropes:

  - [BODY SCULPTURE SKIPPING ROPE BLACK](https://www.elverys.ie/elverys/en/Elverys/Fitness/Accessories/Accessories/Body-Sculpture-Skipping-Rope-Black/p/000000000070871001)

  - [BODY SCULPTURE 9' PVC SKIPPING ROPE BLUE](https://www.elverys.ie/elverys/en/Elverys/Fitness/Accessories/Accessories/Body-Sculpture-9%27-PVC-Skipping-Rope-Blue/p/000000000001040347)

  - [BODY SCULPTURE 9 CABLE SPEED SKIP ROPE](https://www.elverys.ie/elverys/en/Elverys/Fitness/Accessories/Skip-Ropes/Body-Sculpture-9-Cable-Speed-Skip-Rope/p/000000000001115188)

  - [Everlast Leather Skipping Rope](https://www.sportsdirect.com/everlast-leather-skipping-rope-760481#colcode=76048190)

  - [USA PRO Pro Cardio Skipping Rope](https://www.sportsdirect.com/usa-pro-pro-cardio-skipping-rope-761037#colcode=76103702)

  - [Everlast Leather Skipping Rope](https://www.sportsdirect.com/everlast-leather-skipping-rope-761356#colcode=76135603)

  - [LONSDALE Club Skipping Rope](https://www.sportsdirect.com/lonsdale-club-skipping-rope-761137#colcode=76113706)

  - [ADIDAS Skipping Rope](https://www.sportsdirect.com/adidas-skipping-rope-762324#colcode=76232403)

- Boxing Bags:

  - [PUNCHING BAG 850 - RED](https://www.decathlon.co.uk/p/punching-bag-850-red/_/R-p-138425?mc=8365166&c=RED)

  - [BOXING PUNCHING BAG 120 - BLUE](https://www.decathlon.co.uk/p/boxing-punching-bag-120-blue/_/R-p-325820?mc=8588398&c=BLUE)

  - [PUNCHING BAG 500 ANGLE - BURGUNDY](https://www.decathlon.co.uk/p/punching-bag-500-angle-burgundy/_/R-p-312721?mc=8574782&c=BORDEAUX)

  - [FREE-STANDING PUNCHING BAG - BLACK](https://www.decathlon.co.uk/p/free-standing-punching-bag-black/_/R-p-7964?mc=8064899&c=BLACK)

  - [LONSDALE Fitness Strike Bag](https://www.sportsdirect.com/lonsdale-fitness-strike-bag-762217#colcode=76221703)

  - [LONSDALE Angle PU Punchbag](https://www.sportsdirect.com/lonsdale-angle-pu-punchbag-852799#colcode=85279969)

  - [USI 3FT NYLON BOXING BAG RED](https://www.elverys.ie/elverys/en/Elverys/Sports/Combat-Sports/Boxing-Equipment/Punchbag/USI-3Ft-Nylon-Boxing-Bag-Red/p/000000000001048465)

  - [USI 5FT NYLON BOXING BAG](https://www.elverys.ie/elverys/en/Elverys/Sports/Combat-Sports/Boxing-Equipment/Punchbag/USI-5Ft-Nylon-Boxing-Bag/p/000000000001048467)

  - [USF BOXING BAG STAND](https://www.elverys.ie/elverys/en/Elverys/Fitness/Home-Gym-Equipment/USF-Range/USF-Boxing-Bag-Stand/p/000000000001048375)

- Speed Bag:

  - [USI ECONOMY SPEED BALL](https://www.elverys.ie/elverys/en/Elverys/Sports/Combat-Sports/Boxing-Equipment/USI-Economy-Speed-Ball/p/000000000001100682)

  - [LONSDALE LION SPEEDBALL PLATFORM](https://www.boxfituk.com/lonsdale-lion-speedball-platform/)

  - [EXIGO ELITE FIXED SPEEDBALL PLATFORM](https://www.boxfituk.com/exigo-club-pro-fixed-speedball-platform/)

  - [HRD HANDMADE SOLID OAK SPEEDBALL PLATFORM](https://www.boxfituk.com/hrd-handmade-solid-oak-speedball-platform/)

  - [CARBON CLAW ADJUSTABLE SPEEDBALL FRAME WITH RIG](https://www.boxfituk.com/carbon-claw-adjustable-speedball-frame-with-rig/)

  - [BBE SPEEDBALL FRAME FOLDING](https://www.boxfituk.com/bbe-speedball-frame-folding/)

  - [PRO BOX ELITE SPEED BALL FRAME](https://www.boxfituk.com/pro-box-elite-speed-ball-frame/)

  - [PRO BOX PROFESSIONAL SPEEDBALL PLATFORM](https://www.boxfituk.com/pro-box-professional-speedball-platform/)

  - [PRO BOX ORIGINAL LEATHER SPEEDBALL](https://www.boxfituk.com/pro-box-original-leather-speedball/)

  - [PRO BOX CLUB SPEEDBALL LEATHER](https://www.boxfituk.com/pro-box-club-speedball-leather/)

### Content

[about gloves](https://protips.dickssportinggoods.com/sports-and-activities/more-sports/how-to-choose-the-right-size-boxing-gloves)

### Code

### Resources

Code Institute course material.

Bootstrap - general resource.

W3Schools - general resource.

Django docs - general resource.

For 403, 404, and 500 Error Handling pages - I will get inspiration from this [tutorial](https://www.youtube.com/watch?v=gsW5gYTNi34).

### Acknowledgements

Brian Macharia - mentor support, huge help through the project.

Code Institute Tutor support team.
