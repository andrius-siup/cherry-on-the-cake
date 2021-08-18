 ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome andrius-siup,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. The last update to this file was: **July 2, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## User Stories

* As a user, I expect that the site logo always brings me to the home page.
* As a user, I expect to be able to sign up to this website and get the email confirmation.
* As a user, I want to be able to sign up to this site and get all user access, buy products, read the blog posts, write comments.
* As a user, I expect to be able to save my sign-in details for future access to this site.
* As a user, I expect to be able to restore my forgotten password.
* As a user, I want to easily navigate through all the pages.
* As a user, I expect to be able to the shopping bag icon with the amount into the navigation bar, for easily manage my spending.
* As a user, I want to get success, info, and errors messages for my daily uses.
* As a user, I want to know if there is a free delivery from this site.
* As a user, in the Products page I want to find products by category, subcategories.
* As a user, in the Products page I want to sort products by price, rating, name, and category.
* As a user, in the Products page I want to be able to access to the product detail page, to see product description, choose size and quantity, also see the rating and category a clickable.
* As a user, in the Products page I want to see the Back to Top button if there is a lot of products.

* As a user, in the Product Detail page I want to be able to see the product image in the bigger view.
* As a user, in the Product Detail page I want to see the ADD TO BAG button in the product details page, to add a product in the shopping bag.
* As a user, in the Product Detail page I want to see the message success when I added the product into the shopping bag.
* As a user, in the Product Detail page I expect to be able to see a success messages with all details of the product like name, how many items are in the bag, items image, total, info line with getting free delivery, and button go to checkout.

* As a user, in the Shopping bag page I expect to be able to do changes like: add more and remove the number of products, also see updates of bag total, delivery cost, and grand total.
* As a user, in the Shopping bag page I expect to be able to see the cost of the products: like bag total, delivery cost and grand total. Also, the info text with calculations to get free delivery.
* As a user, in the Shopping bag page I expect to be able to see buttons like: back to Products page and go to Secure Checkout page.

* As a user on the checkout page I want to see the form to complete my order, like my own details, delivery information, and payment card field.
* As a user on the checkout page I expect to be able to see the Order summary with all totals.
* As a user on the checkout page I expect to be able to save my own delivery information for future shoppings.
* As a user on the checkout page, I want to be able to back into the shopping bag to do some change.

* As a user, on the Checkout Success page, I want to see the order information with all details.
* As a user, on the Checkout Success page, I want to see the success message with the order number and email confirmation.
* As a user, on the Checkout Success page, I want to be able back to the products page.

* As a user of the website I would like to has access to the site Blog, to read the useful posts.
* As a user on the Blog page I want to see the latest post at, top of the Blog.
* As a user on the Blog page, I want to see all posts with a short text, to read a little bit, and if is interest go to post detail page.
* As a user on the Blog page I want to see the search bar to quick and easy find the post.
* As a user on the Blog page, I want to sort the posts by name, category, date.
* As a user on the Blog page I want to find the posts by category label below the post text. That is to see all posts in this category.
* As a user on the Blog page I want to see the Back to Top button, for quick back to the top of the page.
* As a user on the Blog page I expect to be able to see the post detail page.

* As a user, on the Blog post detail page, I want to see the full post and Back to Blog button.
* As a user, on the Blog post detail page, I want to add a comment below the post, or ask interesting questions.
* As a user, in the Blog post detail page, I want to see others registered users' comments.
* As a user in the Blog post detail page, I want to see the latest comment at top of the all comments.
* As a user, in the Blog post detail page, I want to see the Back to Top button, to quickly back to the top of the page.

* As a user I want to be able to access the My Profile page with delivery information, also can be an editable form if something changes with my address.
* As a user, I expect to be able to see my order history on my profile page.

## Site owner/admin user stories

* As an admin of the website, I want to have access to the add, edit or delete products and blog posts also access to delete user's comments.
* As an admin of the website, in the My Account icon, I want to see the Product Management link, which will be redirected into Add product page.
* As an admin of the website, on the Add Product page, I would like to see a user-friendly input form, that I can manually add new products.
* As an admin of the website, in the Add Product page form, I want to see the form fields:
  * Category
  * SKU
  * Name
  * Description
  * Have sizes
  * Price
  * Rating
  * Image URL
  * Add local image
    * buttons:
      * Add Product - save the new data and redirect into the Product Detail page. To look how everything looks from the user's side.
      * Cancel - data not saved and simple back into the Products page.

