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
>This project is created for everyone and is avaliable upon request [Bro-nament](https://github.com/leeton1412/bronament). 


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

The app is designed using Materialize to elp comply to good UX design. The colors are chosen to match those of similar apps
avaliable to Tesco colleagues to try give a familiar feel to it.

### Colors and theme of the website.

* Revolver:   ![#333238](https://via.placeholder.com/15/333238/333238)
* Manatee:   ![#94929b](https://via.placeholder.com/15/94929b/94929b)
* Black: ![#000000](https://via.placeholder.com/15/000000/000000)
* Cloudy: ![#aba599](https://via.placeholder.com/15/413f3f/413f3f)

### Font Choices 
Header font throughout the website are chosen to mimic a Retro Gaming feel:

    *font-family: 'Monoton', cursive; 

Elements such as paragraphs are a complementing font and Bootstrap recommended:

    *font-family: 'Segoe UI', 'Source Sans Pro', 'Calibri', 'Candara', 'Arial', 'sans-serif';;

### WireFrames 

Here you can see screen shots of the Wire Frames. Due to time restrictions, there could of been more detail involved such as added images.

- ![WireFrame](assets/images/wire-frame-1.jpg) ![WireFrame](assets/images/wire-fram-2.jpg) ![WireFrame](assets/images/wire-frame-3.jpg) ![WireFrame](assets/images/wire-frame-4.jpg) 

## Features 

- Easy Navigation.
- Use of external css animation to create Flicker effect and Rotate effect [Animista](https://animista.net/)
- Hover affects on certain icons.
- Wikipedia API powered game information ensuring it stays relevant.
    - ![WikiApi](assets/images/wiki-api.jpg) ![WikiApi](assets/images/wikiapi-load.jpg)
- Tournament bracket supporting 2, 4 and 8 players.
- Auto Response email through Email.js
- Hover.css effect on Links.
- Links and information on other major tournament sites. 
- Alert to rota screens on lower widths.
- Win alerts when a player wins their match.
- Buttons to hide Wikipedia information so its not displayed on call. 
- Easy use of "button move" to provide clean client side experience.
- Countdown intro page using original Street fighter 2 sounds.
- Auto load on completion of Countdown.
- Live contact form using [Emailjs](https://www.emailjs.com).
- Social Media buttons to create more contact points .
- Extra content buttons.
- Responsive Mobile first design.
- [Bootstrap](https://getbootstrap.com/) 
    - HTML class utilites
    - Grid system
    - Layout Change
    - Input form

### Features Still to Include 

Due to limitations with current personal working arrangements and Covid-19, the time I spent on this project did not give me the required time to implement every thing at launch. 

- Toornament API
    - I have recieved premission to use [Toornament](https://www.toornament.com/en_US/) API. This will create a much better user experience and a useable server. 
- Personal Tournament Data.
    - No current knowledge on servers. Would like to save the information for each user to create a league. 
    - Register the amount of wins each player has
- Brackets
    - Create a better design for the input forms. 
    - Create a input field by using Javascript onclick to remove the need to hide brackets
    - Create a way to fill player names in randomly to ensure brackets are fair and random
    - Better design in javaScript to shorten code for other developers.
    - Auto fill names in player input bars using Toornament API
    - Find away to display brackets portrait on Mobile Phones
    - Link brackets together so people can see their progression clearly. 
    - Support for more player sizes by including Bye Weeks. 
- Countdown
    - Find a way to play sounds without user permission. Sounds will only currently play if allowed in settings.



### Technologies Used:

Technologies used in the making of this page are:

- [HTML](https://www.w3schools.com/whatis/whatis_html.asp)
    - Used to structure the site. 
- [CSS](https://www.w3schools.com/whatis/whatis_css.asp)
    - Used to style the website. 
- [Javascript](https://www.w3schools.com/js/DEFAULT.asp)
    - Used for Count Down on index.html, Game information on landing.html, Tournament movement and bracket building in tournament.html, and live contact form on contact.html. 
- [Jquery](https://jquery.com/download/)
    - Used to create brackets for Tournament.html
- [Google Chrome](https://www.google.com/chrome/)
    - Used to inspect the website via dev tools.
- [Google](http://www.google.com)
    - Used to conduct searches
- [Hover.css](https://ianlunn.github.io/Hover/)
    - Used to add effects to links. 
- [Cors-anywhere](https://github.com/Rob--W/cors-anywhere/#documentation)
    - Used to get passed CORS error
- [Animista](https://animista.net/)
    - Used to display effects on Landing page and Tournament page..
- [Codepen](https://codepen.io/ericagulto/full/KgdyqJ/)
    - Used to create a simple header and footer.
- [Emailjs](https://www.emailjs.com/docs/)
    - Used to create a live contact form.
- [Bootstrap 4](https://getbootstrap.com/)
    - Used for helping create a mobile responsive website. 
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
- [Befunky](https://www.befunky.com/)
    - Used to resize all images on the website.

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






    


