window.onload = (event) => {
  console.log('page is fully loaded');
};

var del_btn = document.getElementById(delete);




var ischecked =$('input[type=checkbox]:checked').length;

if (ischecked > 0){
  del_btn.style.background = red;
  del_btn.style.disabled = false;

}
else{
  del_btn.style.background = grey;
del_btn.style.disabled = true;
}
