# [Golf Mania](https://golf-mania.herokuapp.com/)

![Landing Page](static/images/landing-page-screenshot.png "HighDunes Landing Page")
[LANDING PAGE SCREENSHOT]

### **What is Golf Mania?**

Golf Mania is an online e-commerce, web application designed to sell golf related products from Ireland. The website sells several brands in many categories and also offers an easy navigation system to allow the user to have full control of their actions during their site visit and buying experience. The web applications main aim is to sell new and used golf products from Ireland.
- Site users can browse the website and add products to their basket without the need to **register** or **log in**.
- Once logged in, the user has the **ability** to proceed to checkout and purchase items followed by confirmation.
- As a logged in user, a profile can be saved using the billing information which eases future purchases.
- Descriptive golf products with lots of interactive features throughout the purchasing experience.
- Email verification/confirmation included.

Currently, Golf Mania's website only consists of example products that can potentially be sold on the website. However, the **Project Aim** is to demonstrate how a business of any size can buy and sell products online while maintaining a high *Search Engine Optimization*. This kind of website could work with any theme/category/brand etc. This particular project focuses on selling cheap, golf equipments to its online customers.

Golf Mania currently has a low number of products and product types but given the database models, this can be expanded on quite easily from any perspective which makes it an ideal project to start off with. The project is set it up with **Stripe payment system** and billing information is saved to the project's database through **Stripe webhook** for safer online data transfer.

A review app has been included which can also be expanded by implementing more CRUD functionality which would be beneficial for building **customer confidence**.

### **How it works?**

1. The header offers lots of features to the site user that they have access to at all times, from the moment they land on the site. They can search for specific items, register, log in, filter/sort specific product or browse all products. 

2. The landing page offers a large image that is fixed under the header with a **Welcome Message** with a button that takes the user to view all of the products, which is the key function of the site and the reason the site user landed on the site. 

3. Site users can view special deals on the landing page and reviews. From the products page which is *accessible* through the sticky header or the landing image button. 

4. From the moment the site user starts clicking on product to view them in detail, they can use features such as *zoom in/out* or *read more* features. Products can also be added to the basket that is created as a session for them as well as **opening the basket** and **edit** it given all four CRUD functionalities *available* to them *without* the need to **log in**.

5. If the site wishes to proceed to check out, the **log in button** appears on the basket page. If logged in already, the continue to **secure checkout** button is available instead. 

6. As a logged in user, the site user has access to their personal profile which they can either set up *before purchasing products* or *when filling out their delivery details*, they tick the box to save their delivery information for future purchases.

7. Once the checkout form is filled out and submitted, the site user is directed to the **checkout confirm** page where they can review their order details. However, this only happens **if the payment intent is successful** to ensure no order goes through without a payment. The order data is transferred to stripe *via webhooks* and if the payment is successfull, the data is safely transferred back to Golf Mania's database as an *order*.

### **Who is it for?**

Ireland is home to over 200 golf courses. As a result, it has become a popular region for global golfers to visit for the 66 million golfers worldwide and it also attracts more locals to start playing the sport. Golf Mania currently next day delivery over the delivery allowance of €80. This gives confidence for **tourists** to make cheap orders which they can receive the next day during their holiday as well as being a great online golf store for **Irish golfers** to buy cheaper products from, **used** and **new**.

**New Users**

New Users have the ability to view the website and all of its products in detail without the need to enter any data. However, if they wish to make full use and make a purchase, an account needs to be registered first which is either available through the top header or the view basket html page. Once an account is registered and email is verified, the site user has the ability to either create a profile for themselves for each future purchase or they can just save their delivery details during their first purchase. 

**Returning Users**

As a returning user, the site user can **log in**, **add items** to their bag, proceed to checkout and **only** fill in their *payment details*, if they have saved their information or if they have a profile set up. This speeds up their purchasing experience **substantially**. 

## **Planning**

### **Agile Planning Approach from Start to Finish**

The developer of this project has taken an Agile approach when planning out this e-commerce web application. He created and reviewed a list of **Epic Stories** which he further broke down into smaller user stories to give himself a more precise estimate of the length of time it is going to take to create the project.

He started off by created an **Issue Template** on Golf Mania's Github page and used it to implement each user story broken down. Each of them included a precise explanation of what the user wants followed by **Acceptance Criteria** and **Tasks** for the developer's use. *Example is shown below*.

![Full User Story, Acceptance Criteria and Tasks]()

Another **Agile tool** used to proceed with these issues was to implement the **MOSCOW Prioratization** and split these *User Stories* into 4 categories. *Must-have*, *Should-have*, *Could-have* and *Would-have* issues. A **label** for each was created and each issue was labelled in order of importance during development i.e, what features are essential for release and what features can wait until further updates.

A **Milestone** called *GolfMania E-Site* was then created where the developer prioratized the user stories in order of importance which offered a clean direction in terms of the overall, project workflow.

**Milestone Review**

