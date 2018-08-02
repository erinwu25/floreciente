let scholarships = document.querySelector('#scholarships');
let scholarshipsdescription = document.querySelector('.scholarshipsdescription')
let noscholarships = document.querySelector('#noscholarships');
let noscholarshipsdescription = document.querySelector('.noscholarshipsdescription')

scholarships.addEventListener('click', e => {
  noscholarshipsdescription.style.display = 'none';
  scholarshipsdescription.style.display = 'block';
});

noscholarships.addEventListener('click', e => {
  scholarshipsdescription.style.display = 'none';
  noscholarshipsdescription.style.display = 'block';
});
