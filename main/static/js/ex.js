$(document).ready(function() {
    // Add to cart button click handler
    $(".add-to-cart-btn").on('click', function(event) {
        var productId = $(this).data("product-id");
        $.ajax({
            type: "GET",
            url: "/add-to-cart/",
            data: {
                prod_id: productId,
                product_quantity: 1,
            },
            success: function(data) {
                alert('Product added to cart!');
            },
            error: function(xhr, textStatus, errorThrown) {
                alert('Error adding product to cart');
            }
        });
    });
});
