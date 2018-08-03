let ywrite = document.querySelector('#ywrite');
let ywritedescription = document.querySelector('.ywritedescription')
let nwrite = document.querySelector('#nwrite');
let nwritedescription = document.querySelector('.nwritedescription')

ywrite.addEventListener('click', e => {
  nwritedescription.style.display = 'none';
  ywritedescription.style.display = 'block';
});

nwrite.addEventListener('click', e => {
  ywritedescription.style.display = 'none';
  nwritedescription.style.display = 'block';
});
