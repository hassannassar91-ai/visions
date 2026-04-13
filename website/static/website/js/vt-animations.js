(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function initReveal() {
    var nodes = document.querySelectorAll(".vt-reveal");
    if (!nodes.length) return;

    if (reduceMotion) {
      nodes.forEach(function (el) {
        el.classList.add("vt-reveal--visible");
      });
      return;
    }

    nodes.forEach(function (el) {
      var d = parseInt(el.getAttribute("data-reveal-delay") || "0", 10);
      if (d) el.style.setProperty("--vt-delay", d + "ms");
    });

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("vt-reveal--visible");
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -6% 0px", threshold: 0.06 }
    );

    nodes.forEach(function (el) {
      observer.observe(el);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initReveal);
  } else {
    initReveal();
  }
})();
