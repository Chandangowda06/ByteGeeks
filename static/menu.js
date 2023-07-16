function menuOpenClose(){
    const mobileMenu = document.querySelector('#menu');
   const btn =  document.querySelector('header nav button');
   if(btn.innerHTML == '<i class="fa fa-bars"></i>'){
    btn.innerHTML = "<i class=\"fa fa-close\"></i>";
   }
   else{
    btn.innerHTML = '<i class="fa fa-bars"></i>';
   }
   if(mobileMenu.className === ''){
    mobileMenu.className = 'menu-mobile';
   }
   else{
    mobileMenu.className = '';
   }
}
