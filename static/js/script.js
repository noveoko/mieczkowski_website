var lang = 'pl'; // Initial language
var elements = document.querySelectorAll('[data-en]');
var button = document.getElementById('switch-lang');

function switchLang() {
  lang = (lang == 'pl') ? 'pl' : 'en';
  button.textContent = (lang == 'pl') ? 'PL' : 'EN';
  elements.forEach(function(element) {
    element.textContent = element.dataset[lang];
  });
}

button.addEventListener('click', switchLang);