* As an admin of the website, in the Products page and Product detail page, I want to see the edit and delete product links.
* As an admin of the website, on the Edit Product page, I want to see the form with the all details of the product that I want to edit.
* As an admin of the website, on the Edit Product page, I want to simply remove old information and add new text or replace the image.
* As an admin of the website, on the Edit Product page, I want to see two buttons:
  * Update - save new information and redirected to the Product Detail page, to see how looks from the customer side.
  * Cancel - leave the old data(same data) and redirected to the Products page.
* As an admin of the website, in the Products page and Product Detail page, I want to see the Delete link, for a simple removed product with all data from the site.

* As an admin of the website, on the Blog page, near the search bar button, I want to has the Add Post button, to add new posts.
* As an admin of the website, on the Add Post page, I want to see a simple input form with fields:
  * Choose Category
  * Post Title
  * Input text
  * Created by
  * Two buttons:
    * Add Post - Save all information and redirected to the Post Detail page.
    * Cancel - simply redirected to the Blog page.

* As an admin of the website, in the Blog page and in the Post Detail page, I want to see the edit and delete links:
  * Edit link - which will be redirected into the Edit Post page, with all post details saved into form.
    * In the Edit Post form I want to simply edit text or change the category.
    * Also I want to see two buttons:
      * Update - save the new data and redirected to the Post detail page.
      * Cancel - leave the old data(same data) and redirected to the Blog page.
    * Delete link - simple removed post with all data from the site.
* As an admin of the website, in the Post Detail page, in the single comment, I want to see the delete link, which simply removed the comment from the site.

## Non-register user stories

* As a non-register user, I expect that the site logo always brings me to the home page.
* As a non-register user, I expect to be able to Sign Up for this website.
* As a non-register user, I want to easily navigate through all the pages.
* As a non-register user, I want to know if there is a free delivery from this site.
* As a non-register user, on the Products page, I want to find products by category, subcategories.
* As a non-register user, on the Products page, I want to sort products by price, rating, name, and category.
* As a non-register user, on the Products page, I want to see the Back to Top button if there is a lot of products.
* As a non-register user, in the Products page I want to be able to access to the Product Detail page, to see full product informationproduct.

* As a non-register user, on the Product Detail page I want to be able to see the product full information:
  * Product Name
  * Price
  * Category (link to this category)
  * Description
  * Rating
  * Choose Size (if has size - xs, s, m, l, xl)
  * Quantity (buy more than one - 1-99)
  * Buttons :
    * Back to Products - simple redirecting the non-register user into the Products page.
    * Add to Bag - add the product into the shopping bag, display the item price into the bag icon(into the navigation bar).
* As a non-register user, on the Product Detail page, I want to see the message success when I added the product into the shopping bag.
* As a non-register user, in the Product Detail page I expect to be able to see success messages with all details of the product like name, how many items are in the bag, items image, total, info line with getting free delivery, and button go to checkout.

* As a non-register user, on the Shopping bag page, I expect to be able to do changes like add more and remove the number of products.
* As a non-register user, on the Shopping bag page I expect to be able to see the cost of the products: like bag total, delivery cost, and grand total. Also, the info text with calculations to get free delivery.
* As a non-register user, on the Shopping bag page I expect to be able to see buttons like:
  * Back to Products - redirecting non-register user into the Products page.
  * Secure Checkout - redirecting the non-register user to the Sign In page. The non-register user can't buy items without sign in to the website.

* As a non-register user, I would like to has access to the site Blog, to read the useful posts.
* As a non-register user, on the Blog page, I want to see the latest post at, top of the Blog.
* As a non-register user, on the Blog page, I want to see all posts with a short text, to read a little bit, and if is interest go to the post detail page.
* As a non-register user, on the Blog page, I want to see the search bar to quickly and easily find the post.
* As a non-register user, on the Blog page, I want to sort the posts by name, category, date.
* As a non-register user, on the Blog page, I want to find the posts by category label below the post text. That is to see all posts in this category.
* As a non-register user, on the Blog page, I want to see the Back to Top button, for quick back to the top of the page.
* As a non-register user, on the Blog page I want to see the button View More:
  * View More - button the non-registered user simply redirecting into the Sign In page, as only registered user has access to the Post Detail page.

## Features

