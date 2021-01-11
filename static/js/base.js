// Wait for site to load before initiating js
$(document).ready(function () {
    
    // A scroll to top function that appears as the user scrolls down the page to improve navigation
    $('#scroll-top').click(function () {
        window.scrollTo(0, 0);
    });

    window.onscroll = function () {
        if (pageYOffset >= 750) {
            $('.scroll-top-button').fadeIn(500);
        } else {
            $('.scroll-top-button').fadeOut(500);
        }
    };

    // Used to transform / add styling to category selections on home page when hovered over to improve UX.
    $(".category-image").hover(function transformCategoryImage() {
        $(this).css({ 'transform': 'scale(1.075)', 'transition': 'transform 400ms ease-in-out' });
        $(this).siblings('.category-friendly-name').css({ 'color': '#fff', 'transform': 'scale(1.075)', 'transition': 'transform 400ms ease-in-out'});
    }, function () {
        $(this).css({ 'transform': 'scale(1)', 'transition': 'transform 400ms ease-in-out' });
        $(this).siblings('.category-friendly-name').css({ 'color': '#000', 'transform': 'scale(1)', 'transition': 'transform 400ms ease-in-out' });
    });

    // Used to transform / add styling to product listings when hovered over to improve UX.
    $(".listing-card").hover(function transformListingImage() {
        $(this).children('.listing-image-container').children('.listing-image').css({ 'transform': 'scale(1.075)', 'transition': 'transform 400ms ease-in-out' });
        $(this).children('.listing-info').css({ 'color': '#fff',  'transition': 'transform 400ms ease-in-out' });
    }, function () {
        $(this).children('.listing-image-container').children('.listing-image').css({ 'transform': 'scale(1.0)', 'transition': 'transform 400ms ease-in-out' });
        $(this).children('.listing-info').css({ 'color': '#000',  'transition': 'transform 400ms ease-in-out' });
    });

    // Used to transform / add styling to featured products slider when hovered over to improve UX.
    $(".featured-listing-link").hover(function transformListingImage() {
        $(this).children('.featured-listing-image').css({ 'transform': 'scale(1.075)', 'transition': 'transform 400ms ease-in-out' });
        $(this).children('.featured-listing-info').css({ 'color': '#fff',  'transition': 'transform 400ms ease-in-out' });
    }, function () {
        $(this).children('.featured-listing-image').css({ 'transform': 'scale(1.0)', 'transition': 'transform 400ms ease-in-out' });
        $(this).children('.featured-listing-info').css({ 'color': '#000',  'transition': 'transform 400ms ease-in-out' });
    });

    /* Start of update quantity functions
    This series of functions can be used in combination with each other to update the quantity of an item in a basket 
    (the increment buttons can also be used on the product details page)
    The purpose of these functions is to allow a user to complete updates to item quantities in their basket before 
    the form is submitted and basket values updated.
    This also prevent multiple messages being displayed to a user re updated items.*/

    // Global variable that set when the update basket function runs on the basket page.
    let submitTimer

    // Used to allow user to increase the value of the quantity input boxes on product detail & basket pages for improved UX
    $('.increment-qty').click(function incrementQty() {
        let productId = $(this).data('item_id');
        let input = document.getElementById(`id_qty_${productId}`);
        let currentVal = parseInt(input.value);
        let maxVal = parseInt(input.getAttribute("max"));
        if (input.value < maxVal) {
            input.value = currentVal + 1;
        } else {
            input.value = maxVal;
        }
        if (submitTimer) {
            stopTimer()
        }
      updatebasket(productId);
    });

    // Used to allow user to decrease the value of the quantity input boxes on product detail & basket pages for improved UX
    $('.decrement-qty').click(function decrementQty() {
        let productId = $(this).data('item_id');
        let input = document.getElementById(`id_qty_${productId}`);
        let currentVal = parseInt(input.value);
        let minVal = parseInt(input.getAttribute("min"));
        if (input.value > minVal ) {
            input.value = currentVal - 1;
        } else {
            input.value = 1;
        }
        if (submitTimer) {
            stopTimer()
        }
        updatebasket(productId);
    });

    /* https://stackoverflow.com/questions/19966417/prevent-typing-non-numeric-in-input-type-number
    Used to prevent input of non numeric chars in quanitity input boxes. */
    $(".qty_input").keypress(function (evt) {
        if (evt.which < 48 || evt.which > 57)
        {
            evt.preventDefault();
        }
    });

    // Used to allow user to manually update the quantity input boxes on product detail & basket pages for improved UX
    $(".qty_input").keyup(function(){
        let productId = $(this).data('item_id');
        let input = document.getElementById(`id_qty_${productId}`);
        let currentVal = parseInt(input.value);
        let minVal = parseInt(input.getAttribute("min"));
        let maxVal = parseInt(input.getAttribute("max"));
        if (input.value < minVal ) {
            input.value = 1;
        } else if (input.value > maxVal ){
            input.value = 99;
        } else {
            input.value = input.value
        }
        if (submitTimer) {
            stopTimer()
        }
        updatebasket(productId);
    });

    // function to get the basket quantity form and submit the form, delayed by a 1 second timer (when on the basket page only).
    function updatebasket(productId) {
        if (window.location.pathname == "/basket/") {
            let form = document.getElementById(`basket-qty-update-form_${productId}`);
            submitTimer = setTimeout(function(){ 
                form.submit();
            }, 1000);
        }
    }

    // function to clear any existing timeout to prevent the form being submitted too early.
    function stopTimer() {
        clearTimeout(submitTimer);
    }
    // End of update quantity functions
});


    