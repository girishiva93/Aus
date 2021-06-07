const counters = document.querySelectorAll('.count');
const counterSection = document.querySelector('.counter-section');

function Counter(){
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
        counter.innerText = target + "+";
      }
    };
  
    updateCounter();
  })
}

ScrollTrigger.create({
  trigger:counterSection,
  onEnter:Counter
})

/* Blog section */
var swiper = new Swiper('.blog-slider', {
  spaceBetween:30,
  effect: 'fade',
  loop: true,
  autoplay:true,
  mousewheel:{
    invert:false,
  },
  pagination:{
    el: '.blog-slider__pagination',
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

/*Testimonial slider*/
$('#tes-area').owlCarousel({
  singleItem:true,
  transitionStyle:'fadeUp',
  mouseDrag: false,
  touchDrag:false,
  autoPlay: 3000,
  pagination: true
})

// pop up 
window.onload = function() {
  document.getElementById('button').onclick = function() {
    document.getElementById('modalOverlay').style.display = 'none'
  };
};
