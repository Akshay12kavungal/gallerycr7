document.addEventListener("DOMContentLoaded", function () {
  // Toggle responsive menu
  var menuToggle = document.getElementById("menuToggle");
  var responsiveMenu = document.getElementById("responsiveMenu");

  menuToggle.addEventListener("click", function () {
    responsiveMenu.classList.toggle("show");
  });

  // Close responsive menu on outside click
  document.addEventListener("click", function (event) {
    if (
      !event.target.matches("#menuToggle") &&
      !event.target.matches(".responsive-menu") &&
      !event.target.matches(".responsive-menu a")
    ) {
      responsiveMenu.classList.remove("show");
    }
  });

  // Close responsive menu on resize (if open)
  window.addEventListener("resize", function () {
    if (window.innerWidth > 768 && responsiveMenu.classList.contains("show")) {
      responsiveMenu.classList.remove("show");
    }
  });
});
