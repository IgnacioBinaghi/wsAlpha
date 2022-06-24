$(document).ready(function(){
  $('#open').click(function(){
    $('.container').css("opacity","1");
    $('.container').css("pointer-events","auto");
  });
  $('.login1 span').click(function(){
    $('.container').css("opacity","0");
    $('.container').css("pointer-events","none");
  });
  $('#submit').click(function(){
    $('#email').remove();
    alert("Thanks For Subscribing!");
    $("#submit").remove();
  });
});
