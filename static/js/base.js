// Wait for site to load before initiating js
$(document).ready(function () {
    
    $('#scroll-top').click(function () {
        window.scrollTo(0, 0);
    });

    window.onscroll = function () {
        if (pageYOffset >= 300) {
            $('.scroll-top-button').fadeIn(500);
        } else {
            $('.scroll-top-button').fadeOut(500);
        }
    };
});