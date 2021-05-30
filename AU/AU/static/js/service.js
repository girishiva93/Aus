   // owl carousel js start
   $(document).ready(function () {
    $(".owl-carousel").owlCarousel({
      loop: true,
      margin:20,
      autoplay: true,
      animateIn: "fadeIn",
      animateOut: "fadeOut",
      responsiveClass: true,
      pagination: false,
      dots: false,
      responsive: {
        0: {
          items: 1.01,
        },
        600: {
          items: 3,
        },
        1000: {
          items: 8,
        },
      },
    });
      // Custom Button
    $(".my-next-button").click(function() {
        owl.trigger("next.owl.carousel");
    });
    $(".my-previous-button").click(function() {
        owl.trigger("prev.owl.carousel");
    });
  });
  // owl carousel js end