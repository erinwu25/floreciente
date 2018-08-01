let wikipedia = document.querySelector('#wikipedia');
let dictionary = document.querySelector('#dictionary');
let iframe = document.querySelector('iframe');
let button = document.querySelector('button');

button.addEventListener('click', e => {
  // let img = document.createElement('img');
  // img.src = 'https://thumbs-prod.si-cdn.com/azaY6UJQr6w7GMO5NScOuYhUbIM=/800x600/filters:no_upscale()/https://public-media.smithsonianmag.com/filer/ef/ff/efff9ae5-1832-489f-bb1f-f1a00944a8aa/hedgehog.jpg'
  // img.height = '100'
  // document.body.appendChild(img);
  let p = document.querySelector('p');
  if(p.style.display == 'none'){
    p.style.display = 'block'; }
  else{
    p.style.display = 'none';

  }
});

//wikipedia.remove();
//wikipedia.innerText = 'Google.com';
// wikipedia.style.backgroundColor = 'pink'
// wikipedia.innerHTML = '<button>click me</button>'

// wikipedia.addEventListener('dblclick', e => {
//   iframe.src = 'https://en.wikipedia.org/'
// });
//
// dictionary.addEventListener('dblclick', e => {
//   iframe.src = 'https://dictionary.com/'
// });

window.addEventListener('keydown', e => {
  if (e.key == 'ArrowLeft'){
    window.location.href = '/';
  }
  else if (e.key == 'ArrowRight'){
    window.location.href = '/second';

  }
});
