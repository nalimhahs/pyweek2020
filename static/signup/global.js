
$(document).ready(function(){
   
    
    $("#log_link").click(function(){
        $(this).css({"backgroundColor":"rgba(225, 225, 225, 0.2)"})
        $("#reg_link").css({"backgroundColor":"rgb(0,0,0"})
        $("#registration_form").css({"display":"none"})
        $("#login_form").fadeIn(500)
    })
    $("#reg_link").click(function(){
        $(this).css({"backgroundColor":"rgba(255, 255, 255, 0.2)"})
        $("#log_link").css({"backgroundColor":"rgb(0,0,0"})
        $("#login_form").css({"display":"none"})
        $("#registration_form").fadeIn(500)
    })
    $("#log_link").mouseover(function(){
        $(this).css({"backgroundColor":"rgba(225, 225, 225, 0.2)"})
        $("#reg_link").css({"backgroundColor":"rgb(0,0,0"})
    })
   
    $("#reg_link").mouseover(function(){
        $(this).css({"backgroundColor":"rgba(225, 225, 225, 0.2)"})
        $("#log_link").css({"backgroundColor":"rgb(0,0,0"})
    })
})