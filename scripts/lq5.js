let nocareer = document.querySelector('#nocareer');
let nocareerdescription = document.querySelector('.nocareer')
let career = document.querySelector('#career');
let careerdescription = document.querySelector('.career')

nocareer.addEventListener('click', e => {
  careerdescription.style.display = 'none';
  nocareerdescription.style.display = 'block';
});

career.addEventListener('click', e => {
  nocareerdescription.style.display = 'none';
  careerdescription.style.display = 'block';
});
