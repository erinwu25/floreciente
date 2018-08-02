let apib = document.querySelector('#apib');
let apibdescription = document.querySelector('.apibdescription')
let noapib = document.querySelector('#noapib');
let noapibdescription = document.querySelector('.noapibdescription')

apib.addEventListener('click', e => {
  noapibdescription.style.display = 'none';
  apibdescription.style.display = 'block';
});

noapib.addEventListener('click', e => {
  apibdescription.style.display = 'none';
  noapibdescription.style.display = 'block';
});
