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

var swiper = new Swiper('.slider', {
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