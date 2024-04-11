let language_code = document.getElementById('language_code').value; 
let all_content = document.getElementById('all_content'); 
let btn_en = document.getElementById('eng');
let btn_ar = document.getElementById('ara');
let public_key ; 
if (language_code == 'en'){
  all_content.dir = 'ltr';
  all_content.lang = 'en';
  btn_en.disabled = true;
}else{
  all_content.dir = 'rtl';
  all_content.lang = 'ar';
  btn_ar.disabled = true;
}

