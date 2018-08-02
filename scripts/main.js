// let wikipedia = document.querySelector('#wikipedia');
// let dictionary = document.querySelector('#dictionary');
// let iframe = document.querySelector('iframe');

//Lower Questions 1
let often = document.querySelector('#often');
let oftendescription = document.querySelector('.lq1')
let whenever = document.querySelector('#whenever')
let wheneverdescription = document.querySelector('.lq2')
let not = document.querySelector('#not');
let notdescription = document.querySelector('.lq3');

function windowfetch(){}

often.addEventListener('click', e => {
  wheneverdescription.style.display = 'none';
  notdescription.style.display = 'none';
  oftendescription.style.display = 'block';
});

whenever.addEventListener('click', e => {
  oftendescription.style.display = 'none';
  notdescription.style.display = 'none';
  wheneverdescription.style.display = 'block';
});

not.addEventListener('click', e => {
  oftendescription.style.display = 'none';
  wheneverdescription.style.display = 'none';
  notdescription.style.display = 'block';
});


// often.addEventListener('click', e => {
//   if(oftendescription.style.display == 'none'){
//     oftendescription.style.display = 'block';
//   } else {
//      oftendescription.style.display = 'none';
//   }
// });

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