* All pages: Templates (base.html, mobile-top-header.html, main-nav.html)
  * Mobile version - nav bar:
    * Click the Hamburger button - drop down the page links:
      * Click the Home link - redirecting to the home page.
      * Clicking the All Products link - the drop down the 4 links:
        * By Price - show sorted all products for descending order.
        * By Rating - show sorted all products by acsending rating order.
        * By Category - show sorted all product by ascending category order.
        * All Products - show the all products.
      * Clicking the Clothing link - the drop down the 4 links:
        * Compressions - show all compressions cloths from the store.
        * T-Shirts - show all T-Shirts from the store.
        * Shorts - show all shorts from the store.
        * All Clothing - shows all clothing categories in one page.
      * Clicking the Boxing Gear link - the drop down the 4 category links:
        * Gloves - shows all boxing gloves from the store.
        * Head Guard - shows all head guards from the store.
        * Protective Gear - shows Mouthguard, Groin Guard, Handwraps, Chest Guard Womens from the store.
        * All Boxing Gear - shows all the products from three categories.
      * Clicking the Training Gear link - the drop down the 4 category links:
        * Skipping Ropes - shows the skipping rope products.
        * Boxing Bag - shows the boxing bag categories products.
        * Speed Bag Platform - shows the speed bag platform category products.
        * All Training Gear - shows the all 3 categories products.
      * Clicking the Blog link - redirecting into the site blog page.
    * Clicking Search bar - input a word and  search engine look at the products section.
    * Click the My Account icon:
      * Non-register user - drop down the links for Register and Login pages.
      * Logged in user - drop down the My Profile and Logout pages.
      * Logged in admin - drop down the Product Management, My Profile, Logout pages.
    * Click the Shopping Bag icon - redirectting into Shopping bag page.
    * Click the Search bar icon - input a word and  search engine look at the products section.
    * Click the My Account icon:
      * Non-register user - drop down the links for Register and Login links.
      * Logged in user - drop down the My Profile and Logout links.
      * Logged in admin - drop down the Product Management, My Profile, Logout links.
    * Click the Shopping Bag icon - redirectting into Shopping bag page.
  * Desktop version - nav bar:
    * Click the Logo - redirecting to the home page.
    * Clicking Search bar - input a word and  search engine look at the products section.
    * Click the My Account icon:
      * Non-register user - drop down the links for Register and Login pages.
      * Logged in user - drop down the My Profile and Logout pages.
      * Logged in admin - drop down the Product Management, My Profile, Logout pages.
    * Click the Shopping Bag icon - redirectting into Shopping bag page.
    * Clicking the All Products link - the drop down the 4 links:
      * By Price - show sorted all products for descending order.
      * By Rating - show sorted all products by acsending rating order.
      * By Category - show sorted all product by ascending category order.
      * All Products - show the all products.
    * Clicking the Clothing link - the drop down the 4 links:
      * Compressions - show all compressions cloths from the store.
      * T-Shirts - show all T-Shirts from the store.
      * Shorts - show all shorts from the store.
      * All Clothing - shows all clothing categories in one page.
    * Clicking the Boxing Gear link - the drop down the 4 category links:
      * Gloves - shows all boxing gloves from the store.
      * Head Guard - shows all head guards from the store.
      * Protective Gear - shows Mouthguard, Groin Guard, Handwraps, Chest Guard Womens from the store.
      * All Boxing Gear - shows all the products from three categories.
    * Clicking the Training Gear link - the drop down the 4 category links:
      * Skipping Ropes - shows the skipping rope products.
      * Boxing Bag - shows the boxing bag categories products.
      * Speed Bag Platform - shows the speed bag platform category products.
      * All Training Gear - shows the all 3 categories products.
    * Clicking the Blog link - redirecting into the site blog page.
* Home app features :
  * Hero image on loading page.
  * Shop Now button. Mouse over change the button background color. Redirecting to the products page.
* Products app features:
  * products.html features are to store all products in the single page.The single product is wrapped in the card.
    * Product counter - shows how many products are in the store.
    * The card shows the product image, name, price, category(link to this category products) and raiting. The website admin has access to edit and delete links beside the rating.
    * The drop down sort bar - sorting products by price, rating, name or category.
    * Back to top link - bring you at the top of the page.
    * Break Line - separate the products by the divece screen size.
  * product_details.html features are single product page. There is display all information about the product.
    * Product image - biger size image.
    * Product name
    * Produc price
    * Product category - link that redirected into products page by this category.
    * Product description - the full information about the product.
    * Size - if product has more than one size there is a drop down size bar - the user can choose the size.
    * Quantity - how many items user want to buy. Always shows 1, but user can choose from 1-99. There are plus(+) and minus(-) simbols buttons, or the user can simply input the number.
    * Keep Shopping button - redirecting the user into the products page.
    * Add to Bag button - adding the item into shopping bag. The shopping bag icon in the nav bar display the price and pop-up Success message, that displaying the all information: product name, size, quantity, total(without delivery), total how much to spend to get free delivery, and button to chekout page.
  * add_product.html features are input form to add product to the store. Only admin has access to this page. The form fields are:
    * Category - drop down bar with all categories that added admin from the django administration page.
    * SKU - it is product detail short code, the admin can input the max character 254 lenght.
    * Name - product name, required and max character lenght are 254, and has attribute required.
    * Description - input text, not specified max lenght, the admin should enough for product description, has attribute required.
    * Has sizes - drop down bar with 3 choises, yes, no, uknown. The choise yes will display the drop down bar into product_detail page.
    * Price - input max 6 numbers with 2 decimal places, has attribute required.
    * Rating - has input max one number and max 2 decilam places.
    * Image url - has input max 1024 character long url. Not required, than used default image.
    * Select Image button - add image from your computer. Not required, than used default image.
    * Cancel button - redirecting the user into the products page.
    * Add Product button - save the all input data and redirecting into the product_detail page. All form fields must be filed as required, otherwise the error message will pop-up.
  * edit_product.html features are to edit the product_detail page. There are same form like in add_product page and all requirements are same. Here you can simply edit text, replace image. The pop-up messages will display for your success or error for wrong inputs in the form. Only admin has access to this page.
  * Delete product - there are delete product link into products and the product_detail pages beside the product rating. Simply removing all product data from the website. Only Admin has access to do it.
