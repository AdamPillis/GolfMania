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

**Signed In as Site User**

Once the user signs in, the two buttons are replaced with an **My Account** and *icon* which acts as a dropdown list for more features such as viewing and creating **My Profile**. *My* is used as it is from a user's point of view. 

1. **Home**
2. **Logout**
3. **My Profile**
4. **My Bookings**

![Header Logged In As Site User]()


### 2. **Products Page**
### 3. **Product Detail Page**
### 4. **Basket Page**
### 5. **Checkout Page**
### 6. **Checkout Confirm Page**
### 7. **Landing Page**
### 8. **Add Product Page**
### 9. **Update Product Page**
### 10. **Delete Product Page**
### 11. **Profile Page**
### 12. **AllAuth Form Pages**