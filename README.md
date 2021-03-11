# MyShrink - A Site Designed To Easily Manage Shrink

![Responsive screen grab of homepage](static/assets/responsive-screen-shot.png)

A website built to help managers in Tesco bridge their skill gap with Shrink. 
The website will be powered by a Mongodb that contains the inputed shrink from the managers.

## Ease of use

Really looking after your shrink can be challenging for many managers. This is due to a skill gap between being able to use Tesco SBO system and
being able to adequetly track it. The site will have registered members log in and enter the shrink manually. It will then be submitted to a Mongodb
that will be able to be edited, deleted, searched and added to. 

### Supported Departments

The site currently supports:
* GM
* FRESH FOOD
* PRODUCE

A Duty Manager will visted the app in the morning and log in. After this they will enter the top lines for the store into the database via the app
- ![Add Shrink Page](static/assets/user-shrink.png)



After this the user will be redirected to the Home page where they can Edit if entered inncorrectly.
- ![Home Page Edit](static/assets/user-home.png)

Any Manager can log on to view their own shrink and from here they can also edit, delete and resolve shrink issues.
- ![Profile Page for Managers Shrink](static/assets/user-profile.png)

A Manager can also visit the search function which will enable them to search for more shrink if they wish to see additional information.
- ![Search Page](static/assets/user-search.png)

It can be used on all devices.

