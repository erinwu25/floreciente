let started = document.querySelector('#started');
let starteddescription = document.querySelector('.starteddescription')
let notstarted = document.querySelector('#notstarted');
let notstarteddescription = document.querySelector('.notstarteddescription')

started.addEventListener('click', e => {
  notstarteddescription.style.display = 'none';
  starteddescription.style.display = 'block';
});

notstarted.addEventListener('click', e => {
  starteddescription.style.display = 'none';
  notstarteddescription.style.display = 'block';
});
