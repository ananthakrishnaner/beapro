const burger = document.querySelector('.burger')[0];
const nav = document.querySelector('.navbar-ul-inside')[0];

burger.addEventListener('click', ()=>{
    nav.classList.toggle('active');
});
