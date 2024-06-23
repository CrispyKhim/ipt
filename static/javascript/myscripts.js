// The Cat API
const url = `https://api.thecatapi.com/v1/breeds`;

const api_key = "live_ug7L3YzsrAvPthkUAcOVWqHTJfnd4b6u1NFao0EhLllQDwmokv9iEXeUgQOuoljn";

// a variable to store the information about the breeds

let storedBreeds = [];

// a function to select a random breed

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}


// a function to show images and information of the breeds
function showCatImageAndInformation(index) {

// This will display the image of the cat
document.getElementById("cat_image").src = storedBreeds[index].image.url;

// This will get the breed name
document.getElementById("breed_name").innerHTML = storedBreeds[index].name;

// This will get the wiki link
document.getElementById("wiki_link").href = storedBreeds[index].wikipedia_url;

document.getElementById("wiki_link").innerHTML =
  storedBreeds[index].wikipedia_url;  

// This will get the characteristics of the cat
document.getElementById("breed_json").textContent =
  storedBreeds[index].temperament;
}


// a function to retrieve data from the API
fetch(url, {
headers: {
  "x-api-key": api_key,
},
})
.then((response) => {
  return response.json();
})
.then((data) => {
  // Storing the retrieved data from the API in our variable
  storedBreeds = data;


  // Using the random function to select a specific breed. Then extracting information from that breed
  showCatImageAndInformation(getRandomInt(0, storedBreeds.length - 1));
})
.catch(function (error) {
  console.log(error);
});




// Share button
const shareBtn = document.querySelector('.share-btn');
const shareOptions = document.querySelector('.share-options');

shareBtn.addEventListener('click', () => {
  shareOptions.classList.toggle('active');
})



// Scroll Down Button (Index)
$(function() {
  $('a[href*#]').on('click', function(e) {
    e.preventDefault();
    $('html, body').animate({ scrollTop: $($(this).attr('href')).offset().top}, 500, 'linear');
  });
});

// Helper 
function normalizeRange(value, originalMin, originalMax, newMin, newMax) {
  var originalRange = originalMax - originalMin;
  var newRange = newMax - newMin;
  return (((value - originalMin) * newRange) / originalRange) + newMin;
};
// Button animation
const GlowingButtonModule = {
  init: function (button) {
    const normalizedLocalCursorPos = { x: 0, y: 0 };
    const glowElements = button.querySelectorAll(".GlowingButton__glowWrap span");
    const leftGlow = button.querySelector(".GlowingButton__glowWrap.l span");
    const rightGlow = button.querySelector(".GlowingButton__glowWrap.r span");
    const rect = button.getBoundingClientRect(),
    buttonWidth = button.clientWidth,
    buttonHeight = button.clientHeight;

    button.addEventListener("mousemove", function (e) {
      normalizedLocalCursorPos.x = normalizeRange(e.clientX - rect.left, 0, buttonWidth, -20, 20);
      normalizedLocalCursorPos.y = normalizeRange(e.clientY - rect.top, 0, buttonHeight, -7, 7);
      anime({
          targets: glowElements,
          translateX: `${normalizedLocalCursorPos.x}`,
          translateY: `${normalizedLocalCursorPos.y}`
      });
    });
    button.addEventListener("mouseleave", function () {
      anime({
        targets: glowElements,
        translateX: 0,
        translateY: 0
      });
    })
  }
}
const buttons = document.querySelectorAll(".GlowingButton");
buttons.forEach((button) => {
  new GlowingButtonModule.init(button);
});