window.onload = function() {
  hämtaRecept();
}

const receptListaDiv = document.getElementById("recept");
let allaRecept = [];


function hämtaRecept() {
  const ajaxForfragan = new XMLHttpRequest();
  ajaxForfragan.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      allaRecept = JSON.parse(this.responseText);
      visaRecept(allaRecept);
    }
  };
  ajaxForfragan.open("GET", "recept.json", true);
  ajaxForfragan.send();
}

function visaRecept() {
}