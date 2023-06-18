$(document).ready(function() {
  $(".product-img").click(function() {
    var index = $(this).data("index");
    $("#carouselExampleIndicators").carousel(index);

    $(".product-img").removeClass("active").css("opacity", "0.5");
    $(this).addClass("active").css("opacity", "1");
  });
});