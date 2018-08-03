let uq6not = document.querySelector('#uq6notstarted');
let  notjs = document.querySelector('.notstarted')
let  uq6yes = document.querySelector('#uq6started');
let  yesjs = document.querySelector('.yes')

uq6not.addEventListener('click', e => {
  yesjs.style.display = 'none';
  notjs.style.display = 'block';
});

uq6yes.addEventListener('click', e => {
  notjs.style.display = 'none';
  yesjs.style.display = 'block';
});
