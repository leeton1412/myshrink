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

  // select box on register
   // $(document).ready(function(){
  //  $('select').formSelect();
//  });