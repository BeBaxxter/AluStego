/**
 * PROFILE SHOW / HIDE FUNCTION
 */
function profile_selection() {
    $(document).ready(function() {

        $("#friendlist").hide();
        $("#settings").hide();

        $("#show_friends").click(function() {
            $("#friendlist").show();
            $("#feedlist").hide();
            $("#settings").hide();
        });
        $("#show_feed").click(function() {
            $("#feedlist").show();
            $("#friendlist").hide();
            $("#settings").hide();
        });
        $("#show_settings").click(function() {
            $("#settings").show();
            $("#feedlist").hide();
            $("#friendlist").hide();
        });
    });
}

/**
 * FEED SHOW / HIDE NEW POST FUNCTION
 */
function feed_selection() {
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
}

/**
 * AUTH SHOW / HIDE FUNCTION
 */
function auth_selection() {
    $(document).ready(function() {

        $("#login").show();
        $("#register").hide();
        $("#pwv").hide();

        $("#show_login").click(function() {
            $("#login").show();
            $("#register").hide();
            $("#pwv").hide();

        });
        $("#show_register").click(function() {
            $("#register").show();
            $("#login").hide();
            $("#pwv").hide();

        });
        $("#show_pwv").click(function() {
            $("#pwv").show();
            $("#login").hide();
            $("#register").hide();

        });
    });
}

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