
console.log("Custom JavaScript loaded!");

document.addEventListener("DOMContentLoaded", function() {
    const backToTopBtn = document.getElementById("btnBackToTop");
  
    if (backToTopBtn) {
      backToTopBtn.addEventListener("click", function() {
        window.scrollTo({
          top: 0,
          behavior: "smooth"
        });
      });
    }
  });
  
