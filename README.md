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

## The secret key was accidentally pushed to the repo. 
* Removed the secret key from settings.py
* Generate the new one key here [Random django key]("https://djecrety.ir/")
* store that key in gitpod settings environment variables as SECRET_KEY
* in settings.py set the key like this `SECRET_KEY = os.environ.get('SECRET_KEY', '')`


## The Stripe Issues:
* sometimes accidentally Gitpod will change app URL and it doen't match the Stripe endpoint. When I saw the stripe error it will fix it easily change the  stripe endpoint. 



## Media

[hero image](https://unsplash.com/photos/23h4tMUzGZk) 

[speed platform](https://www.geezersboxing.co.uk/punching-bags/speedbags-platforms/geezers-fixed-speedball-platform) 

## Content
[about gloves](https://protips.dickssportinggoods.com/sports-and-activities/more-sports/how-to-choose-the-right-size-boxing-gloves) 