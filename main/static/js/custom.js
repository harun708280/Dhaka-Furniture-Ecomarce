(function() {
    'use strict';

    // Plus button click handler
    $(".plus-cart").on('click touchstart', function(event) {
        var cartId = $(this).data("cart-id");
        $.ajax({
            type: "GET",
            url: "/plus_cart",
            data: {
                cart_id: cartId,
            },
            success: function(data) {
                updateCart(data);
            },
        });
    });

    // Minus button click handler
    $(".minus-cart").on('click touchstart', function(event) {
        var cartId = $(this).data("cart-id");
        $.ajax({
            type: "GET",
            url: "/minus_cart",
            data: {
                cart_id: cartId,
            },
            success: function(data) {
                updateCart(data);
            },
        });
    });

    // Function to update cart quantities and totals
    function updateCart(data) {
        var cartId = data.cart_id;
        $("#quantity-" + cartId).text(data.quantity);
        // Update other elements as needed
    }
})();
