let sat = document.querySelector('#');
let satdescription = document.querySelector('.')
let nosat = document.querySelector('#');
let nosatdescription = document.querySelector('.')

sat.addEventListener('click', e => {
  nosatdescription.style.display = 'none';
  satdescription.style.display = 'block';
});

nosat.addEventListener('click', e => {
  satdescription.style.display = 'none';
  nosatdescription.style.display = 'block';
});
