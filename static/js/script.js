// Sticky Nav on Scroll
window.onscroll = function() {stickynav()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function stickynav() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky-nav")
  } else {
    navbar.classList.remove("sticky-nav");
  }
}
 
 //Materialize Jquery
$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        autoClose: true,
        showClearBtn: true,
        });
    $('select').formSelect()
    $('.collapsible').collapsible();
  });

window.onscroll = function() {stickynav()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

// Float toggle
function floatToggle(){
    var action = document.querySelector('.float');
    action.classList.toggle('active')

}

// Emailjs

function sendMail(contactForm){
    emailjs.send("shrink", "shrink", {
        "from_name": contactForm.first_name.value,
        "from_email": contactForm.email.value,
        "suggestion_idea": contactForm.message.value,
    })
    .then(
        function(){
            alert('Thank You')
            var form = document.getElementById("myForm")
            form.reset();    
        
        },
        
        function(){
            alert('Your email could not be sent at this time')
        }
    )
 return false; 

}