Hosted on [GitHub Pages](https://leeton1412.github.io/bronament/)
Repository on [GitHub.com](https://github.com/leeton1412/bronament)

## License
>This project is created for Tesco and is avaliable upon request [MyShrink](https://github.com/leeton1412/myshrink). 

## Database Design

### Which Database?

The choice I have made for the Database is [MongoDB](https://www.mongodb.com/3). The simple nature of it means that easy interaction is very much achievable which is the sites main aim.
Though was put into using MySQL but with MongoDB large amounts of information can be stored and easily manipulate. Simplicity is the key in bridging the skill gap.
Python3 will be used to call the functions. 

### Database structure

For this project I decided that i would use 3 Databases.
- shrinkDB
    - This is the main database where information for all shrink is stored.
- shrinkDb
    - This Database is mainly used to store the Departments to make sure a accurate department is selected making it easier to manipulate the database to what I need.
        The Database name does need to be changed at a later date but due to time restrictions i was unable to obtain this
- userDB
    - This Database will be used to store user credentials. With this I will be able to generate the correct information needed for the specific Team Manager

## UX

### Goals

The aim of this website is to provide a quick, easy to use, and intuative system so managers can quickly view their shrink

### Users

The predicted users of the site will be Managers, Area Directors, Colleagues and Depots.

### User Stories 
1. Managers looking to view their shrink to see what needs investigating.
2. Area Managers looking for a quick and accurate view of a stores shrink level.
3. Colleagues looking to take a bigger role within their store.
4. Depots looking for a more store driving view to help assist them with the performance management.
5. Managers looking to find out what theyve done for shrink before their performance reviews.

### Thoughts Behind The Design

- ![Inform Screen Grab](static/assets/inform.jpg)
The app is designed using Materialize to help comply to good UX design. The colors are chosen to match those of similar apps
avaliable to Tesco colleagues to try give a familiar feel to it, namly Inform

### Colors and theme of the website.

Materialize Easy to Use color scheme is used throughout to give a clean feel to the page.

* Blue Darken-1:   ![#1e88e5](https://via.placeholder.com/15/1e88e5/1e88e5)
* Light Blue:   ![#94929b](https://via.placeholder.com/15/03a9f4/03a9f4)
* Red Lighten -1: ![#ef5350](https://via.placeholder.com/15/ef5350/ef5350)

### Font Choices 
Header font throughout the website are chosen to obtain a clean look:

    *font-family: 'Rajdhani', sans-serif;

Elements such as paragraphs are a complementing font:

    *font-family: 'Noto Sans', sans-serif;

### WireFrames 

Here you can see screen shots of the Wire Frames. Due to time restrictions, there could of been more detail involved such as added images.

- ![WireFrame](static/assets/wire-1.png) ![WireFrame](static/assets/wire-2.png) ![WireFrame](static/assets/wire-3.png) ![WireFrame](static/assets/wire-4.png)
   ![WireFrame](static/assets/wire-5.png) ![WireFrame](static/assets/wire-6.png) 

## Features 

- Easy Navigation.
- Use of external Database to create easy interaction [MongoDB](https://www.mongodb.com/3)
- Hover affects on certain icons.
- GoogleMaps Javascript API to show store location.
- Shrink Add Section supporting 3 Departments.
- Auto Response email through Email.js
- Delete Shrink function only avalible to users logged in to ensure data remains safe.
- Edit Shrink function incase of miss entered information
- Links to other Tesco Apps that colleagues often find hard to find. 
- Float Button to help navigate the page to the most important sections easier.
- Alerts for users login and log out. Also for shrink being added and deleted.
- Login functionallity putting a user in session. 
- ERegistration functionallity registering the user to the database.
- Search Function to allow managers to search and delete all shrink. As this information is sensitive.
- Profile page displaying that users specific Shrink items.
- Live contact form using [Emailjs](https://www.emailjs.com).
- Collapsible Nav bar using Materialize.
- Collapisble cards from Materialize containing information on how to use the site and what shrink is.
- Responsive Mobile first design.
- [Materialize](https://materializecss.com/getting-started.html) 
    - CSS class utilites
    - Grid system
    - Layout Change
    - Input form

### Features Still to Include 

Due to limitations with current personal circumstances and Covid-19, the time I spent on this project did not give me the required time to implement every thing at launch. 

- More Department support
    - Currently the site only supports 3 departments. Ideally this would cover the whole of the store 
- More Search Functionality.
    - Original design did not include this, but it has become clear on testing that more search options would make a better user experience. 
- Multi-Store Support
    - Currently only one store is supported at launch. Ive multiple stores used the app information would be hard to read and understand 
    - Another Key Field could be added to help redefine the what information is displayed
    - Create a way to fill player names in randomly to ensure brackets are fair and random 
- Shrink Next-Step Form
    - Feedback I have been given is that a shrink next step form could be very beneficial as we could track what managers are doing following meetings.



### Technologies Used:

Technologies used in the making of this page are:

- [HTML](https://www.w3schools.com/whatis/whatis_html.asp)
    - Used to structure the site. 
- [CSS](https://www.w3schools.com/whatis/whatis_css.asp)
    - Used to style the website. 
- [Javascript](https://www.w3schools.com/js/DEFAULT.asp)
    - Used for GoogleMaps, Float Button, and live contact form on contact.html. 
- [Jquery](https://jquery.com/download/)
    - Used to initialize a varity of functions from Materialize 
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - Used to help create the app and communicate with Jinja
- [Pymongo](https://pymongo.readthedocs.io/en/stable/)
    - Used to interact between python and MongoDB
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
    - Used to create the registration page and salt the users password for protection
- [Google Chrome](https://www.google.com/chrome/)
    - Used to inspect the website via dev tools.
- [Google](http://www.google.com)
    - Used to conduct searches
- [Python3]
    - Used to for most functionallity on the site for example, calling the database. 
- [Emailjs](https://www.emailjs.com/docs/)
    - Used to create a live contact form.
- [Materialize](https://materializecss.com/getting-started.html)
    - Used to create a great UX design that is mobile responsive.
- [GoogleMaps Api](https://developers.google.com/maps/documentation/javascript/get-api-key)
    - Used to create a Map image in the footer showing the location of the store.
- [CDN.js](https://cdnjs.com/)
    - Used to import different plugins.
- [Gitpod](https://www.gitpod.io/)
    - Used to build the website.
- [GitHub](https://github.com/)
    - Used for Repository.
- [Gitpages](https://pages.github.com/)
    - Used to Host the website. 
- [Am I Responsive?](http://ami.responsivedesign.is/)
    - Used to check the responsive design of the website.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    - Used to loop through information from the database and display it accurately.

## Personal Testing
## User Testing

The site was tested by users and software. It has been tested on Google Chrome v83.0.4103.97 and Mozilla Firefox v77.0.1 (64) on Acer Ryzen 5 and also 
a desktop PC. It has also been tested on Ipad Pro, Samsung Galaxy s9, Iphone 11 pro.

### Jack Bailey

Jack was asked to test the page and to feed back on any problems that he encountered or for any feed back he might have. Test was carried out on iphone 10 & a Acer Laptop
- Problems Encountered 
    - Gallery page displayed a scroll bar on screens sized 414 x 736.
        - Issue was due to a container problem but has been changed.
    - On mobile banner is very large when rotated.
        - This issue has been changed.
    - Back-ground of menu items on toggle makes it hard to read
        - This is a valid point and is being changed

- Feed Back. 
    - Syntax Error with text on Index.html
        - Syntax wording did not match with flow of page.
        - The text has now been corrected. 

### Ben Palmby

Ben was asked to test the page and to feed back on any problems that he encountered or for any feed back he might have. 
- Problems Encountered.
    - Index.html text would not fit on screens 750 and above.
        - Media Query has been added to change this.

### [Laura Sawyn](https://www.linkedin.com/in/laura-sawyn-628757178/)

Laura was asked to give feedback on the layout of the page.
- Feed Back.
    - Index.html text would not fit on screens 750 and above.
        - Media Query has been added to change this.
    - Facebook Link view takes to a personal page not a Group page.
        - Group page is being created to answer this problem.
    - Linkedin Link is not working.
        - This is an issue with LinkedIn and is being investigated.
    - Create an Alert for contact page to know it has been sent.
        - This has now been implemented.
    - Spelling across the pages is incorrect.
        - This is being looked into and a full spellcheck is being carried out.



## Technologies used for testing.

### [W3c Markup Validation](https://validator.w3.org/)

Used to look for any potential problems.
- Problems.
    - Various syntax errors. All fixed.
    - Semi-colons missing on tournament.js
    - Anchor tags having a button as a descendant. Issue is fixed.
    

## [Am I Responsive?](http://ami.responsivedesign.is/)

This website was used to check the layout on various screen sizes. 
- Problems
    - inde.html text doesnt fit to page on screen size 768 x 1024.
        - This problem has been fixed.

### Deployment

The website is hosted on [GitHub Pages](https://leeton1412.github.io/bronament/)

The process:
- Host a git repository on Github.
- In the settings for the repository scroll down till Github Pages section.
- Select which Branch you would like in source section. (Normally Master Branch)
- Change the address of your website if required 
- Save changes. 
- The page is now ready to be viewed.
- The generic page set up will be 'yourusername'.github.io/'thereponame'

## Credits

### Content 

- All images from this website are obtained from [Unsplash](https://unsplash.com/)

- Game information is obtained via [WikipediaAPI](https://www.mediawiki.org/wiki/API:Main_page). 

- Nav bar basic structure obtained from [CodePen](https://codepen.io/ericagulto/full/KgdyqJ/).

- Footer basic structure obatined from [MDbootstrap](https://mdbootstrap.com/docs/jquery/navigation/footer/).

- Hover and Landing.html affects obtained from [Animista](https://animista.net/) and [Hover.css](https://ianlunn.github.io/Hover/).

- Cors error corrected by using [Cors-anywhere](https://github.com/Rob--W/cors-anywhere/#documentation).

- Sounds are obtained using [101SoundBoards](https://www.101soundboards.com/boards/10441-street-fighter-ii-sounds)

### Acknowledgments 

- Thanks to Seun Owonikoko @seun_mentor.
- Stuart Crang for encouraging me to join the course.
- Callum Jackson for sharing his PHP knowledge with me to help me understand how to build the brackets in Javascript.
- Laura Sawyn for always supporting me through development. 
- My current Linkedin Group for continued help and motivation. 
- Code institute tutor support for always being available and willingness to support.  
- Code institute for providing me with the tools to chase my dreams. 






    


