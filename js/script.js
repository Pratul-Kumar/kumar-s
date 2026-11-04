    (function() {
      'use strict';
      document.body.classList.add('page-ready');

      var els = document.querySelectorAll('.fade-in');
      if (!('IntersectionObserver' in window)) {
        for (var i = 0; i < els.length; i++) els[i].classList.add('visible');
        return;
      }
      var observer = new IntersectionObserver(function(entries) {
        for (var i = 0; i < entries.length; i++) {
          if (entries[i].isIntersecting) {
            entries[i].target.classList.add('visible');
            observer.unobserve(entries[i].target);
          }
        }
      }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });
      for (var i = 0; i < els.length; i++) observer.observe(els[i]);
    })();
