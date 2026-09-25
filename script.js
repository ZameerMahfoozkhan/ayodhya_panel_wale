// ===== PVC Panel Wale - Production Client Script =====
document.addEventListener('DOMContentLoaded', function () {
  'use strict';

  // ===== 1. Mobile Navigation Toggle =====
  const toggle = document.getElementById('navToggle');
  const nav = document.getElementById('mainNav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      const isOpen = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Close nav on any navigation link click
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });

    // Close nav when clicking outside on mobile
    document.addEventListener('click', function (e) {
      if (nav.classList.contains('open') && !nav.contains(e.target) && !toggle.contains(e.target)) {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // ===== 2. WhatsApp Lead Form Validation & Submission =====
  const form = document.getElementById('leadForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const nameEl = document.getElementById('leadName');
      const phoneEl = document.getElementById('leadPhone');
      const serviceEl = document.getElementById('leadService');

      const name = nameEl ? nameEl.value.trim() : '';
      const phone = phoneEl ? phoneEl.value.trim() : '';
      const service = serviceEl ? serviceEl.value.trim() : '';

      if (!name || !phone || !service) {
        alert('Please fill out all required fields.');
        return;
      }

      // Input Validation: Phone must be at least 10 digits
      const digitsOnly = phone.replace(/[^0-9]/g, '');
      if (digitsOnly.length < 10) {
        alert('Please enter a valid 10-digit mobile number.');
        if (phoneEl) phoneEl.focus();
        return;
      }

      // Safe URL encoding for WhatsApp API
      const msg = encodeURIComponent(
        'Hello PVC Panel Wale,\nI would like an estimate / site visit.\nName: ' + name + '\nPhone: ' + phone + '\nService: ' + service
      );
      window.open('https://wa.me/919580659559?text=' + msg, '_blank', 'noopener,noreferrer');
    });
  }

  // ===== 3. Gallery Lightbox with Accessibility & Scroll Lock =====
  const galleryImages = document.querySelectorAll('.gallery-grid img');
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxClose = document.getElementById('lightboxClose');

  if (galleryImages.length > 0 && lightbox && lightboxImg) {
    function openLightbox(src, alt) {
      lightboxImg.src = src;
      lightboxImg.alt = alt || 'Interior Installation Preview';
      lightbox.classList.add('active');
      lightbox.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
      lightbox.classList.remove('active');
      lightbox.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      lightboxImg.src = '';
    }

    galleryImages.forEach(function (img) {
      img.style.cursor = 'pointer';
      img.addEventListener('click', function () {
        openLightbox(this.src, this.alt);
      });
      // Allow keyboard activation (Enter key)
      img.setAttribute('tabindex', '0');
      img.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') {
          openLightbox(this.src, this.alt);
        }
      });
    });

    if (lightboxClose) {
      lightboxClose.addEventListener('click', closeLightbox);
    }

    lightbox.addEventListener('click', function (e) {
      if (e.target === lightbox) {
        closeLightbox();
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && lightbox.classList.contains('active')) {
        closeLightbox();
      }
    });
  }
});
