let checklistbutton = document.querySelector('#myUL');
let resourcebutton = document.querySelector('#resource')

checklistbutton.addEventListener('click', e => {
  resourcebutton.classList.toggle('checked');
});
