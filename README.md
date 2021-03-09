# MyShrink - A Site Designed To Easily Manage Shrink

![Responsive screen grab of homepage](static/assets/responsive-screen-shot.png)

A website built to help people combine their friendships and competitive nature. 
The website will contain a javaScript based tournament system that can be used as a extra resource when friends gather together.

## Ease of use

Most current tournament based sites require registration and a fee. This site will build a bracket based on the amount of players and progress them on button click.
There is no need for any registration or fees as it is all client-side based. 

### Supported Brackets

The site currently supports:
* 2 players
* 4 players
* 8 players

Onclick events will trigger the amount of brackets to generate. Players will then enter their names into the brackets.
- ![Bracket before loading](assets/images/bracket-loads.jpg)



If the individual wins their match, clicking the icon next to their name will progress them through the brackets. It will alert() the winners name.
- ![After load and win](assets/images/new-win.jpg)

It can be used on all devices, but the site will alert() to state if the screen needs rotating.

Hosted on [GitHub Pages](https://leeton1412.github.io/bronament/)
Repository on [GitHub.com](https://github.com/leeton1412/bronament)

## License
>This project is created for everyone and is avaliable upon request [Bro-nament](https://github.com/leeton1412/bronament). 


## UX

### Goals

The aim of this website is to provide a quick, easy to use, and intuative system so friends can quickly build and play tournaments between each other

### Users

The predicted users of the site will be Friendship Groups, Tournament Organisers, Gaming Websites and Small Event Organisers.

### User Stories 
1. A group of friends looking to compete against each other in a tournament environment.
2. Tournament Organisers looking to create a more simplictic approach.
3. Tournament Organisers looking for a cheaper approach for smaller events.
4. Gaming websites looking to create articles on Esports.
5. A Small event Organiser looking to find a quick solution to an Esports competitive tournament setting.
6. Fans of Esports who wish to create their own brackets and predict player movement.

### Thoughts Behind The Design

The website colors and fonts are designed to give the page a dark intense feel. Having competed in Esports, the feeling of an intense atmosphere is something I can relate to.
I believe that this sort of feeling is important to give the site a competitive feeling.

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






    


