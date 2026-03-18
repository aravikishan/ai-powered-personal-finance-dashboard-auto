// Navigation Interactions
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelectorAll('nav a');

navToggle.addEventListener('click', () => {
  document.body.classList.toggle('nav-open');
});

navLinks.forEach(link => {
  link.addEventListener('click', () => {
    document.body.classList.remove('nav-open');
  });
});

// Smooth Scrolling
const smoothScroll = (target, duration) => {
  const targetPosition = target.getBoundingClientRect().top;
  const startPosition = window.pageYOffset;
  const startTime = null;

  const ease = (t, b, c, d) => {
    t /= d / 2;
    if (t < 1) return c / 2 * t * t + b;
    t--;
    return -c / 2 * (t * (t - 2) - 1) + b;
  };

  const animation = currentTime => {
    if (startTime === null) startTime = currentTime;
    const timeElapsed = currentTime - startTime;
    const run = ease(timeElapsed, startPosition, targetPosition, duration);
    window.scrollTo(0, run);
    if (timeElapsed < duration) requestAnimationFrame(animation);
  };

  requestAnimationFrame(animation);
};

const scrollToSection = document.querySelectorAll('.scroll-to');

scrollToSection.forEach(link => {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    const targetId = this.getAttribute('href');
    const target = document.querySelector(targetId);
    smoothScroll(target, 1000);
  });
});

// Dynamic Content Loading
async function loadContent(url, container) {
  try {
    const response = await fetch(url);
    const content = await response.text();
    document.querySelector(container).innerHTML = content;
  } catch (error) {
    console.error('Error loading content:', error);
  }
}

// Example usage: loadContent('/api/transactions', '#transactions-container');