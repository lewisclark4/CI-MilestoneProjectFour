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

    $('.increment-qty').click(function incrementQty() {
        let productId = $(this).data('item_id')
        let input = document.getElementById(`id_qty_${productId}`);
        let currentVal = parseInt(input.value);
        let maxVal = parseInt(input.getAttribute("max"));
        if (input.value < maxVal) {
        input.value = currentVal + 1;
        } else {
        input.value = maxVal;
      }
    })

    $('.decrement-qty').click(function decrementQty() {
        let productId = $(this).data('item_id')
        let input = document.getElementById(`id_qty_${productId}`);
        let currentVal = parseInt(input.value);
        if (input.value >= 2) {
        input.value = currentVal - 1;
        } else {
        input.value = 1;
        }
    })
});