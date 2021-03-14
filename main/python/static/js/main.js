/**
 * PROFILE SHOW / HIDE FUNCTION
 */
$(document).ready(function() {

    $("#friendlist").hide();
    $("#settings").hide();

    $("#show_friends").click(function() {
        $("#friendlist").show();
        $("#newslist").hide();
        $("#settings").hide();
    });
    $("#show_feed").click(function() {
        $("#newslist").show();
        $("#friendlist").hide();
        $("#settings").hide();
    });
    $("#show_settings").click(function() {
        $("#settings").show();
        $("#newslist").hide();
        $("#friendlist").hide();
    });
});
/**
 * / PROFILE SHOW / HIDE FUNCTION
 */


/**
 * GO TO TOP BUTTON FUNCTION
 */
var mybutton = document.getElementById("goTopButton");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block ";
    } else {
        mybutton.style.display = "none ";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
/**
 * / GO TO TOP BUTTON FUNCTION
 */

/**
 * NEWS SHOW / HIDE NEW POST FUNCTION
 */
$(document).ready(function() {

    $("#text_post").hide();
    $("#image_post").hide();
    $("#video_post").hide();

    $("#show_text_post").click(function() {
        $("#text_post").show();
        $("#image_post").hide();
        $("#video_post").hide();
    });
    $("#show_image_post").click(function() {
        $("#image_post").show();
        $("#text_post").hide();
        $("#video_post").hide();
    });
    $("#show_video_post").click(function() {
        $("#video_post").show();
        $("#image_post").hide();
        $("#text_post").hide();
    });
});
/**
 * / NEWS SHOW / HIDE NEW POST FUNCTION
 */