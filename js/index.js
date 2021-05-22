const counters = document.querySelectorAll('.count');

counters.forEach(counter => {
  counter.innerHTML = '0';

  const updateCounter = () => {
    const target = +counter.getAttribute('data-target');
    const c = +counter.innerHTML;

    const increment = target / 200;

    if(c < target) {
      counter.innerText = `${Math.ceil(c + increment)}`;
      setTimeout(updateCounter, 3);
    } else{
      counter.innerText = target;
    }
  };

  updateCounter();
})

var swiper = new Swiper('.blog-section .slider', {
  spaceBetween:30,
  effect: 'fade',
  loop: true,
  mousewheel:{
    invert:false,
  },
  pagination:{
    el: '.slider-pagination',
    clickable:true,
  }
});

/* Logos section */
$(document).ready(function(){
  $('.customer-logos').slick({
      slidesToShow: 6,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 1500,
      arrows: false,
      dots: false,
      pauseOnHover: false,
      responsive: [{
          breakpoint: 768,
          settings: {
              slidesToShow: 4
          }
      }, {
          breakpoint: 520,
          settings: {
              slidesToShow: 3
          }
      }]
  });
});