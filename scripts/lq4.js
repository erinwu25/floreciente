let nostudy = document.querySelector('#nostudy');
let nostudydescription = document.querySelector('.nostudydescription')
let study = document.querySelector('#study');
let studydescription = document.querySelector('.studydescription')

nostudy.addEventListener('click', e => {
  studydescription.style.display = 'none';
  nostudydescription.style.display = 'block';
});

study.addEventListener('click', e => {
  nostudydescription.style.display = 'none';
  studydescription.style.display = 'block';
});
