// Faithful Homeschool Haven Web Application
// Christ-centered Single Page Application with smooth navigation

class FaithfulHomeschoolHavenApp {
  constructor() {
    this.currentSection = 'home';
    this.init();
  }

  init() {
    this.setupEventListeners();
    this.setupNavigation();
    this.setupForms();
    this.setupBlogFilters();
    this.showSection('home');
  }

  setupEventListeners() {
    // Mobile navigation toggle
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    if (navToggle && navMenu) {
      navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
      });
    }

    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
      if (navMenu && navToggle && 
          !navMenu.contains(e.target) && 
          !navToggle.contains(e.target)) {
        navMenu.classList.remove('active');
        navToggle.classList.remove('active');
      }
    });

    // Handle window resize
    window.addEventListener('resize', () => {
      if (window.innerWidth > 768) {
        navMenu?.classList.remove('active');
        navToggle?.classList.remove('active');
      }
    });
  }

  setupNavigation() {
    // Handle all navigation links
    document.addEventListener('click', (e) => {
      const target = e.target;
      
      // Check if clicked element has data-section attribute
      const sectionTarget = target.getAttribute('data-section');
      if (sectionTarget) {
        e.preventDefault();
        this.showSection(sectionTarget);
        this.updateNavigation(sectionTarget);
        
        // Close mobile menu if open
        const navMenu = document.getElementById('navMenu');
        const navToggle = document.getElementById('navToggle');
        navMenu?.classList.remove('active');
        navToggle?.classList.remove('active');
        
        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    });

    // Handle direct hash navigation
    window.addEventListener('hashchange', () => {
      const hash = window.location.hash.slice(1);
      if (hash && this.isValidSection(hash)) {
        this.showSection(hash);
        this.updateNavigation(hash);
      }
    });

    // Handle initial hash on page load
    const initialHash = window.location.hash.slice(1);
    if (initialHash && this.isValidSection(initialHash)) {
      this.showSection(initialHash);
      this.updateNavigation(initialHash);
    }
  }

  setupForms() {
    // Newsletter forms
    const newsletterForms = document.querySelectorAll('#newsletterForm, #resourcesNewsletter');
    newsletterForms.forEach(form => {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        this.handleNewsletterSubmission(form);
      });
    });

    // Contact form
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
      contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        this.handleContactSubmission(contactForm);
      });
    }
  }

  setupBlogFilters() {
    const filterTags = document.querySelectorAll('.filter-tag');
    const blogPosts = document.querySelectorAll('.blog-post-card');

    filterTags.forEach(tag => {
      tag.addEventListener('click', () => {
        const category = tag.getAttribute('data-category');
        
        // Update active filter
        filterTags.forEach(t => t.classList.remove('active'));
        tag.classList.add('active');
        
        // Filter posts
        blogPosts.forEach(post => {
          const postCategory = post.getAttribute('data-category');
          if (category === 'all' || postCategory === category) {
            post.style.display = 'block';
          } else {
            post.style.display = 'none';
          }
        });
      });
    });
  }

  showSection(sectionId) {
    // Hide all sections
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
      section.classList.remove('active');
    });

    // Show target section
    const targetSection = document.getElementById(sectionId);
    if (targetSection) {
      targetSection.classList.add('active');
      this.currentSection = sectionId;
      
      // Update URL hash without triggering hashchange event
      if (history.pushState) {
        history.pushState(null, null, `#${sectionId}`);
      } else {
        window.location.hash = sectionId;
      }
    }
  }

  updateNavigation(sectionId) {
    // Update navigation active states
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('data-section') === sectionId) {
        link.classList.add('active');
      }
    });
  }

  isValidSection(sectionId) {
    const validSections = ['home', 'blog', 'services', 'about', 'resources', 'contact'];
    return validSections.includes(sectionId);
  }

  handleNewsletterSubmission(form) {
    const emailInput = form.querySelector('input[type="email"]');
    const submitButton = form.querySelector('button[type="submit"]');
    
    if (emailInput && submitButton) {
      const email = emailInput.value.trim();
      
      if (!this.isValidEmail(email)) {
        this.showFormMessage(form, 'Please enter a valid email address.', 'error');
        return;
      }
      
      // Simulate form submission
      const isMinistryButton = submitButton.textContent.includes('Ministry');
      submitButton.textContent = isMinistryButton ? 'Joining Ministry...' : 'Subscribing...';
      submitButton.disabled = true;
      
      setTimeout(() => {
        const successMessage = isMinistryButton ? 
          'Praise God! Welcome to our Christian homeschool family. Check your email for a special welcome gift!' :
          'Thank you for joining our ministry! Check your email for confirmation and your first Christian resource.';
        this.showFormMessage(form, successMessage, 'success');
        emailInput.value = '';
        submitButton.textContent = isMinistryButton ? 'Join Our Ministry' : 'Subscribe';
        submitButton.disabled = false;
      }, 1500);
    }
  }

  handleContactSubmission(form) {
    const submitButton = form.querySelector('button[type="submit"]');
    const formData = new FormData(form);
    
    // Basic validation
    const firstName = form.querySelector('#firstName').value.trim();
    const lastName = form.querySelector('#lastName').value.trim();
    const email = form.querySelector('#email').value.trim();
    const message = form.querySelector('#message').value.trim();
    const service = form.querySelector('#service').value;
    
    if (!firstName || !lastName || !email || !message) {
      this.showFormMessage(form, 'Please fill in all required fields.', 'error');
      return;
    }
    
    if (!this.isValidEmail(email)) {
      this.showFormMessage(form, 'Please enter a valid email address.', 'error');
      return;
    }
    
    // Simulate form submission
    const isPrayerRequest = service === 'prayer';
    submitButton.textContent = isPrayerRequest ? 'Submitting Prayer Request...' : 'Sending Ministry Request...';
    submitButton.disabled = true;
    
    setTimeout(() => {
      const successMessage = isPrayerRequest ? 
        'Thank you for sharing your prayer request. I will lift you and your family up in prayer and respond within 24-48 hours with encouragement from God\'s Word.' :
        'Praise God for your heart to serve Him through homeschooling! I will prayerfully respond to your ministry request within 24-48 hours.';
      this.showFormMessage(form, successMessage, 'success');
      form.reset();
      submitButton.textContent = 'Send Ministry Request';
      submitButton.disabled = false;
    }, 2000);
  }

  showFormMessage(form, message, type) {
    // Remove any existing message
    const existingMessage = form.querySelector('.form-message');
    if (existingMessage) {
      existingMessage.remove();
    }
    
    // Create new message element
    const messageEl = document.createElement('div');
    messageEl.className = `form-message ${type === 'error' ? 'error' : 'success'}`;
    messageEl.textContent = message;
    
    // Style the message
    messageEl.style.padding = 'var(--space-12) var(--space-16)';
    messageEl.style.borderRadius = 'var(--radius-base)';
    messageEl.style.marginTop = 'var(--space-16)';
    messageEl.style.fontSize = 'var(--font-size-sm)';
    messageEl.style.fontWeight = 'var(--font-weight-medium)';
    
    if (type === 'error') {
      messageEl.style.backgroundColor = 'rgba(var(--color-error-rgb), 0.1)';
      messageEl.style.color = 'var(--color-error)';
      messageEl.style.border = '1px solid rgba(var(--color-error-rgb), 0.2)';
    } else {
      messageEl.style.backgroundColor = 'rgba(var(--color-success-rgb), 0.1)';
      messageEl.style.color = 'var(--color-success)';
      messageEl.style.border = '1px solid rgba(var(--color-success-rgb), 0.2)';
    }
    
    // Add to form
    form.appendChild(messageEl);
    
    // Remove after 5 seconds
    setTimeout(() => {
      messageEl.remove();
    }, 5000);
  }

  isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  // Utility methods for dynamic content loading
  loadBlogPost(postId) {
    // In a real application, this would fetch post data from an API
    console.log(`Loading Christian blog post: ${postId}`);
    // For now, we'll just show a placeholder message
    this.showFormMessage(
      document.querySelector('.blog-posts'),
      'Full blog post content coming soon! In the meantime, please feel free to contact us with any Christian homeschool questions.',
      'info'
    );
  }

  downloadResource(resourceName) {
    // In a real application, this would trigger a file download
    console.log(`Downloading Christian resource: ${resourceName}`);
    // For demo purposes, show a message
    const resourceCards = document.querySelectorAll('.resource-card');
    const clickedCard = Array.from(resourceCards).find(card => 
      card.querySelector('h3').textContent.includes(resourceName.replace('Download ', '').replace('Cards', '').replace('PDF', '').replace('Templates', '').replace('Checklists', '').replace('Studies', '').replace('Worksheets', ''))
    );
    
    if (clickedCard) {
      this.showFormMessage(
        clickedCard,
        'Christian resource downloads will be available soon! Please join our newsletter to be notified when they\'re ready.',
        'info'
      );
    }
  }

  // Analytics and tracking (placeholder)
  trackEvent(eventName, eventData = {}) {
    console.log('Event tracked:', eventName, eventData);
    // In a real application, this would send data to analytics service
  }

  // Search functionality (placeholder)
  searchBlogPosts(query) {
    const blogPosts = document.querySelectorAll('.blog-post-card');
    const normalizedQuery = query.toLowerCase().trim();
    
    blogPosts.forEach(post => {
      const title = post.querySelector('h2').textContent.toLowerCase();
      const excerpt = post.querySelector('p').textContent.toLowerCase();
      
      if (title.includes(normalizedQuery) || excerpt.includes(normalizedQuery)) {
        post.style.display = 'block';
      } else {
        post.style.display = 'none';
      }
    });
  }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  window.faithfulHomeschoolApp = new FaithfulHomeschoolHavenApp();
  
  // Add event listeners for resource downloads and blog post clicks
  document.addEventListener('click', (e) => {
    const target = e.target;
    
    // Handle resource download buttons
    if (target.textContent.includes('Download') || target.textContent.includes('Take Quiz')) {
      e.preventDefault();
      const resourceCard = target.closest('.resource-card');
      if (resourceCard) {
        const resourceName = resourceCard.querySelector('h3').textContent;
        window.faithfulHomeschoolApp.downloadResource(resourceName);
      }
    }
    
    // Handle blog post "Read More" buttons
    if (target.textContent.includes('Read More') || target.textContent.includes('Read Full Post')) {
      e.preventDefault();
      const postCard = target.closest('.post-card, .blog-post-card');
      if (postCard) {
        const postTitle = postCard.querySelector('h2, h3').textContent;
        window.faithfulHomeschoolApp.loadBlogPost(postTitle);
      }
    }
  });
  
  // Track page views
  window.faithfulHomeschoolApp.trackEvent('page_view', { page: 'home' });
});

// Handle page visibility changes for analytics
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'visible') {
    window.faithfulHomeschoolApp?.trackEvent('page_focus', { 
      section: window.faithfulHomeschoolApp?.currentSection 
    });
  }
});

// Export for potential future use
if (typeof module !== 'undefined' && module.exports) {
  module.exports = FaithfulHomeschoolHavenApp;
}