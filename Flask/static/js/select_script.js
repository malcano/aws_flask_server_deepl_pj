document.addEventListener('DOMContentLoaded', function() {
    var sm = 480;
    var md = 768;
  
    function resizeThis() {
      var imgH = document.querySelector('.middle img').width;
      if (window.innerWidth >= sm) {
        var elements = document.querySelectorAll('.left,.right,.section');
        for (var i = 0; i < elements.length; i++) {
          elements[i].style.height = imgH + 'px';
        }
      } else {
        var elements = document.querySelectorAll('.left,.right,.section');
        for (var i = 0; i < elements.length; i++) {
          elements[i].style.height = 'auto';
        }
      }
    }
  
    resizeThis();
  
    window.addEventListener('resize', function() {
      resizeThis();
    });
  
    window.addEventListener('scroll', function() {
      var sections = document.querySelectorAll('.section');
      for (var i = 0; i < sections.length; i++) {
        var elementPos = sections[i].offsetTop;
        var scrollPos = window.scrollY;
  
        var sectionH = sections[i].offsetHeight;
        var h = window.innerHeight;
        var sectionVert = ((h/2)-(sectionH/4));
  
        if ((elementPos - sectionVert) <= scrollPos && (elementPos - sectionVert) + sectionH > scrollPos) {
          sections[i].classList.add('animate');
        } else {
          sections[i].classList.remove('animate');
        }
      }
    });
  
    var buttons = document.querySelectorAll('.btn-primary');
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].addEventListener('click', function() {
        alert('I lied');
      });
    }
  
    var links = document.querySelectorAll('a[href*="#"]:not([href="#"])');
    for (var i = 0; i < links.length; i++) {
      links[i].addEventListener('click', function(e) {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
          var target = document.querySelector(this.hash);
          target = target.length ? target : document.querySelector('[name=' + this.hash.slice(1) +']');
          if (target) {
            e.preventDefault();
            window.scrollTo({
              top: target.offsetTop,
              behavior: 'smooth'
            });
          }
        }
      });
    }
  });
  