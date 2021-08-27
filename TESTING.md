# Testing

- [Code validators](#code-validators)
- [Lighthouse](#lighthouse)

## Manual testing

- [Register user Home page](#register-user-home-page)
- [Register user Purchase a product](#register-user-purchase-a-product)
- [Non-register user Purchase a product](#not-register-user-purchase-a-product)
- [Admin Add Product](#admin-add-product)
- [Admin Edit Product](#admin-edit-product)
- [Admin Delete Product](#admin-delete-product)
- [Admin Add Post](#admin-add-post)
- [Admin Edit Post](#admin-edit-post)
- [Admin Delete Post](#admin-delete-post)
- [Admin Delete Comment](#admin-delete-comment)

## Founded Bugs

- [Bugs](#bugs)

## Register user Home page

| Test | Action | Result | Errors |
| ---| --- | --- | --- |
| Logo and Home link | Clicking on the navigation bar's navbar Logo or a Home(on the mobile device) link has been routed to the home page.| Tested, works as should.| No |
| Register | Clicking on the navigation bar's My Account icon. Clicking the Register link has been routed to the Register page. Input the details in the form and the user will be redirected to the confirm email page. After confirming the email address the user will be redirected to the sign-in page. Input details and the user will be Sign In to the website. |  Tested, works as should. | No |
| Login | Clicking on the navigation bar's My Account icon. Clicking the Login link has been routed to the login page. Input details and the user will be Sign In to the website.| Tested, works as should.| No |
| Logout | Clicking on the navigation bar's My Account icon. Clicking the Logout link has been routed to the Logout page. Clicking the Sign Out button, the user will be signed out from the website. | Tested, works as should.| No |
| Password Reset | Clicking on the navigation bar's My Account icon. Clicking the Login link has been routed to the login page. Below the buttons click the Forgot Password link, the user will be redirected to the Password Reset page. Enter the email address, the user will get the email with a link to the Change Password page. Entered new password, the user will get a message that a new password will be added successfully. Then the user can sign in with a new password. | Tested, works as should.| No |
| Home > Shop Now | Clicking the Shop Now button, the user will be redirected to the Products page. | Tested, works as should.| No |
| My Profile | They have to be login to the website. Clicking on the navigation bar's My Account icon. Clicking on the My Profile link the user will be redirected to the My Profile page. | Tested, works as should.| No |
| My Profile > Delivery Form | In My profile the Default delivery information form, the user easily can edit the form. Clicking the Update Information button, the form will save new data, and a Success message will be displayed. | Tested, works as should.| No |
| My Profile > Order History | The Order numbers are unique for every single order and the user can click on that link and will be redirected to the Order History page with that order details. | Tested, works as should.| No |
| Shopping Bag | Clicking on the navigation bar's Bag icon, the user will be redirected to the Bag page. | Tested, works as should.| No |
| Search bar | Clicking on the navigation bar's the search bar, the user can enter the word and search engine look at the product's data(title or description). If the word will match the searched word, the products will be count and displayed on the page. | Tested, works as should.| No |
| Search bar > without entering a word | Clicking on the navigation bar's the search bar icon(without entered a word), the user will be redirected to the product page. Also, pop up the Error message. | Tested, works as should.| No |
| All Products > By Price | Clicking the All Products link the drop-down menu will be shown the 4 links: clicking By Price link - the user will be redirected to the Products page and all products will be displayed by price descending order. | Tested, works as should.| No |
| All Products > By Rating | Clicking the All Products link the drop-down menu will be shown the 4 links: clicking By Rating link - the user will be redirected to the Products page and all products will be displayed by rating ascending order. | Tested, works as should.| No |
| All Products > By Category | Clicking the All Products link the drop-down menu will be shown the 4 links: clicking By Category link - the user will be redirected to the Products page and all products will be displayed by category alphabet ascending order. | Tested, works as should.| No |
| All Products > All Products | Clicking the All Products link the drop-down menu will be shown the 4 links: clicking All Products link - the user will be redirected to the Products page and all products from all categories will be displayed. | Tested, works as should.| No |
| Clothing > Compressions | Clicking the Clothing link the drop-down menu will be shown the 4 links: clicking Compressions link - the user will be redirected to the Products page and all products from this category will be displayed on the page. | Tested, works as should.| No |
| Clothing > T-Shirts | Clicking the Clothing link the drop-down menu will be shown the 4 links: clicking the T-Shirts link - the user will be redirected to the Products page and all products from this category will be displayed on the page. | Tested, works as should.| No |
| Clothing > Shorts | Clicking the Clothing link the drop-down menu will be shown the 4 links: clicking Shorts link - the user will be redirected to the Products page and all products from this category will be displayed on the page. | Tested, works as should.| No |
| Clothing > All Clothing | Clicking the All Clothing link the drop-down menu will be shown the 4 links: clicking All Clothing link - the user will be redirected to the Products page and all products from all clothing categories will be displayed on the page. Also below is the page Header that displays links to this category sub-categories.  | Tested, works as should.| No |
| Boxing Gear > Gloves | Clicking the Boxing Gear link the drop-down menu will be shown the 4 links: clicking Gloves link - the user will be redirected to the Products page and all products with this category will be displayed on the page. | Tested, works as should.| No |
| Boxing Gear > Head Guard | Clicking the Boxing Gear link the drop-down menu will be shown the 4 links: clicking Head Guard link - the user will be redirected to the Products page and all products with this category will be displayed on the page. | Tested, works as should.| No |
| Boxing Gear > Protective Gear | Clicking the Boxing Gear link the drop-down menu will be shown the 4 links: clicking Protective Gear link - the user will be redirected to the Products page and all products with this category will be displayed on the page. | Tested, works as should.| No |
| Boxing Gear > All Boxing Gear | Clicking the Boxing Gear link the drop-down menu will be shown the 4 links: clicking All Boxing Gear link - the user will be redirected to the Products page and all products from the Boxing Gear categories will be displayed in the page. Also below is the page Header that displays links to this category sub-categories. | Tested, works as should.| No |
| Training Gear > Skipping Rope | Clicking the Training Gear link the drop-down menu will be shown the 4 links: clicking Skipping Rope link - the user will be redirected to the Products page and all products with this category will be displayed on the page. | Tested, works as should.| No |
| Training Gear > Boxing Bag | Clicking the Training Gear link the drop-down menu will be shown the 4 links: clicking Boxing Bag link - the user will be redirected to the Products page and all products with this category will be displayed on the page. | Tested, works as should.| No |
| Training Gear > Speed Bag Platform | Clicking the Training Gear link the drop-down menu will be shown the 4 links: clicking Speed Bag Platform link - the user will be redirected to the Products page and all products with this category will be displayed on the page. | Tested, works as should.| No |
| Training Gear > All Training Gear | Clicking the Training Gear link the drop-down menu will be shown the 4 links: clicking All Training Gear link - the user will be redirected to the Products page and all products from the all Training Gear categories will be displayed in the page. Also below is the page Header that displays links to this category sub-categories. | Tested, works as should.| No |
| Products Home | The link will be displayed on all product pages and redirecting the user to the Product page. | Tested, works as should.| No |
| Products Counter | Displaying in all product pages and showing the total of products on that page. | Tested, works as should.| No |
| Sort bar > Price(low to high) | Clicking the sort bar and pick up the Price(low to high) field, the products will be sorted by price descending order on all product pages. | Tested, works as should.| No |
| Sort bar > Price(high to low) | Clicking the sort bar and pick up the Price(high to low) field, the products will be sorted by price descending order on all product pages. | Tested, works as should.| No |
| Sort bar > Rating(low to high) | Clicking the sort bar and pick up the Rating(low to high) field, the products will be sorted by rating ascending order on all product pages. | Tested, works as should.| No |
| Sort bar > Rating(high to low) | Clicking the sort bar and pick up the Rating(high to low) field, the products will be sorted by rating descending order on all product pages. | Tested, works as should.| No |
| Sort bar > Name(A-Z) | Clicking the sort bar and pick up the Name(A-Z) field, the products will be sorted by name alphabet ascending order on all product pages. | Tested, works as should.| No |
| Sort bar > Name(Z-A) | Clicking the sort bar and pick up the Name(Z-A) field, the products will be sorted by name alphabet descending order on all product pages. | Tested, works as should.| No |
| Sort bar > Category(A-Z) | Clicking the sort bar and pick up the Category(A-Z) field, the products will be sorted by category alphabet ascending order on all product pages. | Tested, works as should.| No |
| Sort bar > Category(Z-A) | Clicking the sort bar and pick up the Category(Z-A) field, the products will be sorted by category alphabet descending order on all product pages. | Tested, works as should.| No |
| Sort bar > Sort by | Clicking the sort bar and pick up the Sort by field, the products will be reset sort search. | Tested, works as should.| No |
| Back to Top | Clicking the right bottom corner link up arrow, this is the "Back to Top" link, which bring the user to the top of the page. All product pages have this feature. | Tested, works as should.| No |
| Sub-category > below the single product price | Clicking the tag icon with the category name, the user will redirect to this category products page. | Tested, works as should.| No |
| Blog | Clicking on the navigation bar's the Blog link, the user has been routed to the blog page.| Tested, works as should.| No |
| Blog > Search bar | The user can enter the word into the Blog search bar and the search engine looks at the posts data(title and description). If the word will match the searched word, the posts will be count and displayed on the page. | Tested, works as should.| No |
| Back to Blog | The link will be displaying on all post pages and redirecting the user to the Blog page. | Tested, works as should.| No |
| Posts Counter | Displaying in all post pages and showing the total of posts on that page. | Tested, works as should.| No |
| Blog > Sort bar > Name(A-Z) | Clicking the sort bar and pick up the Name(A-Z) field, the post will be sorted by name, alphabet ascending order on all post categories pages. | Tested, works as should.| No |
| Blog > Sort bar > Name(Z-A) | Clicking the sort bar and pick up the Name(Z-A) field, the post will be sorted by name, alphabet descending order on all post categories pages. | Tested, works as should.| No |
| Blog > Sort bar > Category(A-Z) | Clicking the sort bar and pick up the Category(A-Z) field, the posts will be sorted by category, alphabet ascending order on all post pages. | Tested, works as should.| No |
| Blog > Sort bar > Category(Z-A) | Clicking the sort bar and pick up the Category(Z-A) field, the posts will be sorted by category, alphabet descending order on all post pages. | Tested, works as should.| No |
| Blog > Sort bar > Date(Oldest-Latest) | Clicking the sort bar and pick up the Date(Oldest-Latest) field, the posts will be sorted by date, ascending order(oldest post will be displayed at top of the page) on all posts pages. | Tested, works as should.| No |
| Blog > Sort bar > Date(Latest-Oldest) | Clicking the sort bar and pick up the Date(Latest-Oldest) field, the posts will be sorted by date, descending order(Latest post will be displayed at the top of the page) on all posts pages. | Tested, works as should.| No |
| Sort bar > Sort by | Clicking the sort bar and pick up the Sort by field, the products will be reset sort search. | Tested, works as should.| No |
| Post Category | Clicking the post category (tag icon with the category name, below the post), the user will be redirected to this category posts. | Tested, works as should.| No |
| View More | Clicking the View More button, below the post on the Blog page, the user will be redirected to the Single Post page. | Tested, works as should.| No |
| Back to Top | Clicking the right bottom corner link up arrow, this is the "Back to Top" link, which will bring the user to the top of the page. All post pages have this feature. | Tested, works as should.| No |
| Single Post page > Post Category | Clicking the post category (tag icon with the category name, below the post content), the user will be redirected to this category posts. | Tested, works as should.| No |
| Single Post page > Back to Blog | The link will be redirecting the user to the Blog page. | Tested, works as should.| No |
| Single Post page > Add Comment | Fill up the form. Enter the name, email, and the text, the user can click on the Add Comment button, and the comment will be displayed in the Comments section, below the single post. The latest comment will be displayed at the top of the other comments. | Tested, works as should.| No |
| Single Post page > Back to Top | Clicking the right bottom corner link up arrow, this is the "Back to Top" link, which will bring the user to the top of the page. All single post pages have this feature. | Tested, works as should.| No |
| Footer > Facebook | Clicking the Facebook icon on the footer, the user will be redirected on the blank window to the Facebook(future will be website account) page. | Tested, works as should.| No |
| Footer > Instagram | Clicking the Facebook icon on the footer, the user will be redirected on the blank window to the Instagram(future will be website account) page. | Tested, works as should.| No |
| Footer > LinkedIn | Clicking the Facebook icon on the footer, the user will be redirected on the blank window to the LinkedIn(future will be website account) page. | Tested, works as should.| No |
| Footer > Github | Clicking the Facebook icon on the footer, the user will be redirected on the blank window to the Github(in the future will be replaced into another social media website account) page. | Tested, works as should.| No |
---

## Register user Purchase a product

| Test | Action | Result | Errors |
| ---| --- | --- | --- |
| Product Detail | On the product detail page, the user clicks the Add to Bag button. Then bag icon will be updated with grand total calculations and a pop-up Success message with a summary of the product. In the message also are button to link to the shopping bag page. | Tested, works as should.| No |
| Shopping Bag > Update Qty | On the shopping bag page the user can update the product quantity, simply clicking the quantity bar plus or minus buttons, or entered the number between 1-99. Clicking the update link the  Success message will be pop-up with update totals calculations, also bag icon will be updated too. |Tested, works as should.| No |
| Shopping Bag > Remove Qty | Clicking the remove quantity link, the product will be removed from your bag, Success message will pop up and the user will be redirected to the Shopping Bag page. | Tested, works as should.| No |
| Shopping Bag > Keep Shopping | The user adds the product into the bag and looking for something else. Clicking the Keep Shopping button on the Shopping Bag page the user will be redirected to the Products page. The Shopping Bag page will be saved added products data while the user back to this page. | Tested, works as should.| No |
| Shopping Bag > Secure Checkout | Clicking the Secure Checkout button the user will be redirected to the Checkout page with all product data. | Tested, works as should.| No |
| Checkout > Complete Order Form | The user has to enter the details into the form to complete the order. | Tested, works as should.| No |
| Checkout > Tick box | Clicking the tick box, the user entered details will be saved here and also on the My Profile page. | Tested, works as should.| No |
| Checkout > Payment | Entered card number(4242 4242 4242 4242), for MM/YY(valid month and year like 05/25), for CVC(3 any digit numbers), for ZIP(5 any digit numbers), the user will be ready to purchase the product. | Tested, works as should.| No |
| Checkout > Complete Order | Clicking the Complete order button, if form and payment fields are validated the user will redirect to the Checkout Success page with order details summary. Also, a Success message will pop up and an email confirmation will be sent to the user email. | Tested, works as should.| No |
| Checkout Success > Go Back To All Products | Clicking the Go Back To All Products button, the user will be redirected to the Products page. | Tested, works as should.| No |
| Checkout > Adjust Bag | Clicking the Adjust Bag button on the Checkout page, all Bag data will be saved and the user will be redirected to the Shopping Bag page to edit the product list. | Tested, works as should.| No |
---

## Not register user Purchase a product

| Test | Action | Result | Errors |
| ---| --- | --- | --- |
| Product Detail | On the product detail page, the user clicks the Add to Bag button. Then bag icon will be updated with grand total calculations and a pop-up Success message with a summary of the product. In the message also are buttons to link to the shopping bag page. | Tested, works as should.| No |
| Shopping Bag > Update Qty | On the shopping bag page the user can update the product quantity, simply clicking the quantity bar plus or minus buttons, or entered the number between 1-99. Clicking the update link the  Success message will be pop-up with update totals calculations, also bag icon will be updated too. |Tested, works as should.| No |
| Shopping Bag > Remove Qty | Clicking the remove quantity link, the product will be removed from your bag, Success message will pop up and the user will be redirected to the Shopping Bag page. | Tested, works as should.| No |
| Shopping Bag > Keep Shopping | The user adds the product into the bag and looking for something else. Clicking the Keep Shopping button on the Shopping Bag page the user will be redirected to the Products page. The Shopping Bag page will be saved added products data while the user back to this page. | Tested, works as should.| No |
| Shopping Bag > Secure Checkout | Clicking the Secure Checkout button, the user will be redirected to the Sign In page with the saved bag data. After entered the Sign In details the user will be redirected to the Checkout page to complete the order. | Tested, works as should.| No |
---

## Admin Add Product

| Test | Action | Result | Errors |
| ---| --- | --- | --- |
| Add Product | Clicking the My Account icon > Product Management, the admin will be redirected to the Product Management page that can add product. | Tested, works as should.| No |
| Add Product > Form | The Form has required fields that have to be entered to submit that form. The Success message will be a pop-up that informs the admin of a successfully added product to the store. | Tested, works as should.| No |  
| Add Product > Category | Clicking the category drop-down bar, the bar displays the category list, that was added from the Django administration page. | Tested, works as should.| No |
| Add Product > label with * | The form labels marked with stars are required and have to be filled in, to submit the form. | Tested, works as should.| No |
| Add Product > Description | Description form field can be extended with drag the mouse from the right bottom corner. | Tested, works as should.| No |
| Add Product > Has sizes | Has sizes drop-down bar display the option to add the size list on the product. If a product has a size the product detail page display the size list. | Tested, works as should.| No |
| Add Product > Select Image |  Clicking the Select Image button, the window will pop up and the admin can add an image from the computer disk. | Tested, works as should.| No |
| Add Product > Cancel | Clicking the Cancel button all entered data will be not saved and the admin will be redirected to the products page. | Tested, works as should.| No |
| Add Product > Add Product | Clicking the Add Product button, the form will be saved, all input data will be redirected to the single product. All form fields must be filed as required, otherwise, the error message will pop up. | Tested, works as should.| No |
---

## Admin Edit Product

| Test | Action | Result | Errors |
| ---| --- | --- | --- |
| Edit Product > Products | Clicking the edit link beside the product rating on the Products page, the admin will be redirected to the Edit Product page of this product. The alert message will be pop-up with the product title. | Tested, works as should.| No |
| Edit Product > Product Detail | Clicking the edit link beside the product rating on the Product Detail page, the admin will be redirected to the Edit Product page of this product. The alert message will be pop-up with the product title. | Tested, works as should.| No |
| Edit Product > Form | The Form came with saved details that the admin can be edit. The form has required fields that have to be entered to submit that form. The Success message will be a pop-up that informs the admin of a successfully edited product to the store. | Tested, works as should.| No |
| Edit Product > Category | Clicking the category drop-down bar, the bar displays the category list, that was added from the Django administration page. | Tested, works as should.| No |
| Edit Product > label with * | The form labels marked with stars are required and have to be filled in, to submit the form. | Tested, works as should.| No |
| Edit Product > Description | Description form field can be extended with drag the mouse from the right bottom corner. | Tested, works as should.| No |
| Edit Product > Has sizes | Have sizes drop-down bar display the option to add the size list on the product. If a product has a size the product detail page display the size list. | Tested, works as should.| No |
| Edit Product > Tick box | Clicking the tick box with label Remove, then clicked the Update Product button. The Product image will be removed.| Tested, works as should.| No |
| Edit Product > Select Image |  Clicking the Select Image button, the window will pop up and the admin can add an image from the computer disk, replace the previous image. | Tested, works as should.| No |
| Edit Product > Cancel | Clicking the Cancel button all entered data will be not saved(previous data will be left) and the admin will be redirected to the products page. | Tested, works as should.| No |
| Edit Product > Update Product | Clicking the Update Product button, the form will be saved(data), all input data will be redirected to the single product page. All form fields must be filed as required, otherwise, the error message will pop up. | Tested, works as should.| No |
---

## Admin Delete Product

| Test | Action | Result | Errors |
| ---| --- | --- | --- |
| Delete Product | Clicking the Delete link on the Products page, beside the product Rating. The product will be removed from the website and the Success message will be pop-up. The admin will be redirected to the Products page. | Tested, works as should.| No |
| Delete Product | Clicking the Delete link in the Product Detail page, beside the product Rating. The product will be removed from the website and the Success message will be pop-up.  The admin will be redirected to the Products page. | Tested, works as should.| No |
---

## Admin Add Post

| Test | Action | Result | Errors |
| ---| --- | --- | --- |
| Blog > Add Post | Clicking the button beside the search bar in the Blog Page. The Admin will be redirected to the Add Post page. | Tested, works as should.| No |
| Add Post > Category | Clicking the category drop-down bar, the bar displays the category list, that was added from the Django administration page. Have attribute, required. | Tested, works as should.| No |
| Add Post > Post Title | Entered the text with a max of 254 characters in length. Have attribute, required. | Tested, works as should.| No |
| Add Post > Post Content | Entered text, not specified max length, the admin should enough for post content. Have attribute, required. | Tested, works as should.| No |
| Add Post > Created by | Entered text, with max 25 character length. Have attribute, required. | Tested, works as should.| No |
| Add Post > Cancel | Clicking the Cancel button, the form data will be not saved and the admin will be redirected to the Blogs page. | Tested, works as should.| No |
| Add Post > Add Post | Clicking the Add Post button, the form saves all input data and the admin will be redirected to the Post Detail page. | Tested, works as should.| No |
---

## Admin Edit Post

| Test | Action | Result | Errors |
| ---| --- | --- | --- |
| Blog > Edit post | Clicking the Edit link below the post category tag, in the Blog Page, the admin will be redirected to the Edit Post page. The alert message will be pop-up with the post title. | Tested, works as should.| No |
| Post Detail > Edit post | Clicking the Edit link above the post category tag, in the Post Detail Page, the admin will be redirected to the Edit Post page. The alert message will be pop-up with the post title. | Tested, works as should.| No |
| Edit Post > Category | Clicking the category drop-down bar, the bar displays the category list, that was added from the Django administration page. Have attribute, required. The admin can edit the category from the list. | Tested, works as should.| No |
| Edit Post >  Post Title | The admin can edit or enter the new Post Title text with a max of 254 characters length. Have attribute, required. | Tested, works as should.| No |
| Edit Post >  Post Content | The admin can edit or enter the new Post content, with max length not specified, the admin should enough for post content, has attribute required. | Tested, works as should.| No |
| Edit Post >  Created by | The admin can edit or enter the new name, with max 25 character length, has attribute required. | Tested, works as should.| No |
| Edit Post >  Cancel | Clicking the Cancel button, the form data will be not saved and the admin will be redirected to the Blogs page. | Tested, works as should.| No |
| Edit Post >  Update Post | Clicking the Update Post button, the form saves all input data and the admin will be redirected to this Post Detail page. | Tested, works as should.| No |
---

## Admin Delete Post

| Test | Action | Result | Errors |
| ---| --- | --- | --- |
|  |  |
| Delete Post | Clicking the Delete link on the Blog page, below the single post category tag. The post will be removed from the website and the Success message will be pop-up. The admin will be redirected to the Blog page. | Tested, works as should.| No |
| Delete Post | Clicking the Delete link in the Post Detail page, above the post category tag. The post will be removed from the website and the Success message will be pop-up.  The admin will be redirected to the Blog page. | Tested, works as should.| No |
---

## Admin Delete Comment

| Test | Action | Result | Errors |
| ---| --- | --- | --- |
|  |  |
| Post Detail > Delete Comment | Clicking the Delete link in the Comment, the comment will be removed from the website. | Tested, works as should.| No |
---

## Bugs

![FieldError at /blog/](/media/readme/bug-same-word-in-modul-created.png)

Fixed this error to replace **created_date** into **date**.

![MultipleObjectsReturned at /blog/11/](/media/readme/multipleobjectsreturned.png)

I fixed this error by added an objects filter (```comments = BlogPostComment.objects.filter(post=post)```).

![UnboundLocalError at /blog/11/](/media/readme/unbundlocalerror.png)

I fixed this error by adding a local variable (``` global post ```) to the function.

![AttributeError at /blog/edit/11/](/media/readme/attributeerror.png)

Typo error. I fixed this error by adding S in word FILE.

### The secret key was accidentally pushed to the repo

- Removed the secret key from **settings**
- Generate the new one key here [Random django key](https://djecrety.ir/)
- store that key in gitpod settings environment variables as SECRET_KEY
- in **settings** set the key like this `SECRET_KEY = os.environ.get('SECRET_KEY', '')`

### The Stripe Issues

- sometimes accidentally Gitpod will change app URL and it doen't match the Stripe endpoint. When I saw the stripe error it will fix it easily change the stripe endpoint that will match the Gitpod app URL. Otherwise, stop the server, restart the workspace, and restart the server.

![Webhook Details](/media/readme/webhook-details.png)

 have to match to:

![Gitpod app URL](/media/readme/gitpod-app-url.png)

## Code validators

### W3C HTML Validator

There was found error, duplicate id. Fixed that, renamed id.

![W3C HTML Validator](/media/readme/lighthouse/html.png)

### W3C CSS Validator

No errors, just few warnings.

![W3C CSS Validator](/media/readme/lighthouse/base.css.png)

### JSHint

No errors, just two warnings.

![jshint](/media/readme/lighthouse/jshint.png)

### PEP8 Online

I will check the python code on this tool, which showed just too long lines, but no errors. For lack of time, I will do that later.

## Lighthouse

Mobile test

![mobile](/media/readme/lighthouse/mobile-first-test.png)

Desktop test

![desktop](/media/readme/lighthouse/desktop-first-test.png)

- Buttons do not have an accessible name:
  - Added into the search button ``` aria-label="Enter search term" ```

- Links do not have a discernible name:
  - Added into the social media icon links ``` aria-label="with the name of social media" ```

- Heading elements are not in a sequentially-descending order:
  - For delivery banner. Replace h4 into h2 and set font-size 1em.
  - For Shop Now button. Replace h4 into div.

- Links to cross-origin destinations are unsafe:
  - Added attribute rel="noopener" into anchor for social media links.

- Document does not have a meta description:
  - Added meta desription ``` <meta name="description" content="Boxing website store for beginners and advanced boxers."> ```

After added atributes

![all-pass](/media/readme/lighthouse/all-pass.png)
