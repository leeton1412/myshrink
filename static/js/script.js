  //Materialize Jquery
$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.datepicker').datepicker();
    $('select').formSelect({
        format: "dd mmmm, yyyy",
        autoClose: true,
        showClearBtn: true,
        i18n:{
            done: "select"
        }
    });
  });

  // select box on register
   // $(document).ready(function(){
  //  $('select').formSelect();
//  });