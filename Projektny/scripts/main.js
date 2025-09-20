window.onload = function() {
  hämtaRecept();
}

const receptListaDiv = document.getElementById("lista-alla-recept");
let allaRecept = [];

// Funktion för att hämta recept från en fil 
function hämtaRecept() {
  const ajaxForfragan = new XMLHttpRequest();
  ajaxForfragan.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      allaRecept = JSON.parse(this.responseText);
      visaRecept(allaRecept);
    }
  };
  ajaxForfragan.open("GET", "recipes.json", true);
  ajaxForfragan.send();
}

// Funktion för att visa recept på sidan
function visaRecept(receptAttVisa) {
  let receptHTML = "";
  for (let i = 0; i < receptAttVisa.length; i++) {
    const recept = receptAttVisa[i];
    receptHTML += `
      <div class="recipe-card">
        <h3>${recept.title}</h3>
        <p><strong>Beskrivning:</strong> ${recept.description}</p>
        <p><strong>Ingredienser:</strong> ${recept.ingredients}</p>
        <p><strong>Instruktioner:</strong> ${recept.instructions}</p>
        <div class="interaction-buttons">
          <button onclick="gillaRecept(${i})">👍 ${recept.likes}</button>
          <button onclick="kommenteraRecept(${i})">Kommentera</button>
        </div>
        <div id="kommentarer-${i}" class="kommentarer"></div>
      </div>
    `;
  }
  receptListaDiv.innerHTML = receptHTML;
}