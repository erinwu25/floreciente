let ec = document.querySelector('#ec');
let ecdescription = document.querySelector('.ec')
let noec = document.querySelector('#noec');
let noecdescription = document.querySelector('.noec')

ec.addEventListener('click', e => {
  noecdescription.style.display = 'none';
  ecdescription.style.display = 'block';
});

noec.addEventListener('click', e => {
  ecdescription.style.display = 'none';
  noecdescription.style.display = 'block';
});
