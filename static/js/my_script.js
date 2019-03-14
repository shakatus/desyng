document.addEventListener('DOMContentLoaded', function() {
  var myElem = document.getElementById('id_base64');
  if (myElem === null){
	}
  else{
var img = new Image();
var div = document.getElementById('id_base64').parentNode;
img.onload = function() {
  div.appendChild(img);
};
img.src = 'data:image/png;base64,'+myElem.value;
	}
})
