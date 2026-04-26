// ===== Mobile Nav Toggle =====
document.addEventListener('DOMContentLoaded', function () {
  const toggle = document.getElementById('navToggle');
  const nav = document.getElementById('mainNav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
    });
    // Close nav on link click
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('open');
      });
    });
  }

  // ===== WhatsApp Lead Form =====
  const form = document.getElementById('leadForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const name = document.getElementById('leadName').value.trim();
      const phone = document.getElementById('leadPhone').value.trim();
      const service = document.getElementById('leadService').value;
      if (!name || !phone || !service) {
        alert('Please fill all fields.');
        return;
      }
      const msg = encodeURIComponent(
        'Hello, I need PVC panel service.\nName: ' + name + '\nPhone: ' + phone + '\nService: ' + service
      );
      window.open('https://wa.me/919580659559?text=' + msg, '_blank');
    });
  }

  // ===== Gallery Lightbox =====
  const galleryImages = document.querySelectorAll('.gallery-grid img');
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxClose = document.getElementById('lightboxClose');

  if (galleryImages.length && lightbox) {
    galleryImages.forEach(function (img) {
      img.addEventListener('click', function () {
        lightboxImg.src = this.src;
        lightboxImg.alt = this.alt;
        lightbox.classList.add('active');
      });
    });
    lightboxClose.addEventListener('click', function () {
      lightbox.classList.remove('active');
    });
    lightbox.addEventListener('click', function (e) {
      if (e.target === lightbox) {
        lightbox.classList.remove('active');
      }
    });
  }
});
