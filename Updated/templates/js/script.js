// get all the toggle buttons
const toggleButtons = document.querySelectorAll('.faq-toggle');

// loop through all the toggle buttons and add a click event listener to each
toggleButtons.forEach(function(button) {
  button.addEventListener('click', function() {
    // get the corresponding answer element
    const answer = this.parentElement.parentElement.querySelector('.faq-answer');
    // toggle the active class on the answer element
    answer.classList.toggle('active');
    // toggle the active class on the toggle button element
    this.classList.toggle('active');
  });
});

const sliderImages = document.querySelectorAll('.slider-image');

let currentImage = 0;
sliderImages[currentImage].classList.add('active');

setInterval(() => {
  sliderImages[currentImage].classList.remove('active');
  currentImage = (currentImage + 1) % sliderImages.length;
  sliderImages[currentImage].classList.add('active');
}, 5000); // change the images every 5 seconds (adjust as necessary)

document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('.reco-form form');
  const recoInput = document.querySelector('.book-recommendation');
  const recoOutput = document.querySelector('.recommendation-results');

  // Hide the output section initially
  recoOutput.style.display = 'none';

  form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Show the output section and hide the input section
    recoInput.style.display = 'none';
    recoOutput.style.display = 'block';
  });
});

