$(document).ready(function(){

  $('#open').click(function(){
    $('.container').css("opacity","1");
    $('.container').css("pointer-events","auto");
  });

  $('.login1 span').click(function(){
    $('.container').css("opacity","0");
    $('.container').css("pointer-events","none");
  });

  $('#submit_subscription').click(function(){
//    $('#email').remove();
//    $("#submit").remove();
    alert("Thanks For Subscribing!");
  });

  $('#submit_unsubscription').click(function(){
//    $('#email').remove();
//    $("#submit").remove();
    alert("We're sorry your had to unsubcribe!");
  });

});
