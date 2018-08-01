// let wikipedia = document.querySelector('#wikipedia');
// let dictionary = document.querySelector('#dictionary');
// let iframe = document.querySelector('iframe');
let button = document.querySelector('button');
let p = document.querySelector('.lq1');

button.addEventListener('click', e => {
  if(p.style.display == 'none'){
    p.style.display = 'block'; }
  else{
     p.style.display = 'none';

  }
});

//wikipedia.remove();
//wikipedia.innerText = 'Google.com';
// wikipedia.style.backgroundColor = 'pink'
// wikipedia.innerHTML = '<button>click me</button>'

// wikipedia.addEventListener('dblclick', e => {
//   iframe.src = 'https://en.wikipedia.org/'
// });
//
// dictionary.addEventListener('dblclick', e => {
//   iframe.src = 'https://dictionary.com/'
// });

// window.addEventListener('keydown', e => {
//   if (e.key == 'ArrowLeft'){
//     window.location.href = '/';
//   }
//   else if (e.key == 'ArrowRight'){
//     window.location.href = '/second';
//
//   }
// });
