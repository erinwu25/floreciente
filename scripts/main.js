

//Lower Questions 1
let often = document.querySelector('#often');
let oftendescription = document.querySelector('.lq1')
let whenever = document.querySelector('#whenever')
let wheneverdescription = document.querySelector('.lq2')
let not = document.querySelector('#not');
let notdescription = document.querySelector('.lq3');

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




  // header = {
  //   'Content-Type': 'text/html'
  // }
  // body = 'study tips'
  // window.fetch('/resource', {'headers': header,'method': 'post', 'body': body, 'credentials': 'include'});
