let checklistbutton = document.querySelectorAll('.myUL');
//let resourcebutton = document.querySelectorAll('.resource')

for(let button of checklistbutton){
  button.addEventListener('click', e => {
  button.querySelector('.resource').classList.toggle('checked');
});
}
