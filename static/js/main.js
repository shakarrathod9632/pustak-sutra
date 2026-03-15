// // Main JavaScript file for Pustak Sutra

// // Wait for DOM to load
// document.addEventListener('DOMContentLoaded', function() {
    
//     // Initialize AOS (Animate On Scroll)
//     AOS.init({
//         duration: 1000,
//         once: true,
//         offset: 100
//     });
    
//     // Navbar scroll effect
//     const navbar = document.querySelector('.navbar-custom');
//     if (navbar) {
//         window.addEventListener('scroll', function() {
//             if (window.scrollY > 50) {
//                 navbar.classList.add('scrolled');
//             } else {
//                 navbar.classList.remove('scrolled');
//             }
//         });
//     }
    
//     // Initialize tooltips
//     var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
//     var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
//         return new bootstrap.Tooltip(tooltipTriggerEl);
//     });
    
//     // Smooth scroll for anchor links
//     document.querySelectorAll('a[href^="#"]').forEach(anchor => {
//         anchor.addEventListener('click', function (e) {
//             e.preventDefault();
//             const target = document.querySelector(this.getAttribute('href'));
//             if (target) {
//                 target.scrollIntoView({
//                     behavior: 'smooth',
//                     block: 'start'
//                 });
//             }
//         });
//     });
    
//     // Counter animation for stats
//     const counters = document.querySelectorAll('.stat-number');
//     if (counters.length > 0) {
//         counters.forEach(counter => {
//             const updateCount = () => {
//                 const target = +counter.getAttribute('data-target');
//                 const count = +counter.innerText;
//                 const increment = target / 100;
                
//                 if (count < target) {
//                     counter.innerText = Math.ceil(count + increment);
//                     setTimeout(updateCount, 10);
//                 } else {
//                     counter.innerText = target;
//                 }
//             };
            
//             // Check if element is in viewport
//             const observer = new IntersectionObserver((entries) => {
//                 entries.forEach(entry => {
//                     if (entry.isIntersecting) {
//                         updateCount();
//                         observer.unobserve(entry.target);
//                     }
//                 });
//             });
            
//             observer.observe(counter);
//         });
//     }
    
//     // Form validation
//     const forms = document.querySelectorAll('form');
//     forms.forEach(form => {
//         form.addEventListener('submit', function(e) {
//             if (!form.checkValidity()) {
//                 e.preventDefault();
//                 e.stopPropagation();
//             }
//             form.classList.add('was-validated');
//         });
//     });
// });