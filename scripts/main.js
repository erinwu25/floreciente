// let wikipedia = document.querySelector('#wikipedia');
// let dictionary = document.querySelector('#dictionary');
// let iframe = document.querySelector('iframe');
let button = document.querySelector('button');
let a = document.querySelector('.lq1');
let b = document.querySelector('.lq2');
let c = document.querySelector('.lq3');

function windowfetch(){}


button.addEventListener('click', e => {
  if(p.style.display == 'none'){
    p.style.display = 'block'; }
  else{
     p.style.display = 'none';

  }
});

let often = document.querySelector('#often');
often.addEventListener('click', e => {
  if(p.style.display == 'none'){
    p.style.display = 'block'; }
  else{
     p.style.display = 'none';
  }
});

let whenever = document.querySelector('#whenever');
whenever.addEventListener('click', e => {
  if(p.style.display == 'none'){
    p.style.display = 'block'; }
  else{
     p.style.display = 'none';
  }
});
let not = document.querySelector('#not');
not.addEventListener('click', e => {
  // if(c.style.display == 'none'){
  //   c.style.display = 'block'; }
  // else{
  //    c.style.display = 'none';
  // }

  header = {
    'Content-Type': 'text/html'
  }
  body = 'study tips'
  window.fetch('/resource', {'headers': header,'method': 'post', 'body': body, 'credentials': 'include'});
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