![Milestone Project (open issues)]() 

![Milestone Project (closed issues)]()

The developer then created a Project called **GolfMania E-Commerce Site User Stories** where he set up three columns **To Do**, **In Progress** and **Done**. This is where he moved each user story across and monitored what user stories have been completed, are in progress and what still needs to be done. The labels helped to identify the important user stories which needed to moved across first followed by should have's and etc. 

![GitHub Project Layout]()

Overall, given the Epic Stories provided at the start, a total of 35 Issues were identified and further broken down into tasks. A total of **129 tasks** were created. Once each issue was labelled by the developer, out of 35, **19** issues/user stories were identified as **Must-Have** features (just under 60%) which consisted of 75 tasks out of 129 not surpassing the **60% mark** given that an **Agile Timeboxing Approach** is considered to estimate the length of the project.

### **Search Engine Optimisation Planning**

Once the project was deployed, the developer used [https://www.xml-sitemaps.com/](https://www.xml-sitemaps.com/) to create a sitemap file for Golf Mania which was then copied into a newly created **sitemap.xml** file in the main project. 

A **robots.txt** was also created where the search engine is given permission to access the website and follow every page except the urls including **/accounts/**.

The developer has also researched the Google Search Engine for key words that he can use within meta tags built into the base.html file to make it findable using the **right** keywords.

Below are examples of what the developer was researching and where the key words used in the meta tags were discovered. 

![Meta Google Search Key Words Image One]()

![Meta Google Search Key Words Image Two]()

**Keyword** brainstorming in progress

![Meta Google Search Key Word Brainstorm]()

### **Marketing Strategies Planning**

The developer came up with a **Customer Persona** i.e, the ideal customer for the e-commerce site followed by *forms of essential marketing* that Golf Mania's project is to include. 

![Marketing Strategies Planning Process]()

### **Further Planning**

The style of writing was decided through **Google Fonts**. The main writing is kept thin for a cleaner, more elegent style while the headings style was thicker.

![Google fonts chosen style](static/images/google-fonts-style.png)

The main theme colors were chosen on [coolors.co](https://coolors.co/palette/004b23-006400-007200-008000-38b000-70e000-9ef01a-ccff33) in order to find colours which work together very well and hence, provide a better visual experience for site users.

![Main color theme chosen](static/images/coolors-color-theme.png)

**Bootstrap** is used to design the overall strucuture of the website on screens of all sizes. 
[startbootstrap.com](https://startbootstrap.com/previews/landing-page) was used to choose the main strucuture of this golf web app. The link above is linked with the specific theme used for this project. 

**Custom CSS** will be used to design the visual look of the website.

**Buttons**

[codepen.io](https://codepen.io/annguyn/pen/xNVprL) was used to select an overall button style for this project.

##### **HTML page structure sketches**

**1. Landing Page** 

The landing page was planned and designed by reviewing several applications with similar business goals such as [https://www.onlinegolf.eu/](https://www.onlinegolf.eu/). Each section within this page were listed in order of importance i.e. header with search features followed by landing image with view product button. Deals and offers are displayed thereafter followed by some reviews and finally, the footer which container the **Newsletter section**.

![Landing page sketch](static/images/landing-page-sketch.jpg)

#### Landing page (Mobile View)

The main header was re-designed by the developer for mobile views to ensure all features are displayed well and look aesthetically pleasing. 

![Landing page mobile view sketch]()

**2. Products Page** 

This is where all products can be viewed in rows of 4 on larger screens and rows of one for smaller screen. Sorting can specify the user's search. This page can accessed via the header or the landing image.

![Products page sketch]()

**3. Product Detail Page**

When the user click on a specific product in any of the pages, they are taken to this page where product data is displayed.

![Product details page sketch]()

**4. Basket Page**

When the user adds a product into their basket from the product details page, a session is created within her where the list of items added are stored and ready to interact with CRUD function created in views.py

![Basket page sketch]()

**5. Checkout Page**

Once logged in, the user can access this page through their basket page when they are ready with their basket to make a payment.

![Checkout page sketch]()

**6. Checkout Confirm Page**

Once a payment is received via Stripe, webhooks confirm the payment and this page is rendered with the order details sent back to the database with it.

![Checkout confirm page sketch]()

**7. Add Product Page**

Only accessibly by the superuser/admin. Accessible via the header where products can easily be added to the page.

![Add Product page sketch]()

**8. Profile Page**

Once the user is logged in, this page also accessible via the header where delivery profile can be set up and order history can also be viewed.

![Profile page sketch]()

**9. Delete product page**

Instead of automatically deleting a product with one click, this page will work as defense to ensure the admin wants this CRUD funcitonality to proceed, as it cannot be reversed.

![Delete product page sketch]()

**10. Update product page**

Accessible within each product and feature is only available to the admin.

![Update product page sketch]()

**11. AllAuth custom design for Account html pages**

All of these html pages provided by allauth include different forms so therefore, the styling of all these can also be identical. 

![AllAuth Form page sketches]()

#### **Workflow Process**

The workflow process for **New Users** and **Returning Users** when interacting with the features included within this e-commerce site. 

![E-Commerce App Workflow Process]()

#### **Project Apps and Relationships**

Overall, **five main applications** were built the very least while using *Django AllAuth's user model* also. 

![Project Apps and Relationships]()

**Seven different models** were also planned within these five applications and how they will be linked to each other. 

![Model Sketches]()

The **CRUD** functionality was also planned for each application. i.e. to what extent can a Site User or Admin manipulate data built from the models as shown above. 

![CRUD APP Function sketch]()

## 2. **Features (existing)**

All of the **buttons** throughout all of the html pages are styled and colored consistenly for enhanced visual look from a user point of view which includes **padding, background color, hover effect and text color**.

The background color of each html page is also kept identical in terms of color, mainly a **light green** color set using *RGB* and **white** in other parts for *contrast*. 

In terms of text, the website interacts with all of its users one to one when the user is logged and phrases/text content is also written as if there was **one user only**. 

### 1. **Landing Page**

#### **Header**

The header is included within *base.html* which indicates that it is displayed in every html page and it is also set **sticky** so that it follows the user as they scroll down the page.

It consists of three sections:

- The logo on the left hand side. Normally speaking, like the developer, most **users** would almost expect a website logo to **reload the home page** so to keep these type of users satisfied with this application, the **golf club name** and **logo** is a link to the home page which always follows the *user*.

- In the middle, a search bar is available for the user to type in keywords to find specific products. For example, if they're interested in golf balls, they can type golf balls find related products.

- On the right hand side, the site user can find **register** or **login** buttons which are linked with relevant AllAuth html pages followed by a basket icon which links with *basket.html*. If products are added to the basket, the price under the basket icon updates and displays the **total** of the user's basket.

**Not Signed In**

If the user is not signed in, only three features are visible.

1. **Register Link**
2. **Log in Link**
3. **Basket Link**

![Header Not Logged In]()

Signed In as Site User

Once the user signs in, the two buttons are replaced with an My Account and icon which acts as a dropdown list for more features such as viewing and creating My Profile. My is used as it is from a user's point of view.

1. **Home**
2. **My Profile**
3. **Log Out**

![Header Not Logged In as Site User]()

**Signed In as Admin**

If signed in as Admin, two additional features are available to the **superuser** which are the **Admin Panel** and **Add Product**. Through the admin panel, the superuser has *full control* of Golf Mania database. The Add Product feature tells it function and it terms of style, it matches the overall theme of Golf Mania's website.

![Header Logged In As Admin]()

#### **Main Nav Bar**

Contains **4** main **dropdown lists**. The first dropdown focuses on sorting products using their *model field data* such as *price*, *rating*, *brand* etc. The other two offer the main products while the final dropdown list consists of special offers which are displayed throughout the website.

![Main Nav Bar]()

#### **Delivery Banner**

Contains a delivery message telling the site user that over the delivery threshold, Golf Mania offers *free next day delivery* which fades in and out using **CSS in static/base.css**.

![Delivery Banner]()

#### **Header (mobile view)**

In mobile view, all features within the header are rearranged for an enhanced visual look. The *website logo* is displayed at the top with a *direct home link*. The Main Nav dropdown lists are placed in another dropdown lists as *clickable icon*. All of the account features are now placed within in icon as a dropdown. The *log in and register buttons* are also replaced with a **dropable list**. The *search bar* is given full width as well as the *delivery banner*.

![Mobile view of Header]()

#### **Landing Image**

The landing image covers 100VH to visually attract the site users attention to the *Welcome Message and some ear catching info about the Spring Sale*. This section also contains a **View All Products** feature as a **button**.

![Landing Image]()

#### **Clearance Section**

In this section, a list of category **"clearance"** products are advertised which have all been reduced in terms of price to increase the chances of catching the site users eyes and each product is *clickable* to **view in full detail** and add to their basket if they so wish. 

In terms of view, this section display **4** products on *large* screens, **2** on *medium* and **1** on *smaller* screens to maintain the size of photo for better visual design. 

![Clearance Section]()

#### **Reviews Section**

In this section, two reviews would be allowed to be viewed and after that, they would paginate which is built into index.html. For now, the two reviews were added via the *admin panel* to demonstrate what they would look like once the CRUD functionality of the reviews app is developed further to allow customers leave their on reviews which can then be approved by the admin. This is an area where external reviews could also be imported or included as images. For example, **Trustpilot** reviews.

In terms of view, this section displays **2** products on *larger* screens and **1** on smaller screens.

![Reviews Section]()

#### **Footer Section**

The footer contains several features which are always available to the user at the bottom of each page. It starts with a **Sign Up to Newsletter** feature which is built through **mailchimp** so each email entered is validated and saved using mailchimp.

In the middle, four external social media page icons are equally alligned starting off with *Facebook's Icon* which is linked with Golf Mania's newly built **Facebook Business Page**.

In case, the page gets deleted by Facebook, the following three images are screenshot of Golf Mania's facebook page.

![Facebook Image One]()

![Facebook Image Two]()

![Facebook Image Three]()

At the bottom of the footer, a **payment** image is displayed which tells the user what payment types are accepted on Golf Mania's website followed by the developer's signature.

![Footer]()


### 2. **Products Page**

As every page, the products page includes the header and footer features. 

#### **Top Section**

When the products.html page is loaded, depending on whether a search criteria was entered or a category through the main nav bar, a message on the top right displays the number of products found for the category or the search typo.

Accross, a filter feature is available to the site user to filter products by a specific field such as by price, brand etc. All of these options will also list the filtered products in price/alphabetical order and reversed to offer as many filtering options to the user as possible. Each function works instantly using some *Javascript at the bottom of the page*. 

Below the above features is a Back to Home button that the site user can use to go back to the index page and clear any sorting/filtering options. 

![Products page top section]()

#### **Products Section**

The products are listed in rows of **4** on *larger screens*, **2** on *media screens* and **1** on mobile screens. Each product is **clickable** to view each product **in detail** using *product_detail.html*. From a site user's point of view, the most important data is displayed here to spark their interest within the products. Examples, are **price**, **rating** and whether its *new* or *used*. The category type of each product is also displayed which works as a **link** if the user wants to be redirected to view a *clicked* category. 

![Products section as Site User]()

As a site admin, two additional features are available. To **update** and **delete** a specific product.

![Products section as Site Admin]()

As seen in the screenshots above, their is a *see-through up-arrow* **button** which takes the user **back to the top** of the page with a click given that all products are listed on the one page. This button is visible and available to the user through all screen sizes and works using *Javascript* at the bottom of this page.


### 3. **Product Detail Page**

#### **Image Section**

On the left hand side, the product image is 400px by 400px. When clicked, the image is opened in a separate tab for the site user to view. Below the image, Zoom In and Zoom Out features are available to the site user to maintain a good level of interactivity. 

![Products page top section]()

#### **Product Details Section**

The product details sections displays all the data stored for each product including the category icon which is linked with the product's specific category. To maintain a visually appealing view, only the productt description is displayed with an additional features section if the user clicks the Read More button. If signed in as *Admin*, the **update** and **delete** functions are available in this page also.
The **rating** row is set so that any product with a *rating better than 4* will display the message **"Highly Recommended"**.

The user has full control of the quantity that the can add to the basket using the Add to Basket button. This feature is validated to ensure that at least 1 product needs to be added but no more than 99 and this is controlled with the Minus and Plus button.

Once the product is added to the basket, the user would assumingly continue shopping so a Keep Shopping button is also displayed. At this point, the basket can either be viewed using the button displayed within a **successfully added toast** or the basket icon in the main header where the total is calculated and displayed. 

#### **Newest Products Section**

In this section, a list of category **"new in"** products are advertised and each product is *clickable* to **view in full detail** and add to their basket if they so wish. Only vital, eye-catching data is displayed to maintain a large image size.

In terms of view, this section display **4** products on *large* screens, **2** on *medium* and **1** on *smaller* screens to maintain the size of photo for better visual design. 

![Newest Products Section]()

### 4. **Basket Page**

The shopping basket page is split into two sections.

On the left hand side, all of the products within the basket are displayed in rows. The product image is smaller and also **clickable** to go back to view the product in detail again. The **quanity** can be **adjusted** by the user along with **removing** items from the basket. 

![Shopping Basket Product Details]()

On the right hand side, the order summary is displayed with the *basket total* and a *delivery total* of €10.00 if basket total is under €80.00. An *alert message* is displayed under the delivery total if it is **chargable** while a **pleasing message** is displayed if the basket total is above €80.00. The order total is styled to stand out which is important for the user to know before proceeding. 

The feature buttons available under order summary are **Keep Shopping** which takes the user back to the products page and **Secure Checkout** if logged in or **Sign In to Continue** otherwise. The workflow process cannot continue to *checkout* unless the user is logged in.

**Shopping Basket Order Summary Logged In**
![Shopping Basket Order Summary Logged In]()

**Shopping Basket Order Summary Logged Out**
![Shopping Basket Order Summary Logged Out]()

### 5. **Checkout Page**

The checkout page is also split into two sections.

On the *right hand side*, the shopping basket details are displayed for the last time followed by the order summary. The user can still go back to the basket and edit it using the **edit basket** internal link to go back to **basket.html**. The product image is also **clickable** in this section to view the product in **product_details.html** again to be sure. 

![Checkout Shopping Basket]()

On the *left hand side*, the checkout form is displayed and validated using django forms and required fields set for vitals information for delivery purposes. 

The developer has included a field for additional information that the site user may want to share in terms of delivery. Required fields are labelled with **"*"** and a short message under the form explains this feature. If the user does not have a profile set up yet or if they need to update their profile using the typed in delivery data, there is a **Save Delivery Information** checkbox that is checked and calls a function using the Stripe payment system's webhooks. 

![Checkout Form]()

At the bottom of this section, the "Payment section" is imported using Stripe where payment details are entered and validated.

Below, two buttons are displayed. 

1. Back to **Basket Button**
2. **Complete Order** Button to send Stripe the validated data and take payment and a small message underneath telling the user how much they are going to be charged as a final **alert message**

![Checkout Buttons]()

For responsive design, the **Shopping Basket and Order Summary** is displayed first on smaller screens followed by the **checkout and payment form** to maintain the workflow.


### 6. **Checkout Confirm Page**

#### **Checkout Confirm Top Section**

The checkout confirm page is rendered if the payment intent is successfull. It offers a **personal Thank You message** followed by and **Shop Again Button** linked with the *products page*. At this point, a confirmation email is sent to the user confirming the order and the email receiving this is displayed at the top of the page also. 

![Checkout Confirm Top of the page from Checkout]()

The user has access to view order histories through their profile page. As a result, the message at the top is changed as well as the **button** to **Back to My Profile**. An *info toast* is also rendered to keep the user up to date in case they clicked into it by accident. 

![Checkout Confirm Top of the page from Profile]()

#### **Order Summary Section**

Below, the order summary is broken into three sections when displaying order data. **Personal**, **Delivery** and **Cost Summary** details. 

![Checkout Confirm Order summary]()

#### **Newest Products Section**

In this section, a list of category **"new in"** products are advertised and each product is *clickable* to **view in full detail** and add to their basket if they so wish. Only vital, eye-catching data is displayed to maintain a large image size.

In terms of view, this section display **4** products on *large* screens, **2** on *medium* and **1** on *smaller* screens to maintain the size of photo for better visual design. 

![Checkout Confirm Newest Product Section]()

### 7. **Add Product Page**

This page is only available to the admin. A warm welcome message greets the superuser and below, it displays the product form using crispy forms to enhance the visual look of the form itself so that products can be instantly added to the products page and its a feature doable in an environment that matches the overall theme of the website rather than logging into the admin panel. 

![Add Product Top of page]()

The image field has been styled to match the general button style while the image file name is also displayed when one is selected. If not image is selected, the standard **no image** file will replace the empty field.

At the bottom of the form, two buttons are displayed:
1. **Cancel** - to bring the admin back to the products page.
2. **Add Product** - to add the new product to the database.

![Add Product Bottom of page]()

### 8. **Update Product Page**

The update product page is quite identical to the add product page. The title at the top changes to **Update Product** and an *instance* of a specific product is displayed that is changeable.

![Update Product Top of page]()

The image field displays the current image saved with an additional feature to remove the image altogether or upload a new one instead.

In terms of the buttons at the bottom, instead of the Add Product, an **Update Button** is displayed. 

![Update Product Bottom of page]()

### 9. **Delete Product Page**

This page is only visible to the admin again when deleting products.
It acts as an additional level of defense in case the delete function was called by mistake. The page displays the **name** and **sku** of the product selected followed by:
1. **Cancel button** - to cancel delete function and return to products.html
2. **Submit Button** - to confirm and delete product. 

![Delete Product Page]()

### 10. **Profile Page**

The profile can be opended via the fixed top header. This page is also split into two section.

The profile form on the left hand side which can be empty or an instance of *saved delivery information*. Using the **Update Button** at the bottom of the page will update the profile at any point instantly.

![Profile Form]()

If the site user has made an order using the logged in account, the previous orders will be displayed which are linked with the **Order History checkout confirm** html page as mentioned above in checkout confirm features. Only the first 7 digits of the order number are visible for each previous order and **clickable** to view them in full detail. If the orders exceed a certain amount, the order history turns into a scrollable list for better visual looks followed by a **Shop Again** button to return the user to the product page. 

![Profile Order History]()

When displayed on smaller screen, the profile form is shown first followed by the Order History section.

### 11. **AllAuth Form Pages**

All of the allauth form pages are designed and styled **almost identically** for better user experience. Buttons are styled identically again to keep the overall UX design style.

**Sign Up Page**

The user is asked to enter their **email twice** followed by a **username** and **password**. Email is **required** for **account features** such as *changing password and sending confirmation email* to a verified email address. Of course looking at it from a user's point of view, they may click here by mistake so a **click here** is created at the top of the form which is liked with the ***log in page***.

The new user only needs to provide a username and a strong password which is validated through AllAuth.

![Sign up page]()

**Log In Page**

Given the fields required to sign up, the user is asked to enter their **email or username** followed by their **password**. From a user's perspective, incase they clicked on this tab instead of *Register*, a **sign up now** link is displayed for the user that they can click to be directed to the *Sign Up Page*.

The **Remember Me** feature is available to the user to *tick* so that their log in details are saved to improve their future booking experience. 

The **Sign In** button logs the user in and the *nav bar elements* displayed change accordingly.

![Log in page]()

**Log Out Page**

Once the user is logged in, the **LogOut** nav element comes available to them. However, rather than this function being a once click option, when the user clicks on the log out element, it directs them to the log out page where it is double checked before proceeding with this feature. 

A **cancel** link is displayed to the user if they have changed their or if they clicked on this option by mistake. It redirects the user back to the home page. 

However, if the user wishes to continue, they just have to simply click on the styled **Sign Out Button**.

![Log out page]()

The **rest of the AllAuth html pages** have also been *custom designed* to maintain the overall theme in terms of style and color.

### 12. **AllAuth Admin Panel**

The developer of this website created a nav bar element called **Admin** which only appears if the user logged in is the superuser (manager). This element is linked with Django's admin panel through which the manager is granted all of the CRUD functionality of all custom applications created as well as allauth's **user model**. They are given the ability to return to the website at any point through the link in the top right corner.

![Admin panel page]()

### **Toasts**

Toasts have been set up as includes in templates folder to display four types of toasts in the top right hand corner. **Success**, **Warning**, **Info** and **Error**. Every action taken by any user on Golf Mania's web application is displayed using toasts to ensure every site user is kept up to date of their actions. 

## Features (new ideas) 

Given that this is the very first e-commerce project developed by the author, he discovered lots of new potential features/ideas which could be implmeneted into this project to make it more appealing, attractive and interactive from a site user's perspective in future updates. 

- Using Django AllAuth, *include social account log in options* from sites like Facebook, Instagram and Twitter using each site's developer's api keys.

- For now, reviews can only be added using the admin panel and displayed on the index page. However, **reviews** should become a **foreign key to specific products** which could be displayed as part of the product_detail html page. *Trustpilot reviews* can replace custom reviews *in index.html*. Site user's should then be given permission to access a product *review form to fill in* and await approval by the manager or validate externally.

- Include an **image gallery** of five images for each product in product_details.html.

- Add a section in index.html which focuses on providing information regarding buying second hand clubs given that the main aim of Golf Mania is to sell **new** and **used** products. This could include an image and an **external link** to a *useful* site. 

- Expand the products model to **include quality** and hand type options too which requires further update to all aspects of the app. For example, when adding to the basket, does it exist there already etc. 

- For now, only enough products were added to the database to be able to demonstrate the functionality of the overall application but the number of products can also be expanded substanstially as well as category types, brands.

- Include a **clothing** dropdown list given that *size selection feature* is already included which can be used for clothing. 

- The **signup newsletter** within the footer has been set up with mailchimp but no actual emails are sent to signed up users yet. This can be set up in the near future. 

- Create an **Instagram and Twitter pages** for Golf Mania.

- For now, products can be purchased unlimited. However, when quantity of products are limited i.e. may only have one used driver, the **quantity of a product should be set** and minus any purchases so when it reaches zero, the specific product can longer be sold again to prevent **over-buying** products.

## 3. Testing and Bugs Fixed/Unfixed 

Golf Mania E-Commerce Web manual and automated testing has been broken down into several stages, given its complexity, length and reliance on a database and deployment.

#### **Validator Testing**

Validation testing for this project include HTML, CSS, Javascript and Python code validation. 

**Validating HTML Pages**

[https://validator.w3.org/](https://validator.w3.org/) is used to test all html files and their code to ensure high coding standards. Base.html is not tested given that the following html pages would not work without it and the content within the base.html is displayed correctly.

All of the testing below was done through the source code of each page on the **deployed** version of the project.

**index.html**

![index.html validation]()

**products.html**

![products.html validation]()

**product_detail.html**

![product_detail.html validation]()

**basket.html**

![basket.html validation]()

**checkout.html**

![checkout.html validation]()

**checkout_confirm.html**

![checkout_confirm.html validation]()

**add_product.html**

![add_product.html validation]()

**profile.html**

![profile.html validation]()

**update_product.html**

![update_product.html validation]()

**delete_product.html**

![delete_product.html validation]()

**signup.html**

![signup.html validation]()

**login.html**

![login.html validation]()

**logout.html**

![logout.html validation]()

**Validating CSS file**

[https://validator.w3.org/](https://jigsaw.w3.org/css-validator/) is used to test CSS files and their code to ensure high coding standards.

**static/css/base.css**

![static/css/base.css validation]()

**profiles/static/css/profile.css**

![profiles/static/css/profile.css validation]()

**checkout/static/css/checkout.css**

![checkout/static/css/checkout.css validation]()

**Validating JavaScript file**

[https://jshint.com/](https://jshint.com/) is used to test js files and their code to ensure high coding standards.

**profiles/static/js/countryoption.js**

![profiles/static/js/countryoption.js validation]()

**checkout/static/js/stripe_elements.js**

![checkout/static/js/stripe_elements.js validation]()

**base.html JS File**

![base.html JS File validation]()

**add_product/update_product.html JS File**

![add_product/update_product.html JS File validation]()

**product_detail.html JS File**

![product_detail.html JS File validation]()

**products.html JS File**

![products.html JS File validation]()

**quantity_input_js.html JS File**

![quantity_input_js.html JS File validation]()

**basket.html JS File**

![basket.html JS File validation]()

**Validating Python files**

[http://pep8online.com/](http://pep8online.com/) is used to test Python files and their code to ensure high coding standards.

1. #### reviews Application

Testing every custom python file within this application.

**admin.py**

![admin.py validation]()

**models.py**

![models.py validation]()

**urls.py**

![urls.py validation]()

**views.py**

![views.py validation]()

2. #### profiles Application

Testing every custom python file within this application.

**admin.py**

![admin.py validation]()

**forms.py**

![forms.py validation]()

**models.py**

![models.py validation]()

**test_forms.py**

![test_forms.py validation]()

**test_urls.py**

![test_urls.py validation]()

**urls.py**

![urls.py validation]()

**views.py**

![views.py validation]()

3. #### products Application

Testing every custom python file within this application.

**admin.py**

![admin.py validation]()

**forms.py**

![forms.py validation]()

**models.py**

![models.py validation]()

**test_forms.py**

![test_forms.py validation]()

**test_urls.py**

![test_urls.py validation]()

**urls.py**

![urls.py validation]()

**views.py**

![views.py validation]()

**widgets.py**

![widgets.py validation]()

4. #### home Application

Testing every custom python file within this application.

**test_urls.py**

![test_urls.py validation]()

**urls.py**

![urls.py validation]()

**views.py**

![views.py validation]()

5. #### checkout Application

Testing every custom python file within this application.

**admin.py**

![admin.py validation]()

**apps.py**

![apps.py validation]()

**forms.py**

![forms.py validation]()

**models.py**

![models.py validation]()

**signals.py**

![signals.py validation]()

**test_forms.py**

![test_forms.py validation]()

**test_urls.py**

![test_urls.py validation]()

**urls.py**

![urls.py validation]()

**views.py**

![views.py validation]()

**webhooks.py**

![webhooks.py validation]()

**webhook_handler.py**

![webhook_handler.py validation]()

6. #### basket Application

Testing every custom python file within this application.

**basket_tools.py**

![basket_tools.py validation]()

**contexts.py**

![contexts.py validation]()

**test_urls.py**

![test_urls.py validation]()

**urls.py**

![urls.py validation]()

**views.py**

![views.py validation]()

7. #### golfmania main Application

**settings.py**

![settings.py validation]()

**urls.py**

![urls.py validation]()

**wsgi.py**

![wsgi.py validation]()

**custom_storages.py**

![custom_storages.py validation]()

**Light-house Report**

Within DevTools, the lighthouse report is used to test overall performance of the website.

Performance has been categorised and is the only element not above 90% given that some of the images take much longer to load given their size i.e. main landing image which is essential to be good quality and big to attract new site visitors.

**Landing Page**

![Light-house Report landing page](static/images/devtools-report-landing_page.html.png "Light-house Report landing page")

**Products Page**

![Light-house Report Products page]( "Light-house Report Products page")

**Product Detail Page**

![Light-house Report Product Detail page]( "Light-house Report Product Detail page")

**Basket Page**

![Light-house Report Basket page]( "Light-house Report Basket page")

**Checkout Page**

![Light-house Report Checkout page]( "Light-house Report Checkout page")

**Checkout Confirm Page**

![Light-house Report Checkout Confirm page]( "Light-house Report Checkout Confirm page")

**Add Product Page**

![Light-house Report Add Product page]( "Light-house Report Add Product page")

**Update Product Page**

![Light-house Report Update Product page]( "Light-house Report Update Product page")

**Delete Product Page**

![Light-house Report Delete Product page]( "Light-house Report Delete Product page")

**Profile Page**

![Light-house Report Profile Page]( "Light-house Report Profile Page")

**Register Page**

![Light-house Report Register Page]( "Light-house Report Register Page")

**Log In Page**

![Light-house Report Log In page]( "Light-house Report Log In page")

**Log Out Page**

![Light-house Report Log Out page]( "Light-house Report Log Out page")

### **Testing colour contrast**

[Coolors.co/palette](https://coolors.co/palette/004b23-006400-007200-008000-38b000-70e000-9ef01a-ccff33) site was used to chose the color theme for the project as it provides a set of colors which work well together and the contrast perfect.

![Coolors color theme]( "Coolors color theme")

### **Search Engine Testing**

This project was tested through three several search engines including Google Chrome which is the creator's default search engine. Internet Explorer was not included below given its lack of popularity. 

1. **Google Chrome (default)**

2. **Mozilla Firefox**

Each section displayed as a page was tested and checked through ***Mozilla Firefox*** and no issues detected.

**Landing Page**

![Mozilla Firefox landing page](static/images/devtools-report-landing_page.html.png "Mozilla Firefox landing page")

**Products Page**

![Mozilla Firefox Products page]( "Mozilla Firefox Products page")

**Product Detail Page**

![Mozilla Firefox Product Detail page]( "Mozilla Firefox Product Detail page")

**Basket Page**

![Mozilla Firefox Basket page]( "Mozilla Firefox Basket page")

**Checkout Page**

![Mozilla Firefox Checkout page]( "Mozilla Firefox Checkout page")

**Checkout Confirm Page**

![Mozilla Firefox Checkout Confirm page]( "Mozilla Firefox Checkout Confirm page")

**Add Product Page**

![Mozilla Firefox Add Product page]( "Mozilla Firefox Add Product page")

**Update Product Page**

![Mozilla Firefox Update Product page]( "Mozilla Firefox Update Product page")

**Delete Product Page**

![Mozilla Firefox Delete Product page]( "Mozilla Firefox Delete Product page")

**Profile Page**

![Mozilla Firefox Profile Page]( "Mozilla Firefox Profile Page")

**Register Page**

![Mozilla Firefox Register Page]( "Mozilla Firefox Register Page")

**Log In Page**

![Mozilla Firefox Log In page]( "Mozilla Firefox Log In page")

**Log Out Page**

![Mozilla Firefox Log Out page]( "Mozilla Firefox Log Out page")

**Admin Page**

![Mozilla Firefox Admin Page]( "Mozilla Firefox Admin Page")

3. **Microsoft Edge**

Each section displayed as a page was tested and checked through ***Microsoft Edge*** and no issues detected.

**Landing Page**

![Microsoft Edge landing page](static/images/devtools-report-landing_page.html.png "Microsoft Edge landing page")

**Products Page**

![Microsoft Edge Products page]( "Microsoft Edge Products page")

**Product Detail Page**

![Microsoft Edge Product Detail page]( "Microsoft Edge Product Detail page")

**Basket Page**

![Microsoft Edge Basket page]( "Microsoft Edge Basket page")

**Checkout Page**

![Microsoft Edge Checkout page]( "Microsoft Edge Checkout page")

**Checkout Confirm Page**

![Microsoft Edge Checkout Confirm page]( "Microsoft Edge Checkout Confirm page")

**Add Product Page**

![Microsoft Edge Add Product page]( "Microsoft Edge Add Product page")

**Update Product Page**

![Microsoft Edge Update Product page]( "Microsoft Edge Update Product page")

**Delete Product Page**

![Microsoft Edge Delete Product page]( "Microsoft Edge Delete Product page")

**Profile Page**

![Microsoft Edge Profile Page]( "Microsoft Edge Profile Page")

**Register Page**

![Microsoft Edge Register Page]( "Microsoft Edge Register Page")

**Log In Page**

![Microsoft Edge Log In page]( "Microsoft Edge Log In page")

**Log Out Page**

![Microsoft Edge Log Out page]( "Microsoft Edge Log Out page")

**Admin Page**

![Microsoft Edge Admin page]( "Microsoft Edge Admin page")

### **Application Features Test**

#### **Automated Testing**

Some automated testing has been completed on this project. This website consists of **six** separate applications. Within **5** of these, files **urls.py** and **forms.py** have been tested and overall, **18** automated tests are running error free.

**1. profiles application**

**test_forms.py**: **One** automated tests running successfully to test for correct number of errors (required fields) come back when no data is submitted. 

**test_urls.py**: **Two** automated tests running successfully to check CRUD functionality url paths created for profile view function.

**2. products application**

**test_forms.py**: **One** automated tests running successfully to test for correct number of errors (required fields) come back when no data is submitted. 

**test_urls.py**: **Four** automated tests running successfully to check ALL CRUD functionality url paths for all products app view functions.

**3. home application**

**test_urls.py**: **One** automated tests running successfully to check if index.html is rendered.

**4. checkout application**

**test_forms.py**: **One** automated tests running successfully to test for correct number of errors (required fields in checkout form) come back when no data is submitted. 

**test_urls.py**: **Four** automated tests running successfully to check ALL CRUD functionality url paths for checkout app.

**5. basket application**

**test_urls.py**: **Four** automated tests running successfully to check ALL CRUD functionality url paths for basket views urls.

![Screenshot of 18 automated tests running successfully]()

#### **Manual Testing**

While the developer is fully aware of the advantages of full automated testing, he made a decisions to test the rest of the project manually in detail as result of the **upcoming due date**.

### **1. index.html features**
### **2. products.html features**
### **3. product_detail.html features**
### **4. basket.html features**
### **5. checkout.html features**
### **6. checkout_confirm.html features**
### **7. add_product.html features**
### **8. update_product.html features**
### **9. delete_product.html features**
### **10. profile.html features**
### **11. signup.html features**
### **12. login.html features**
### **13. logout.html features**
