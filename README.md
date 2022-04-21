<h1 align="center">Biltong Shop</h1>

[Biltong Shop - Heroku App](https://ci-ms4-biltong-shop.herokuapp.com/)

This is a biltong boutique store selling biltong and anything related to biltong.

<h2 align="center">
<img src="https://www.touristsecrets.com/wp-content/uploads/2019/07/Jerky-Moist-Dried-Meat-Biltong-Protein-Food-Beef-2794787-1-1024x683.jpg" alt="Cut Biltong" height="300px">
<img src="https://tastykitchen.com/recipes/wp-content/uploads/sites/2/2011/11/blog-biltong1-410x272.jpg" alt="Biltong Sticks" height="300px">
</h2>

<h4 id="layout">Layout:</h4>

1. [User Experience (UX)](#ux)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Credits](#credits)

<h2 id="ux">User Experience (UX)</h2>

[Layout](#layout)
-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find products.

    -   #### Returning Visitor Goals (New Shopper)

        1. As a Returning Visitor, I want to easily be able to make a purchase without an account.
        2. As a Returning Visitor, I want to easily be able to register an account as a shopper to make it easier the next time I return to the site.
        3. As a Returning Visitor, I want to be able to see some recipes for making biltong.

    -   #### Frequent User Goals (Shopper)
        1. As a Frequent User, I want to log into the site and see my current orders.
        2. As a Frequent User, I want to quickly search for and select the items for purchase.
        3. As a Frequent User, I want to manage my account easily.
        4. As a Frequent User, I want to read, add, and edit my product reviews.
    
    -   #### Site Administrator Goals (Owner)
        1. As a Site Administrator, I want to log into the site and manage my products in the store.
        2. As a Site Administrator, I want to read, add, and edit all product reviews.

-   ### Design
    -   #### Colour Scheme
        -   Dark theme with '#222' as the main dark tone
        -   The contrast tone is a bright green-yellow to highlight buttons and calls to action elements.
    -   #### Typography
        -   The Lato font is the main font used throughout the whole website with Sans Serif as the fallback font in case the font isn't being imported into the site correctly. XXX is a clean font used frequently in programming, so it is both attractive and appropriate.
    -   #### Imagery
        -   Imagery is important. The large, background hero image is designed to be striking and catch the user's attention. The image will provide a quick understanding to site visitors as to the purpose of the site.

*   ### Wireframes

    -   [Lo-Fi layout](https://raw.githubusercontent.com/greggo58/CI-MS4-biltong-shop/main/wireframes/Biltong-shop-wireframe.png)

<h2 id="features">Features</h2>

[Layout](#layout)
-   Responsive for all device sizes
-   Interactive elements
-   CRUD operations with a database

### Data Schema
- ACCOUNTS (AllAuth)
    - Email addresses
- AUTHENTICATION AND AUTHORIZATION (AllAuth)
    - Groups
    - Users
- CHECKOUT app
    - Orders
        - User profile (Foreign Key from Users)
- INSTRUCTIONS app
    - Recipies
- PRODUCTS app
    - Categories
    - Products
        - Category (Foreign Key from Categories)
    - Reviews
        - User profile (Foreign Key from Users)

<h2 id="technologies-used">Technologies Used</h2>

[Layout](#layout)
### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
2. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
3. [Bulma:](https://bulma.io/)
    - Bulma was used as some starter CSS templates
4. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
5. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
6. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
8. [Django:](https://www.djangoproject.com/)
    - Django is the main framework used to build the website application efficiently.
9. [Amazon Web Services (S3):](https://aws.amazon.com/s3/)
    - AWS S3 was used to store static and media files in a bucket and serve them to Heroku
10. [Heroku:](https://dashboard.heroku.com/)
    - Heroku was used to deploy the app and receive updates from GitHub repository
11. [Stripe (Card Payments)](https://stripe.com/en-gb)
    - Stripe was used in managing the payments and card verifications and the use of webhooks
12. [Gmail](https://mail.google.com/)
    - Gmail was used to set up a SMTP host point for Django

<h2 id="testing">Testing</h2>

[Layout](#layout)

Markup Validators from W3C Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Full pass
-   [W3C HTML Validator - Home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-biltong-shop.herokuapp.com%2F)
    - Errors related to li element tags in nav element ignored. Used for Bootstrap CSS.
    - Duplicate id occurrence ignored. Required for mobile top header switch.
-   [W3C HTML Validator - Products](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-biltong-shop.herokuapp.com%2Fproducts%2F)
    - Errors related to li element tags in nav element ignored. Used for Bootstrap CSS.
    - Duplicate id occurrence ignored. Required for mobile top header switch.
-   [W3C HTML Validator - Product Details](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-biltong-shop.herokuapp.com%2Fproducts%2F7%2F)
    - Errors related to li element tags in nav element ignored. Used for Bootstrap CSS.
    - Duplicate id occurrence ignored. Required for mobile top header switch.
-   [W3C HTML Validator - Instructions](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-biltong-shop.herokuapp.com%2Finstructions%2F)
    - Errors related to li element tags in nav element ignored. Used for Bootstrap CSS.
    - Duplicate id occurrence ignored. Required for mobile top header switch.
-   [W3C HTML Validator - Add Product](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-biltong-shop.herokuapp.com%2Fproducts%2Fadd%2F)
    - Errors related to li element tags in nav element ignored. Used for Bootstrap CSS.
    - Duplicate id occurrence ignored. Required for mobile top header switch.
-   [W3C HTML Validator - Profile](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-biltong-shop.herokuapp.com%2Fprofile%2F)
    - Errors related to li element tags in nav element ignored. Used for Bootstrap CSS.
    - Duplicate id occurrence ignored. Required for mobile top header switch.
-   [W3C HTML Validator - Accounts Logout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-biltong-shop.herokuapp.com%2Faccounts%2Flogout%2F)
    - Errors related to li element tags in nav element ignored. Used for Bootstrap CSS.
    - Duplicate id occurrence ignored. Required for mobile top header switch.
-   [W3C HTML Validator - Accounts SignUp](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-biltong-shop.herokuapp.com%2Faccounts%2Fsignup%2F)
    - Errors related to li element tags in nav element ignored. Used for Bootstrap CSS.
    - Duplicate id occurrence ignored. Required for mobile top header switch.
-   [W3C HTML Validator - Accounts Login](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-biltong-shop.herokuapp.com%2Faccounts%2Flogin%2F)
    - Errors related to li element tags in nav element ignored. Used for Bootstrap CSS.
    - Duplicate id occurrence ignored. Required for mobile top header switch.
-   [W3C HTML Validator - Recipe Add](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-biltong-shop.herokuapp.com%2Finstructions%2Fadd%2F)
    - Errors related to li element tags in nav element ignored. Used for Bootstrap CSS.
    - Duplicate id occurrence ignored. Required for mobile top header switch.
-   [W3C HTML Validator - Recipe Edit](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-biltong-shop.herokuapp.com%2Finstructions%2Fedit%2F2%2F)
    - Errors related to li element tags in nav element ignored. Used for Bootstrap CSS.
    - Duplicate id occurrence ignored. Required for mobile top header switch.

### Testing User Stories from the User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site.
        - As a First Time Visitor, I immediately see the large hero image and can understand the theme and purpose of the site
    2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find products.
        - As a First Time Visitor, I can see the labels and buttons very clearly and understand the purpose of the links and what will happen if I click on them.

-   #### Returning Visitor Goals (New Shopper)

    1. As a Returning Visitor, I want to easily be able to make a purchase without an account.
        - As a Returning Visitor, I see that I can make a purchase by just filling out some basic contact information and my card details for payment. I understand that to improve my convenience I would need an account to have a profile that prefills this information for me.
        - As a Returning Visitor, I can easily see my shopping bag total on all screens and the shopping subtotals at checkout.
        - As a Returning Visitor, I receive confirmation emails on my purchase orders letting me know that my purchase has gone through successfully.
    2. As a Returning Visitor, I want to easily be able to register an account as a shopper to make it easier the next time I return to the site.
        - As a Returning Visitor, I can register an account easily to store an order history, contact information, and prefill the checkout form before payment.
    3. As a First Time Visitor, I want to be able to see some recipes for making biltong.
        - As a Returning Visitor, I can easily find the recipes / instructions on how to make biltong.

-   #### Frequent User Goals (Shopper)
    1. As a Frequent User, I want to log into the site and see my current orders.
        - As a Frequent User, I can use the navigation to get to my profile and see my order history.
        - As a Frequent User, I can access my bag to see what I have added and adjust / remove the items very quickly.
    2. As a Frequent User, I want to quickly search for and select the items for purchase.
        - As a Frequent User, I can use the pre-built navigation as product filters to easily narrow the choices for selection.
        - As a Frequent User, I can sort the products by various means to see products of my interest first.
        - As a Frequent User, I can manually search for products I know by name or have a specific word or keyphrase in the description.
    3. As a Frequent User, I want to manage my account easily.
        - As a Frequent User, I can navigate to my profile to adjust my contact information.
    4. As a Frequent User, I want to read, add, and edit my product reviews.
        - As a Frequent User, I can open a product to see the details and add my review (if I haven't added one already), edit my review (if one exists), or delete my review (if one exists).

-   #### Site Administrator Goals (Owner)
    1. As a Site Administrator, I want to log into the site and manage my products in the store.
        - As a Site Administrator, I can log into the site and use the Product Management link to add new products or edit / delete products as I see them on the site using the convenient links that only site admins can see.
    2. As a Site Administrator, I can open a product to see the details and add my review (if I haven't added one already), edit any reviews (if any exist), or delete any reviews (if any exist).

### Further Testing

-   The Website was tested on Google Chrome, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, Android Smartphone, Apple iPhone.
-   A large amount of testing was done to ensure that all pages were linking correctly and the data binding was functioning correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   An issue with custom clearable file input dumping a 500 server error. This was removed from products/forms.py for now.

<h2 id="deployment">Deployment</h2>

[Layout](#layout)
### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not the top of the page), locate the "Settings" button on the menu.
    - Alternatively, click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not the top of the page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

### Heroku

[Heroku - Github Integration](https://devcenter.heroku.com/articles/github-integration)

#### **Enabling GitHub Integration**
You can configure GitHub integration in the **Deploy** tab of apps in the [Heroku Dashboard](https://dashboard.heroku.com/).

<img src="https://devcenter1.assets.heroku.com/article-images/2349-imported-1443570588-2349-imported-1443555058-421-original.jpg">

To configure GitHub integration, you have to authenticate with GitHub. You only have to do this once per Heroku account.

>GitHub repo admin access is required for you to configure automatic GitHub deploys. This is because Heroku has to register a service hook on the GitHub repo, and this action requires admin access. For GitHub organisations, your GitHub account will also need to be a member of the organisation and not an outside collaborator.

>If your repo is in a GitHub organization that has third-party application restrictions enabled, an organization admin needs to approve Heroku for use with the organization. More details are available on GitHub.

After you link your Heroku app to a GitHub repo, you can selectively deploy from branches or configure auto-deploys.

If you do not have any apps, you must approve integration for your organization from GitHub. For more information about this process, see Approving OAth Apps for your organization.

#### **Manual Deploys**
With manual deploys, you can create an immediate deployment of any branch from the GitHub repo that’s connected to your app. Use manual deploys if you want to control when changes are deployed to Heroku.

<img src="https://devcenter1.assets.heroku.com/article-images/2349-imported-1443570589-2349-imported-1443555058-422-original.jpg">

You can also use manual deploys to temporarily deploy a branch other than the one that’s configured for automatic deployment. For example, you might have a development app synced to the **development** GitHub branch, but you temporarily want to test a feature branch. Simply trigger a manual deploy of the feature branch to test it on the Heroku app. Note that the release of the feature branch is overwritten on the next successful GitHub push to the **development** branch.

#### **Automatic Deploys**
When you enable automatic deploys for a GitHub branch, Heroku builds and deploys all pushes to that branch. If, for example, you have a development app on Heroku, you can configure pushes to your GitHub development branch to be automatically built and deployed to that app.

<img src="https://devcenter3.assets.heroku.com/article-images/2349-imported-1443570589-2349-imported-1443555058-423-original.jpg">

If you’ve configured your GitHub repo to use automated Continuous Integration (with Travis CI, for example), you can check the “Wait for CI to pass before deploy” checkbox. When enabled, Heroku will only auto-deploy after all the commit statuses of the relevant commit show **success**.

This commit won’t auto-deploy because one of the checks shows a **pending** status:<img src="https://devcenter3.assets.heroku.com/article-images/1516299367-Screen-Shot-2018-01-18-at-9.35.09-AM.png">

This commit will auto-deploy because all of the checks show a status of success:<img src="https://devcenter0.assets.heroku.com/article-images/1516299538-Screen-Shot-2018-01-18-at-10.12.16-AM.png">

#### **Review Apps**
With review apps enabled for a Heroku app, Heroku will create temporary test apps for each pull request that’s opened on the GitHub repo that’s connected to the parent app. Review apps are great if you’re using [GitHub Flow](https://guides.github.com/introduction/flow/) to propose, discuss, and merge changes to your codebase. Because pull request branches are deployed to new apps on Heroku, it’s very simple for you and your collaborators to test and debug code branches. You can also run automated integration tests on the Heroku app representing a GitHub branch.

See the [Review apps article](https://devcenter.heroku.com/articles/github-integration-review-apps) for details.

#### **Heroku CI**
Once you’ve connected your GitHub repo to your Pipeline, you can turn on Heroku CI, our visual, low-configuration test runner that integrates easily with Heroku Pipelines (and so complements Review apps, existing Heroku apps, and our GitHub integrations). Any Heroku Pipeline is already Heroku CI ready – just turn it on in the Pipeline’s Settings tab.

#### **Links to Diffs**
For apps that are linked to GitHub repos, releases in the Dashboard Activity tab will include a “View Diff” link. Following the link will take you to the GitHub comparison view, showing the changes made since the last release.

<img src="https://devcenter0.assets.heroku.com/article-images/2349-imported-1443570590-2349-imported-1443555059-411-original.jpg">

#### **Disconnecting from GitHub**
Disconnecting Individual Apps
Individual apps can be disconnected in the GitHub pane of the **Deploy** tab for the app.

<img src="https://devcenter3.assets.heroku.com/article-images/2349-imported-1443570591-2349-imported-1443555059-434-original.jpg">

#### **Disconnecting Account**
You can disconnect your Heroku and GitHub accounts in the [Applications pane on your Dashboard account page](https://dashboard.heroku.com/account/applications#third-party-applications).

<img src="https://devcenter2.assets.heroku.com/article-images/1576871458-Screen-Shot-on-2019-12-20-at-11-50-08.png">

<h2 id="credits">Credits</h2>

[Layout](#layout)
### Code

-   All content was written by the developer based on the tutorials.

### Content


-   Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

### Media

-   Media files are used from the creative commons license photos.
-   If any files are considered not creative commons or the status changes, please let me know so I may remove them.

### Acknowledgements

-   Friends and family for their support and help.