* Blog app features are to store the website post. There only admin can add new, edit or delete posts. All posts will be displayed by added date order. Latest added will be first on the page.
  * blogs.html features are:
    * Search bar - searched the input word into the post title or post content. Founed posts shows by latest first, also displaying how many posts find.
    * Sorting bar - sorting posts by name, category and date. You can used search bar for find the post and sort than by date. To reset your searches click the Back to Blog link.
    * Add Post button - only admin has access to this page, there is a hide for others users, but if the user goes to this page by URL, than he will redirected into 404 error page.
    * The single post will displays into card: post title, created date, short content about 50 word, post category(link to this category posts) and button to post detail page.
    * Back to Top button - sticked in the right bottom page corner, simply bring the user top of the page.
  * blog_post_detail.html features are to see the single post with all content. Only registered user has access to this page. There is also a link to edit and delete the post(only admin has access), post category link, button to back to Blog home page. Below the post detail content displaying the users comments. At the bottom of the page, there are the Add Comment form with button. Added new comment will be displayed at the top in comment section. Only admin has access to delete comments. Every single comment has delete link.
  * add_blog_post.html features are to add a post into the blog. Only admin has access to do this. There is a form:
    * Category - drop down bar with categories list, that was added from the django administration page, has attribute required.
    * Post Title - input field with max 254 character lenght, has attribute required.
    * Content - input text, not specified max lenght, the admin should enough for post content, has attribute required.
    * Created by - input text, with max 25 character lenght, has attribute required.
    * Cancel button - not save the input data and redirecting into the blogs page.
    * Add Post button - save all input data and redirecting into the post_detail page.
  * edit_blog_post.html features are to edit single the blog post. Only admin has access to this page. There is a form same as like to add post form, just with saved all data that admin can edit or replace. There is two buttons:
    * Cancel button - not save the input data, leave the old data and redirecting into the blogs page.
    * Update Post button - save the inputed data and redirecting into the post_detail page.
  * delete post features are to delete post with all data from the website. Only admin has access to do this.
* Profiles app features are to keep the user delivery information and order history.
  * profile.html features are the page divided into 2 parts:
    * Default Delivery information - a form with saved user details after the first buyed product. The all form fields are simply editable if user needed:
      * Phone Number - the input field with max 20 character long.
      * Street Address 1 - the input field with the max 80 character length.
      * Street Address 2 - the input field with the max 80 character length.
      * Town or City -  the input field with the max 40 character length
      * County, State - the input field with the max 80 character length
      * Postal Code -  the input field with the max 20 character length
      * Country - drop down bar with list of countries.
      * Update information - saved the delivery form data and keep the input text into form.
    * Order History - shortr order template to store the all user orders:
      * Order Number - displaying the long unique order number(link) that will redirecting the user into the order history page with the single order information.
      * Date - displaying the order created date.
      * Items - displaying the product items name.
      * Order total - displaying grand total of the order.




## The secret key was accidentally pushed to the repo

* Removed the secret key from settings.py
* Generate the new one key here [Random django key]("https://djecrety.ir/")
* store that key in gitpod settings environment variables as SECRET_KEY
* in settings.py set the key like this `SECRET_KEY = os.environ.get('SECRET_KEY', '')`

## The Stripe Issues

* sometimes accidentally Gitpod will change app URL and it doen't match the Stripe endpoint. When I saw the stripe error it will fix it easily change the  stripe endpoint.

## Media

[hero image](https://unsplash.com/photos/23h4tMUzGZk)

[speed platform](https://www.geezersboxing.co.uk/punching-bags/speedbags-platforms/geezers-fixed-speedball-platform)

## Content

[about gloves](https://protips.dickssportinggoods.com/sports-and-activities/more-sports/how-to-choose-the-right-size-boxing-gloves)
