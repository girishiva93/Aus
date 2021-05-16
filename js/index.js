const navBarBrand = document.querySelector(".navbar-brand");

var width,height;
window.onresize = window.onload = function() {
    width = this.innerWidth;
    height = this.innerHeight;
    if (width <= 992) {
        navBarBrand.innerHTML = "Logo";
    } else {
        navBarBrand.innerHTML = "";
    }
}