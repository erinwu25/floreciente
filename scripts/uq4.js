let novisit = document.querySelector('#novisit');
let novisitdescription = document.querySelector('.novisitdescription');
let visit = document.querySelector('#visit');
let visitdescription = document.querySelector('.visitdescription');

novisit.addEventListener('click', e => {
  visitdescription.style.display = 'none';
  novisitdescription.style.display = 'block';
});

visit.addEventListener('click', e => {
  novisitdescription.style.display = 'none';
  visitdescription.style.display = 'block';
});
