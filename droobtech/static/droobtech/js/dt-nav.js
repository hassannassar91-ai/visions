(function () {
  "use strict";

  var header = document.querySelector("[data-header]");
  var toggle = document.querySelector("[data-nav-toggle]");
  var mobileNav = document.querySelector("[data-mobile-nav]");
  var closeBtn = document.querySelector("[data-nav-close]");

  function setHeaderState() {
    if (!header) return;
    if (window.scrollY > 24) {
      header.classList.remove("dt-header-top");
      header.classList.add("dt-header-scrolled");
    } else {
      header.classList.add("dt-header-top");
      header.classList.remove("dt-header-scrolled");
    }
  }

  function openNav() {
    if (!mobileNav || !toggle) return;
    mobileNav.classList.remove("hidden");
    toggle.setAttribute("aria-expanded", "true");
    document.body.style.overflow = "hidden";
  }

  function closeNav() {
    if (!mobileNav || !toggle) return;
    mobileNav.classList.add("hidden");
    toggle.setAttribute("aria-expanded", "false");
    document.body.style.overflow = "";
  }

  if (toggle) toggle.addEventListener("click", openNav);
  if (closeBtn) closeBtn.addEventListener("click", closeNav);
  mobileNav && mobileNav.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", closeNav);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeNav();
  });

  window.addEventListener("scroll", setHeaderState, { passive: true });
  setHeaderState();
})();
