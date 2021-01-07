// Wait for site to load before initiating js
$(document).ready(function () {
    

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

    $(".category-image").hover(function transformCategoryImage() {
        $(this).css({ 'transform': 'scale(1.075)', 'transition': 'transform 400ms ease-in-out' });
        $(this).siblings('.category-friendly-name').css({ 'color': '#fff', 'transform': 'scale(1.075)', 'transition': 'transform 400ms ease-in-out'});
    }, function () {
        $(this).css({ 'transform': 'scale(1)', 'transition': 'transform 400ms ease-in-out' });
        $(this).siblings('.category-friendly-name').css({ 'color': '#000', 'transform': 'scale(1)', 'transition': 'transform 400ms ease-in-out' });
    });

    $(".listing-card").hover(function transformListingImage() {
        $(this).children('.listing-image-container').children('.listing-image').css({ 'transform': 'scale(1.075)', 'transition': 'transform 400ms ease-in-out' });
        $(this).children('.listing-info').css({ 'color': '#fff',  'transition': 'transform 400ms ease-in-out' });
    }, function () {
        $(this).children('.listing-image-container').children('.listing-image').css({ 'transform': 'scale(1.0)', 'transition': 'transform 400ms ease-in-out' });
        $(this).children('.listing-info').css({ 'color': '#000',  'transition': 'transform 400ms ease-in-out' });
    });

    $(".featured-listing-link").hover(function transformListingImage() {
        $(this).children('.featured-listing-image').css({ 'transform': 'scale(1.075)', 'transition': 'transform 400ms ease-in-out' });
        $(this).children('.featured-listing-info').css({ 'color': '#fff',  'transition': 'transform 400ms ease-in-out' });
    }, function () {
        $(this).children('.featured-listing-image').css({ 'transform': 'scale(1.0)', 'transition': 'transform 400ms ease-in-out' });
        $(this).children('.featured-listing-info').css({ 'color': '#000',  'transition': 'transform 400ms ease-in-out' });
    });

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
      updatebasket(productId);
    });

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
        updatebasket(productId);
    });

    function updatebasket(productId) {
        let form = document.getElementById(`basket-qty-update-form_${productId}`);
        if (window.location.pathname == "/basket/") {
            form.submit();
        }
    }
   
});


    