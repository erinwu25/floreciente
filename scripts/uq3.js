let sat = document.querySelector('#sat');
let satdescription = document.querySelector('.satdescription')
let nosat = document.querySelector('#nosat');
let nosatdescription = document.querySelector('.nosatdescription')

sat.addEventListener('click', e => {
  nosatdescription.style.display = 'none';
  satdescription.style.display = 'block';
});

nosat.addEventListener('click', e => {
  satdescription.style.display = 'none';
  nosatdescription.style.display = 'block';
});
